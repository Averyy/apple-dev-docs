# Converting bitmap data between Core Graphics images and vImage buffers

**Framework**: Accelerate

Pass image data between Core Graphics and vImage to create and manipulate images.

#### Overview

When you work with bitmap images, you typically work with Core Graphics [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instances. The vImage library provides functionality that allows you to work with Core Graphics bitmap images. Typically, you convert a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance to a vImage buffer, apply operations to the vImage buffer, and convert the transformed data to a new [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance.

Conversions between Core Graphics-backed images and vImage buffers require a [`vImage_CGImageFormat`](vimage_cgimageformat.md) format structure. The format describes properties such as the color space, the number of channels and how they’re ordered, and the size, in bits, of the color channels.

##### Initialize an 8 Bit Core Graphics Image Format From Hard Coded Values

Create a [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure with hard-coded values when you need to perform operations on image data with properties that your app defines at compile time. For example, the code below initializes an 8-bit-per-channel ARGB format that’s suitable for working with [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structures with a [`vImage.Interleaved8x4`](vimage/interleaved8x4.md) format.

```swift
var format = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 4,
    colorSpace: CGColorSpace(name: CGColorSpace.displayP3)!,
    bitmapInfo: .init(rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue))!
```

The [`init(cgImage:cgImageFormat:pixelFormat:)`](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md) initializer creates a pixel buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance and converts the source image data to the format that the [`vImage_CGImageFormat`](vimage_cgimageformat.md) describes. If you’re working with [`vImage_Buffer`](vimage_buffer.md) structures, the [`vImageBuffer_InitWithCGImage(_:_:_:_:_:)`](vimagebuffer_initwithcgimage(_:_:_:_:_:).md) function performs the same conversion and creates a buffer that’s suitable for working with ARGB8888 operations, such as [`vImageConvolve_ARGB8888(_:_:_:_:_:_:_:_:_:_:_:)`](vimageconvolve_argb8888(_:_:_:_:_:_:_:_:_:_:_:).md).

The code below creates a buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance named `cgImage` and prints the values of the first two pixels. The opaque alpha values (`255`) are the first value in each pixel as [`CGImageAlphaInfo.noneSkipFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/noneSkipFirst) defines.

```swift
let buf = try vImage.PixelBuffer(
    cgImage: cgImage,
    cgImageFormat: &format,
    pixelFormat: vImage.Interleaved8x4.self)

// Prints:
// "[255, 115, 136, 165,  255, 115, 136, 165]"
//    A    R    G    B  |  A    R    G    B
print(buf.array[0 ..< 2 * format.componentCount])
```

For all the examples in this article, pass the [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure to the [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) method to generate an output image.

```swift
let result = buf.makeCGImage(cgImageFormat: format)
```

On return, `result` is a four-channel 8-bit-per-channel image with [`CGImageAlphaInfo.noneSkipLast`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/noneSkipLast) alpha ordering.

![A color photograph of a flower.](https://docs-assets.developer.apple.com/published/e1dcfd821ae7c4dcc337fc0723d06f84/media-4265606%402x.png)

##### Initialize a 32 Bit Core Graphics Image Format From Hard Coded Values

You can use the [`init(cgImage:cgImageFormat:pixelFormat:)`](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md) initializer to convert an image’s color model and bit depth. For example, you can specify a grayscale 32-bit format such as the example below:

```swift
let bitmapInfo = CGBitmapInfo(
    rawValue: kCGBitmapByteOrder32Host.rawValue |
    CGBitmapInfo.floatComponents.rawValue |
    CGImageAlphaInfo.none.rawValue)

var format = vImage_CGImageFormat(bitsPerComponent: 32,
                                  bitsPerPixel: 32,
                                  colorSpace: CGColorSpaceCreateDeviceGray(),
                                  bitmapInfo: bitmapInfo)!
```

In this case, the initializer uses the Rec. 601 luma coefficients to convert the RGB pixel values (`115, 136, 165`) to a single grayscale pixel.

```swift
let buf = try vImage.PixelBuffer(cgImage: cgImage,
                                 cgImageFormat: &format,
                                 pixelFormat: vImage.PlanarF.self)

// Prints:
// "[133, 133]"  // (0.299 * 115 + 0.587 * 136 + 0.114 * 165) = 133
//    Y    Y
print(buf.array[0 ..< 2 * format.componentCount].map {
    Pixel_8($0 * 255 )
})
```

As above, pass the 32-bit format to [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) to create a single-channel 32-bit-per-channel image with no alpha information.

```swift
let result = buf.makeCGImage(cgImageFormat: format)
```

On return, `result` contains a grayscale version of the original image.

![A grayscale photograph of a flower.](https://docs-assets.developer.apple.com/published/ae5f5747dea959308768dc11cf3050ff/media-4265605%402x.png)

##### Initialize a Core Graphics Image Format From a Core Graphics Image

The [`init(cgImage:)`](vimage_cgimageformat/init(cgimage:).md) initializer creates a new [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure that describes a Core Graphics image’s properties.

```swift
guard var format = vImage_CGImageFormat(cgImage: cgImage) else {
    NSLog("Unable to derive format from image.")
    return
}

print(format.bitsPerComponent)                      // 8
print(format.componentCount)                        // 4
print(format.colorSpace.takeRetainedValue().name!)  // kCGColorSpaceDisplayP3
print (format.bitmapInfo)                           // noneSkipLast
```

In this example, the image’s inherent channel ordering is [`CGImageAlphaInfo.noneSkipLast`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/noneSkipLast). The code below prints the first two pixels and shows that the opaque alpha values (`255`) are the last two values in each pixel:

```swift
let buf = try vImage.PixelBuffer(cgImage: cgImage,
                                 cgImageFormat: &format,
                                 pixelFormat: vImage.Interleaved8x4.self)

// Prints:
// "[115, 136, 165, 255,  115, 136, 165, 255]"
//    R    G    B    A  |  R    G    B    A
print(buf.array[0 ..< 2 * format.componentCount])
```

##### Initialize a Core Graphics Image Format From an Image During Pixel Buffer Initialization

You can pass an empty [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure to the [`init(cgImage:cgImageFormat:pixelFormat:)`](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md) initializer to instruct the initializer to populate the format with an image’s properties. In this case, the initializer returns `nil` if the image’s and the pixel buffer’s bit depths aren’t equal.

```swift
guard cgImage.bitsPerComponent == 8,
      cgImage.bitsPerPixel == 8 * 4 else {
    fatalError("Unsupported `bitsPerComponent` and `bitsPerPixel`.")
}

var format = vImage_CGImageFormat()

let buf = try vImage.PixelBuffer(cgImage: cgImage,
                                 cgImageFormat: &format,
                                 pixelFormat: vImage.Interleaved8x4.self)
```

On return, the mutable format variable contains the image properties.

```swift
print(format.colorSpace.takeRetainedValue().name!)  // kCGColorSpaceDisplayP3
print(format.bitmapInfo)                            // noneSkipLast

// Prints:
// "[115, 136, 165, 255,  115, 136, 165, 255]"
//    R    G    B    A  |  R    G    B    A
print(buf.array[0 ..< 2 * format.componentCount])
```

## See Also

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
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
  Improve your app’s performance by converting image buffer formats from interleaved to planar.
- [vImage](vimage-library.md)
  Manipulate large images using the CPU’s vector processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/converting-bitmap-data-between-core-graphics-images-and-vimage-buffers)*