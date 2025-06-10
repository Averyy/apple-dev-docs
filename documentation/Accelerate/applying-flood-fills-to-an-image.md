# Applying flood fills to an image

**Framework**: Accelerate

Fill consistently colored connected parts of an image with a new color.

#### Overview

The vImage library provides a set of functions that allow you to flood fill areas of an image with a new color. The following image demonstrates how the flood-fill operation can colorize a hand-drawn line illustration:

![A flow diagram that depicts colorization of a hand-drawn illustration. On the left is a grayscale line drawing of a mountainous landscape, and on the right is the same drawing with each segment filled in with a solid color.](https://docs-assets.developer.apple.com/published/f942d57c950e905b5d515ec5cbbb8df6/media-4098131%402x.png)

The flood-fill functions fill areas with identical pixel values. The process of applying lossy compression, such as when generating JPG images, may subtly change pixel values. Use losslessly compressed or uncompressed images, such as PNGs, to achieve the best flood-fill results.

##### Create the Planar Vimage Buffer That Represents the Source Image

Create a 32-bit-per-pixel, planar image to store the image of the line drawing.

```swift
var cgImageFormatPlanarF = vImage_CGImageFormat(
    bitsPerComponent: 32,
    bitsPerPixel: 32,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(
        rawValue: kCGBitmapByteOrder32Host.rawValue |
        CGBitmapInfo.floatComponents.rawValue |
        CGImageAlphaInfo.none.rawValue),
    renderingIntent: .defaultIntent)!

let image: CGImage = [ ... ]

let bufferPlanarF = try! vImage.PixelBuffer<vImage.PlanarF>(
    cgImage: image,
    cgImageFormat: &cgImageFormatPlanarF)

```

Call the [`colorThreshold(_:destination:)`](vimage/pixelbuffer/colorthreshold(_:destination:).md) function to binarize the image, that is, reduce it to only black and white colors with no midtones. Pass a threshold value of `0.5` to convert all pixel values below `0.5` to `0.0`, and other pixel values to `1.0`.

```swift
bufferPlanarF.colorThreshold(
    0.5,
    destination: bufferPlanarF)
```

##### Create the Interleaved Vimage Buffer That Represents the Destination Image

Use the 32-bit planar buffer to create a four-channel, 8-bit-per-pixel buffer.

```swift
let bufferRGB8 = vImage.PixelBuffer<vImage.Interleaved8x4>(
    planarBuffers: [bufferPlanarF, bufferPlanarF, bufferPlanarF, bufferPlanarF])
```

##### Apply the Flood Fill Operation

The source image is 1024 pixels wide and 1585 pixels high. The following image shows the coordinates of the six seed pixels:

![A diagram of a grayscale line drawing of a mountainous landscape. An indicator at the top shows the width as 1024, and an indicator on the left shows the height as 1585. On the right are six callouts that are stacked vertically. Each callout specifies the x and y positions of the seed pixel and the corresponding red, green, and blue values for the color fill.](https://docs-assets.developer.apple.com/published/5a53f4d909cd849b96e3622b746b156d/media-4110108%402x.png)

Call [`vImageFloodFill_ARGB8888(_:_:_:_:_:_:_:)`](vimagefloodfill_argb8888(_:_:_:_:_:_:_:).md) to apply different colors to different parts of the line drawing. Note that the vImage flood-fill functions only work in place. That is, a single vImage buffer is the source and the destination for the flood-fill operation.

```swift
bufferRGB8.withUnsafePointerToVImageBuffer { src in
    let alpha = UInt8(255)
    
    var newARGB: [UInt8] = [alpha, 68, 41, 11]
    let seedX: vImagePixelCount = 600
    var seedY: vImagePixelCount = 10
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)
    
    newARGB = [alpha, 160, 198, 212]
    seedY = 200
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)

    newARGB = [alpha, 147, 163, 169]
    seedY = 450
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)

    newARGB = [alpha, 90, 101, 103]
    seedY = 700
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)

    newARGB = [alpha, 54, 62, 65]
    seedY = 900
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)

    newARGB = [alpha, 51, 81, 28]
    seedY = 1300
    vImageFloodFill_ARGB8888(src, nil,
                             seedX, seedY,
                             &newARGB, 8, 0)
}

```

##### Create a Core Graphics Image of the Result

Create a [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure that describes the four-channel, 8-bit-per-channel output image.

```swift
let cgImageFormatRGB8 = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 4,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(
        rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue),
    renderingIntent: .defaultIntent)!

```

Finally, call [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) to generate the image.

```swift
let result = bufferRGB8.makeCGImage(cgImageFormat: cgImageFormatRGB8)
```

## See Also

- [func vImageFloodFill_Planar8(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, Pixel_8, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_planar8(_:_:_:_:_:_:_:).md)
  Applies a flood-fill operation to an 8-bit planar image.
- [func vImageFloodFill_Planar16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, Pixel_16U, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_planar16u(_:_:_:_:_:_:_:).md)
  Applies a flood fill-operation to an unsigned 16-bit planar image.
- [func vImageFloodFill_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt8>!, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_argb8888(_:_:_:_:_:_:_:).md)
  Applies a flood-fill operation to an 8-bit-per-channel, four-channel interleaved image.
- [func vImageFloodFill_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImagePixelCount, vImagePixelCount, UnsafeMutablePointer<UInt16>!, Int32, vImage_Flags) -> vImage_Error](vimagefloodfill_argb16u(_:_:_:_:_:_:_:).md)
  Applies a flood-fill operation to an unsigned 16-bit-per-channel, four-channel interleaved image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-flood-fills-to-an-image)*