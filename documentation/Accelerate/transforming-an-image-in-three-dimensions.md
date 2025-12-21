# Transforming an image in three dimensions

**Framework**: Accelerate

Create and use a projective transformation to apply a perspective warp to an image.

#### Overview

The vImage library provides a set of functions that allow you create projective-transformation structures and apply them to images. The following image shows the effect of a projective transformation that derives from the four corner points of a perspective distorted rectangle. The image demonstrates how the projective transformation warps the image to match the empty billboard rectangle.

![A flow diagram of two images. On the left is a photograph of an empty picture frame, and on the right is the same image with a photograph of a palm tree composited over the picture frame. The photograph has been taken at an angle so that the picture frame is subject to perspective distortion. The composite image shows the palm tree image warped to fit the distorted frame.](https://docs-assets.developer.apple.com/published/1defa86f6cf143f437a019749fbe43df/media-4098130%402x.png)

##### Create the Vimage Buffers That Represent the Source Images

Create a [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure that describes the four-channel, 8-bit-per-channel images that this example uses.

```swift
var format = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 4,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue))!
```

Use separate buffers to store the background and foreground images.

```swift
let backgroundImage =  imageLiteral(resourceName: "background.jpg").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!
let backgroundBuffer = try vImage.PixelBuffer<vImage.Interleaved8x4>(
    cgImage: backgroundImage,
    cgImageFormat: &format)

let foregroundImage =  imageLiteral(resourceName: "foreground.jpg").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!
let foregroundBuffer = try vImage.PixelBuffer<vImage.Interleaved8x4>(
    cgImage: foregroundImage,
    cgImageFormat: &format)

```

Because the perspective warp doesn’t work in place (that is, the source and destination buffers need to point to different underlying memory), create a third destination buffer.

```swift
let warpedBuffer = vImage.PixelBuffer<vImage.Interleaved8x4>(
    size: backgroundBuffer.size)
```

##### Use the Vision Framework to Find the Rectangle Corner Points

The [`Vision`](https://developer.apple.com/documentation/Vision) framework allows you to find the corner points of the target rectangle. The code below is a simplified example. See [`Detecting Objects in Still Images`](https://developer.apple.com/documentation/Vision/detecting-objects-in-still-images) for additional information.

```swift
let imageRequestHandler = VNImageRequestHandler(cgImage: backgroundImage,
                                                options: [:])

let requests: [VNRequest] = [VNDetectRectanglesRequest()]

try imageRequestHandler.perform(requests)

guard let observation = requests.first?.results?.first as? VNRectangleObservation  else {
    throw vImage.Error.internalError
}
```

On return, `observation` contains the four corner points of the target rectangle.

##### Create the Source and Destination Points

Use the values in the Vision [`VNRectangleObservation`](https://developer.apple.com/documentation/Vision/VNRectangleObservation) instance to create a set of points for the vImage warp function. The Vision framework returns normalized coordinates in the range `0...1` with `0` at the bottom-left of the image. The vImage warp function requires coordinates that represent pixel values with `0` at the top-left of the image.

The destination points refer to the corner points of the target rectangle.

```swift
typealias vImagePoint = (Float, Float)

let dstPoints: [vImagePoint] = {
    func scalePoint(_ point: CGPoint) -> vImagePoint {
        return (Float(point.x) * Float(backgroundImage.width),
                Float(point.y) * Float(backgroundImage.height))
    }
    
    let dstTopLeft: vImagePoint = scalePoint(observation.topLeft)
    let dstTopRight: vImagePoint = scalePoint(observation.topRight)
    let dstBottomLeft: vImagePoint = scalePoint(observation.bottomLeft)
    let dstBottomRight: vImagePoint = scalePoint(observation.bottomRight)
    
    return [dstTopLeft, dstTopRight, dstBottomLeft, dstBottomRight]
}()

```

The source points refer to the bounding box of the foreground image.

```swift
let srcPoints: [vImagePoint] = {
    let foregroundWidth = Float(foregroundImage.width)
    let foregroundHeight = Float(foregroundImage.height)
    
    let srcTopLeft: (Float, Float) = (0, foregroundHeight)
    let srcTopRight: (Float, Float) = (foregroundWidth, foregroundHeight)
    let srcBottomLeft: (Float, Float) = (0, 0)
    let srcBottomRight: (Float, Float) = (foregroundWidth, 0)
    
    return [srcTopLeft, srcTopRight, srcBottomLeft, srcBottomRight]
}()

```

##### Calculate the Projective Transformation

Call [`vImageGetPerspectiveWarp(_:_:_:_:)`](vimagegetperspectivewarp(_:_:_:_:).md) to calculate the projective transformation to translate the foreground image to the target rectangle.

```swift
var transform = vImage_PerpsectiveTransform()
vImageGetPerspectiveWarp(srcPoints, dstPoints, &transform, 0)

```

On return, `transform` contains the projective transformation to warp the source points to the destination points.

##### Apply the Perspective Warp

Call [`vImagePerspectiveWarp_ARGB8888(_:_:_:_:_:_:_:)`](vimageperspectivewarp_argb8888(_:_:_:_:_:_:_:).md) to warp the foreground image to the destination rectangle’s shape and position.

```swift
foregroundBuffer.withUnsafePointerToVImageBuffer { src in
    warpedBuffer.withUnsafePointerToVImageBuffer { dst in
        
        var bgColor: [UInt8] = [0, 0, 0, 0]
        
        vImagePerspectiveWarp_ARGB8888(
            src, dst, nil,
            &transform,
            vImage_WarpInterpolation(kvImageInterpolationLinear),
            &bgColor,
            vImage_Flags(kvImageBackgroundColorFill))
    }
}

```

##### Composite the Warped Foreground Over the Background Image

Finally, composite the warped foreground image over the background image.

```swift
backgroundBuffer.alphaComposite(.nonpremultiplied,
                                topLayer: warpedBuffer,
                                destination: backgroundBuffer)

let result = backgroundBuffer.makeCGImage(cgImageFormat: format)

```

## See Also

- [func vImageGetPerspectiveWarp(UnsafePointer<(Float, Float)>, UnsafePointer<(Float, Float)>, UnsafeMutablePointer<vImage_PerpsectiveTransform>, vImage_Flags) -> vImage_Error](vimagegetperspectivewarp(_:_:_:_:).md)
  Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.
- [struct vImage_PerpsectiveTransform](vimage_perpsectivetransform.md)
  A projective-transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/transforming-an-image-in-three-dimensions)*