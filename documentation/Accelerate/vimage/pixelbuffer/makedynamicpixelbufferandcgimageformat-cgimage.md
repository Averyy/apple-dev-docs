# makeDynamicPixelBufferAndCGImageFormat(cgImage:)

**Framework**: Accelerate  
**Kind**: method

Returns a new dynamic pixel format pixel buffer and Core Graphics image format structure from a Core Graphics image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func makeDynamicPixelBufferAndCGImageFormat(cgImage: CGImage) throws -> (pixelBuffer: vImage.PixelBuffer<vImage.DynamicPixelFormat>, cgImageFormat: vImage_CGImageFormat)
```

#### Return Value

A new pixel buffer of type [`vImage.DynamicPixelFormat`](vimage/dynamicpixelformat.md) and a [`vImage_CGImageFormat`](vimage_cgimageformat.md) that describes the ordering and number of the color channels, the size and type of the data in the color channels, and whether or not the data is premultiplied by alpha.

#### Discussion

Use this function to create an image format and pixel buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance. The pixel buffer that this function returns has a pixel format that’s unknown at compile time.

Note that you can call [`init(cgImage:cgImageFormat:pixelFormat:)`](vimage/pixelbuffer/init(cgimage:cgimageformat:pixelformat:).md) to create a statically typed pixel buffer from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance. However, this function allows you to create your own any-to-any converter for more control over the conversion process to a statically typed buffer.

For example, the following code creates a dynamically typed pixel buffer and [`vImage_CGImageFormat`](vimage_cgimageformat.md) from a source image. Use the returned [`vImage_CGImageFormat`](vimage_cgimageformat.md) as the source format on an any-to-any converter. For example:

```swift
let srcImage = imageLiteral(resourceName: " ... ").cgImage(
    forProposedRect: nil,
    context: nil,
    hints: nil)!

let source = try vImage.PixelBuffer.makeDynamicPixelBufferAndCGImageFormat(
    cgImage: srcImage)

let destFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let destBuffer = vImage.PixelBuffer(size: source.pixelBuffer.size,
                                    pixelFormat: vImage.Planar8.self)

let converter = try vImageConverter.make(sourceFormat: source.cgImageFormat,
                                         destinationFormat: destFormat)

try converter.convert(from: source.pixelBuffer, to: destBuffer)
```

On return, `destBuffer` contains an 8-bit, grayscale representation of the original image.

## Parameters

- `cgImage`: The source Core Graphics image.

## See Also

- [static func makePixelBufferAndCGImageFormat(cgImage: CGImage, pixelFormat: Format.Type) throws -> (pixelBuffer: vImage.PixelBuffer<Format>, cgImageFormat: vImage_CGImageFormat)](vimage/pixelbuffer/makepixelbufferandcgimageformat(cgimage:pixelformat:).md)
  Returns a new pixel buffer and Core Graphics image format structure from a Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/makedynamicpixelbufferandcgimageformat(cgimage:))*