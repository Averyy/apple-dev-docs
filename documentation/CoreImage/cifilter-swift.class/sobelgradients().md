# sobelGradients()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Calculates the Sobel gradients for an image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func sobelGradients() -> any CIFilter & CISobelGradients
```

```objc
+ (CIFilter<CISobelGradients> *) sobelGradientsFilter;
```

## Return Value

A [`CIImage`](../ciimage.md) containing the Sobel gradients.

## Discussion

This filter applies the Sobel operator to the color components of the input image. You would typically use the Sobel filter as part of an edge-detection algorithm for performing.

- **`inputImage`**: A [`CIImage`](../ciimage.md) containing the image to process.

The following code applies the [`sobelGradients()`](./sobelgradients%28%29.md) filter to an image.

```swift
func sobelGradients(inputImage: CIImage) -> CIImage {
    let sobel = CIFilter.sobelGradients()
    sobel.inputImage = inputImage
    return sobel.outputImage!
}
```

![Two images arranged horizontally. The left image is a photograph of modern building with horizontal concrete beams and large tinted windows. The image on the right shows the result of applying the Sobel gradients filter. Edges in the image are highlighted and flat areas of the image are set to black.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407283@2x.png)

## See Also

### Filters
- [class func blendWithAlphaMask() -> any CIFilter & CIBlendWithMask](./blendwithalphamask%28%29.md)
  Blends two images by using an alpha mask image.
- [class func blendWithBlueMask() -> any CIFilter & CIBlendWithMask](./blendwithbluemask%28%29.md)
  Blends two images by using a blue mask image.
- [class func blendWithMask() -> any CIFilter & CIBlendWithMask](./blendwithmask%28%29.md)
  Blends two images by using a mask image.
- [class func blendWithRedMask() -> any CIFilter & CIBlendWithMask](./blendwithredmask%28%29.md)
  Blends two images by using a red mask image.
- [class func bloom() -> any CIFilter & CIBloom](./bloom%28%29.md)
  Adjusts an image’s colors by applying a blur effect.
- [class func cannyEdgeDetector() -> any CIFilter & CICannyEdgeDetector](./cannyedgedetector%28%29.md)
  Applies the Canny edge-detection algorithm to an image.
- [class func comicEffect() -> any CIFilter & CIComicEffect](./comiceffect%28%29.md)
  Creates an image with a comic book effect.
- [class func coreMLModel() -> any CIFilter & CICoreMLModel](./coremlmodel%28%29.md)
  Filters an image with a Core ML model.
- [class func crystallize() -> any CIFilter & CICrystallize](./crystallize%28%29.md)
  Creates an image made with a series of colorful polygons.
- [class func depthOfField() -> any CIFilter & CIDepthOfField](./depthoffield%28%29.md)
  Simulates a depth of field effect.
- [class func edges() -> any CIFilter & CIEdges](./edges%28%29.md)
  Hilghlights edges of objects found within an image.
- [class func edgeWork() -> any CIFilter & CIEdgeWork](./edgework%28%29.md)
  Produces a black-and-white image that looks similar to a woodblock print.
- [class func gaborGradients() -> any CIFilter & CIGaborGradients](./gaborgradients%28%29.md)
  Highlights textures in an image.
- [class func gloom() -> any CIFilter & CIGloom](./gloom%28%29.md)
  Adjusts an image’s color by applying a gloom filter.
- [class func heightFieldFromMask() -> any CIFilter & CIHeightFieldFromMask](./heightfieldfrommask%28%29.md)
  Creates a realistic shaded height-field image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/sobelgradients())*