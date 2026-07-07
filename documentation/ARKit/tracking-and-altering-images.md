# Tracking and altering images

**Framework**: ARKit

Create images from rectangular shapes found in the user’s environment, and augment their appearance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 16.0+

#### Overview

To demonstrate general image recognition, this sample app uses Vision to detect rectangular shapes in the user’s environment that are most likely artwork or photos. Run the app on an iPhone or iPad, and point the device’s camera at a movie poster or wall-mounted picture frame. When the app detects a rectangular shape, you extract the pixel data defined by that shape from the camera feed to create an image.

The sample app changes the appearance of the image by applying a Core ML model that performs a stylistic alteration. By repeating this action in succession, you achieve real-time image processing using a trained neural network.

To complete the effect of augmenting an image in the user’s environment, you use ARKit’s image tracking feature. ARKit can hold an altered image steady over the original image as the user moves the device in their environment. ARKit also tracks the image if it moves on its own, as when the app recognizes a banner on the side of a bus, and the bus begins to drive away.

![Screenshot of the app in use. In the center of the user's view, there's a wall art picture being augmented with a stylistic image processing filter.](https://docs-assets.developer.apple.com/published/01ff7efe738d079880b1554c23f01de8/rendered2x-1584985272.png)

This sample app uses SceneKit to render its graphics.

#### Detect Rectangular Shapes in the Users Environment

As shown below, you can use Vision in real-time to check the camera feed for rectangles. You perform this check up to 10 times a second by using `RectangleDetector` to schedule a repeating timer with an `updateInterval` of `0.1` seconds.

```swift
init() {
    self.updateTimer = Timer.scheduledTimer(withTimeInterval: updateInterval, repeats: true) { [weak self] _ in
        if let capturedImage = ViewController.instance?.sceneView.session.currentFrame?.capturedImage {
            self?.search(in: capturedImage)
        }
    }
}
```

Because Vision requests can be taxing on the processor, check the camera feed no more than 10 times a second. Checking for rectangles more frequently may cause the app’s frame rate to decrease, without noticeably improving the app’s results.

When you make Vision requests in real-time with an ARKit–based app, you should do so serially. By waiting for one request to finish before invoking another, you ensure that the AR experience remains smooth and free of interruptions. In the `search` function, you use the `isBusy` flag to ensure you’re only checking for one rectangle at a time:

```swift
private func search(in pixelBuffer: CVPixelBuffer) {
    guard !isBusy else { return }
    isBusy = true
    
    // ...
}
```

The sample sets the `isBusy` flag to `false` when a Vision request completes or fails.

#### Crop the Camera Feed to an Observed Rectangle

When Vision finds a rectangle in the camera feed, it provides you with the rectangle’s precise coordinates through a [`VNRectangleObservation`](https://developer.apple.com/documentation/Vision/VNRectangleObservation). You apply those coordinates to a Core Image perspective correction filter to crop it, leaving you with just the image data inside the rectangular shape.

```swift
private func completedVisionRequest(_ request: VNRequest?, error: Error?) {
    defer {
        isBusy = false
    }
    // Only proceed if a rectangular image was detected.
    guard let rectangle = request?.results?.first as? VNRectangleObservation else {
        guard let error = error else { return }
        print("Error: Rectangle detection failed - Vision request returned an error. \(error.localizedDescription)")
        return
    }
    guard let filter = CIFilter(name: "CIPerspectiveCorrection") else {
        print("Error: Rectangle detection failed - Could not create perspective correction filter.")
        return
    }
    let width = CGFloat(CVPixelBufferGetWidth(currentCameraImage))
    let height = CGFloat(CVPixelBufferGetHeight(currentCameraImage))
    let topLeft = CGPoint(x: rectangle.topLeft.x * width, y: rectangle.topLeft.y * height)
    let topRight = CGPoint(x: rectangle.topRight.x * width, y: rectangle.topRight.y * height)
    let bottomLeft = CGPoint(x: rectangle.bottomLeft.x * width, y: rectangle.bottomLeft.y * height)
    let bottomRight = CGPoint(x: rectangle.bottomRight.x * width, y: rectangle.bottomRight.y * height)
    
    filter.setValue(CIVector(cgPoint: topLeft), forKey: "inputTopLeft")
    filter.setValue(CIVector(cgPoint: topRight), forKey: "inputTopRight")
    filter.setValue(CIVector(cgPoint: bottomLeft), forKey: "inputBottomLeft")
    filter.setValue(CIVector(cgPoint: bottomRight), forKey: "inputBottomRight")
    
    let ciImage = CIImage(cvPixelBuffer: currentCameraImage).oriented(.up)
    filter.setValue(ciImage, forKey: kCIInputImageKey)
    
    guard let perspectiveImage: CIImage = filter.value(forKey: kCIOutputImageKey) as? CIImage else {
        print("Error: Rectangle detection failed - perspective correction filter has no output image.")
        return
    }
    delegate?.rectangleFound(rectangleContent: perspectiveImage)
}
```

Using the first image in the Overview, the camera image is:

![Screenshot of the session's uncropped camera feed.](https://docs-assets.developer.apple.com/published/198fd6717e1a4258e07ac10037e6ebb0/rendered2x-1662142496.png)

The cropped result is:

![Screenshot of the camera feed that's been cropped to just the rectangular shape that Vision observed.](https://docs-assets.developer.apple.com/published/87fab06f33ca2e073cba6d3e5ba6dd1e/rendered2x-1662142494.png)

#### Create a Reference Image

To prepare to track the cropped image, you create an [`ARReferenceImage`](arreferenceimage.md), which provides ARKit with everything it needs, like its look and physical size, to locate that image in the physical environment.

```swift
let possibleReferenceImage = ARReferenceImage(referenceImagePixelBuffer, 
                                              orientation: .up, 
                                              physicalWidth: CGFloat(0.5))
```

ARKit requires that reference images contain sufficient detail to be recognizable; for example, a plain white image cannot be tracked. To prevent ARKit from failing to track a reference image, you validate it first before attempting to use it.

```swift
possibleReferenceImage.validate { [weak self] (error) in
    if let error = error {
        print("Reference image validation failed: \(error.localizedDescription)")
        return
    }
    // ...
```

#### Track the Image Using Arkit

Provide the reference image to ARKit to get updates on where the image lies in the camera feed when the user moves their device. Do that by creating an image tracking session and passing the reference image in to the configuration’s [`trackingImages`](arimagetrackingconfiguration/trackingimages.md).

```swift
let configuration = ARImageTrackingConfiguration()
configuration.maximumNumberOfTrackedImages = 1
configuration.trackingImages = trackingImages
sceneView.session.run(configuration, options: runOptions)
```

Vision made the initial observation about where the image lies in 2D space in the camera feed, but ARKit resolves its location in 3D space, in the physical environment. When ARKit succeeds in recognizing the image, it creates an [`ARImageAnchor`](arimageanchor.md) and a SceneKit node at the right position. You save the anchor and node that ARKit gives you by passing them to an `AlteredImage` object.

```swift
func renderer(_ renderer: SCNSceneRenderer, didAdd node: SCNNode, for anchor: ARAnchor) {
    alteredImage?.add(anchor, node: node)
    setMessageHidden(true)
}
```

#### Alter the Images Appearance Using Core Ml

This sample app is bundled with a Core ML model that performs image processing. Given an input image and an integer index, the model outputs a visually modified version of that image in one of eight different styles. The particular style of the output depends on the value of the index you pass in. The first style resembles burned paper, the second style resembles a mosaic, and there are six other styles as shown in the following image.

![Figure that shows screenshots of each of the 8 different artistic styles applied to a recognized image. At left, the original is shown with no style applied.](https://docs-assets.developer.apple.com/published/18929b5d1b62a8f2afeeea1250be938a/rendered2x-1584985287.png)

When Vision finds a rectangular shape in the user’s environment, you pass the camera’s image data defined by that rectangle into a new `AlteredImage`.

```swift
guard let newAlteredImage = AlteredImage(rectangleContent, referenceImage: possibleReferenceImage) else { return }
```

The following code shows how you choose the artistic style to apply to the image by inputting the integer index to the Core ML model. Then, you process the image by calling the Core ML model’s [`predictions(from:options:)`](https://developer.apple.com/documentation/CoreML/MLModel/predictions(from:options:)).

```swift
let input = StyleTransferModelInput(image: self.modelInputImage, index: self.styleIndexArray)
let output = try AlteredImage.styleTransferModel.prediction(input: input, options: options)
```

The following figure shows the result when you process the input image with a style index of 2.

![Screenshot of altered image that's the result of inputting the cropped image in to the Core ML model.](https://docs-assets.developer.apple.com/published/42757aa9eb35d1542b88deb6bb44490d/rendered2x-1584985290.png)

#### Display the Altered Image in Augmented Reality

To complete the augmented reality effect, you cover the original image with the altered image. First, add a visualization node to hold the altered image as a child of the node provided by ARKit.

```swift
node.addChildNode(visualizationNode)
```

When Core ML produces the output image, you call `imageAlteringComplete(_:)` to pass the model’s output image into the visualization node’s `display` function, where you set the image as the visualization node’s contents.

```swift
func imageAlteringComplete(_ createdImage: CVPixelBuffer) {
    guard fadeBetweenStyles else { return }
    modelOutputImage = createdImage
    visualizationNode.display(createdImage)
}
```

The visualization node’s contents overlap the original image when SceneKit displays it. In the case of the image above, the following screenshot shows the end result as seen through a user’s device:

![Screenshot of the altered image overlay on the camera feed.](https://docs-assets.developer.apple.com/published/6684f66bc785993bb4b4d6e166afe87a/rendered2x-1584985292.png)

#### Continually Update the Images Appearance

This sample demonstrates real-time image processing by switching artistic styles over time. By calling `selectNextStyle`, you can make successive alterations of the original image. `styleIndex` is the integer input to the Core ML model that determines the style of the output.

```swift
func selectNextStyle() {
    styleIndex = (styleIndex + 1) % numberOfStyles
}
```

The sample’s `VisualizationNode` fades between two images of differing style, which creates the effect that the tracked image is constantly transforming into a new look. You accomplish this effect by defining two SceneKit nodes. One node displays the current altered image, and the other displays the previous altered image.

```swift
private let currentImage: SCNNode
private let previousImage: SCNNode
```

You fade between these two nodes by running an opacity animation:

```swift
SCNTransaction.begin()
SCNTransaction.animationDuration = fadeDuration
currentImage.opacity = 1.0
previousImage.opacity = 0.0
SCNTransaction.completionBlock = {
    self.delegate?.visualizationNodeDidFinishFade(self)
}
SCNTransaction.commit()
```

When the animation finishes, you begin altering the original image with the next artistic style by calling `createAlteredImage` again:

```swift
func visualizationNodeDidFinishFade(_ visualizationNode: VisualizationNode) {
    guard fadeBetweenStyles, anchor != nil else { return }
    selectNextStyle()
    createAlteredImage()
}
```

#### Respond to Image Tracking Updates

As part of the image tracking feature, ARKit continues to look for the image throughout the AR session. If the image itself moves, ARKit updates the [`ARImageAnchor`](arimageanchor.md) with its corresponding image’s new location in the physical environment, and calls your delegate’s [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md) to notify your app of the change.

```swift
func renderer(_ renderer: SCNSceneRenderer, didUpdate node: SCNNode, for anchor: ARAnchor) {
    alteredImage?.update(anchor)
}
```

The sample app tracks a single image at a time. To do that, you invalidate the current image tracking session if an image the app was tracking is no longer visible. This, in turn, enables Vision to start looking for a new rectangular shape in the camera feed.

```swift
func update(_ anchor: ARAnchor) {
    if let imageAnchor = anchor as? ARImageAnchor, self.anchor == anchor {
        self.anchor = imageAnchor
        // Reset the timeout if the app is still tracking an image.
        if imageAnchor.isTracked {
            resetImageTrackingTimeout()
        }
    }
}
```

## See Also

- [Detecting Images in an AR Experience](detecting-images-in-an-ar-experience.md)
  React to known 2D images in the user’s environment, and use their positions to place AR content.
- [Tracking preregistered images in 3D space](../visionOS/tracking-images-in-3d-space.md)
  Place content based on the current position of a known image in a person’s surroundings.
- [class ImageTrackingProvider](imagetrackingprovider.md)
  A source of live data about a 2D image’s position in a person’s surroundings.
- [struct ImageAnchor](imageanchor.md)
  A 2D image’s position in a person’s surroundings.
- [struct ReferenceImage](referenceimage.md)
  A 2D image the system uses as a reference to find the same image in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/tracking-and-altering-images)*