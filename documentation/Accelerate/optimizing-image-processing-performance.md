# Optimizing image-processing performance

**Framework**: Accelerate

Improve your app’s performance by converting image buffer formats from interleaved to planar.

#### Overview

The vImage library operates on image data with two memory layouts:

 stores each pixel’s color data consecutively in a single buffer. For example, the data that describes a 4-channel image (red, green, blue, and alpha) would be stored as RGBARGBARGBA…

 stores each color channel in separate buffers. For example, a 4-channel image would be stored as four individual buffers containing red, green, blue, and alpha data.

![A diagram showing how the color information for each pixel in an image is stored in interleaved and planar buffers.](https://docs-assets.developer.apple.com/published/9ca5720cecfccf9a40e29dcb8dfb8134/media-3023512%402x.png)

Because many vImage functions operate on a single color channel at a time — by converting an interleaved buffer to planar buffers — you can often improve your app’s performance by doing this conversion manually. However, most vImage functions are available in both the interleaved and planar variants, so before you do the conversion, try both to see which works better in your context.

In some cases, you may not want to apply a vImage operation to all four channels of an image. For example, you may know beforehand that the alpha channel is irrelevant in the images that you’re dealing with, or perhaps all of your images are grayscale and you need to operate on only one channel. Using planar formats makes it possible to isolate and work with only the channels you need.

##### Review Interleaved Performance

Typically, your source imagery is in interleaved format, and your default option will be to use the interleaved variant of a vImage function. For example, the following code scales a Core Graphics image to one tenth of its original size. Note that the 4-channel, 8-bit-per-channel interleaved pixel buffer [`scale(destination:)`](vimage/pixelbuffer/scale(destination:)-5euvc.md) function calls [`vImageScale_ARGB8888(_:_:_:_:)`](vimagescale_argb8888(_:_:_:_:).md).

```swift
var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 4,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue:
                                CGImageAlphaInfo.noneSkipLast.rawValue))!

let sourceBuffer = try vImage.PixelBuffer(cgImage: sourceImage,
                                          cgImageFormat: &cgImageFormat,
                                          pixelFormat: vImage.Interleaved8x4.self)

let destinationBuffer = vImage.PixelBuffer(size: .init(width: sourceBuffer.width / 10,
                                                       height: sourceBuffer.height / 10),
                                           pixelFormat: vImage.Interleaved8x4.self)

let time = ContinuousClock().measure {
    sourceBuffer.scale(destination: destinationBuffer)
}
```

You can use [`ContinuousClock`](https://developer.apple.com/documentation/Swift/ContinuousClock) to measure the execution time.

##### Convert an Interleaved Source Buffer to Planar Buffers

The pixel buffer [`init(cgImage:cgImageFormat:pixelFormat:)`](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md) initializer and the vImage buffer [`vImageBuffer_InitWithCGImage(_:_:_:_:_:)`](vimagebuffer_initwithcgimage(_:_:_:_:_:).md) function both populate a buffer based on the properties of a [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure.

For example, the following code creates an interleaved 3-channel, 8-bit-per-channel [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structure from the source Core Graphics image. The code calls [`deinterleave(destination:)`](vimage/pixelbuffer/deinterleave(destination:)-hrhz.md) to deinterleave the image data and populate the individual red, green, and blue planar pixel buffers.

```swift
var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue:
                                CGImageAlphaInfo.none.rawValue))!

let sourceBuffer = try vImage.PixelBuffer(cgImage: sourceImage,
                                          cgImageFormat: &cgImageFormat,
                                          pixelFormat: vImage.Interleaved8x3.self)
let sourceRedBuffer = vImage.PixelBuffer(size: sourceBuffer.size,
                                         pixelFormat: vImage.Planar8.self)
let sourceGreenBuffer = vImage.PixelBuffer(size: sourceBuffer.size,
                                           pixelFormat: vImage.Planar8.self)
let sourceBlueBuffer = vImage.PixelBuffer(size: sourceBuffer.size,
                                          pixelFormat: vImage.Planar8.self)

sourceBuffer.deinterleave(planarDestinationBuffers: [sourceRedBuffer,
                                                     sourceGreenBuffer,
                                                     sourceBlueBuffer])
```

##### Initialize the Destination Buffers

Create an interleaved 3-channel, 8-bit-per-channel destination buffer and three planar destination buffers:

```swift
let destinationBuffer = vImage.PixelBuffer(size: .init(width: sourceBuffer.width / 10,
                                                       height: sourceBuffer.height / 10),
                                           pixelFormat: vImage.Interleaved8x3.self)

let destinationRedBuffer = vImage.PixelBuffer(size: destinationBuffer.size,
                                              pixelFormat: vImage.Planar8.self)
let destinationGreenBuffer = vImage.PixelBuffer(size: destinationBuffer.size,
                                                pixelFormat: vImage.Planar8.self)
let destinationBlueBuffer = vImage.PixelBuffer(size: destinationBuffer.size,
                                               pixelFormat: vImage.Planar8.self)
```

##### Apply the Scale Operation to the Planar Buffers

Use the `withTaskGroup(of:returning:body:)` function to start a new scope that contains the three planar scale operations. Note that the 8-bit planar [`scale(destination:)`](vimage/pixelbuffer/scale(destination:)-5euvc.md) function calls [`vImageScale_Planar8(_:_:_:_:)`](vimagescale_planar8(_:_:_:_:).md).

In the code below, the [`interleave(destination:)`](vimage/pixelbuffer/interleave(destination:)-46cgi.md) function interleaves the three planar buffers and populates the interleaved destination buffer with the scaled image:

```swift
let time = await ContinuousClock().measure {
    
    await withTaskGroup(of: Void.self) { group in
        
        group.addTask(priority: .userInitiated) {
            sourceRedBuffer.scale(destination: destinationRedBuffer)
        }
        
        group.addTask(priority: .userInitiated) {
            sourceGreenBuffer.scale(destination: destinationGreenBuffer)
        }
        
        group.addTask(priority: .userInitiated) {
            sourceBlueBuffer.scale(destination: destinationBlueBuffer)
        }
    }
    
    destinationBuffer.interleave(planarSourceBuffers: [destinationRedBuffer,
                                                       destinationGreenBuffer,
                                                       destinationBlueBuffer])
}
```

The following code calls [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) to create a Core Graphics image from the result of the scale operation:

```swift
let scaledImage = destinationBuffer.makeCGImage(cgImageFormat: cgImageFormat)
```

## See Also

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
  Pass image data between Core Graphics and vImage to create and manipulate images.
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
  Initialize vImage buffers from Core Graphics images.
- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)
  Create displayable representations of vImage buffers.
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
  Resize an image with vImage.
- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
  Combine two images by using blend modes to create a single output.
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
  Limit the effect of vImage operations to rectangular regions of interest.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/optimizing-image-processing-performance)*