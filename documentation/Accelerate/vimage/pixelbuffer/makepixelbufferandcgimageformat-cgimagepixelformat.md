# makePixelBufferAndCGImageFormat(cgImage:pixelFormat:)

**Framework**: Accelerate  
**Kind**: method

Returns a new pixel buffer and Core Graphics image format structure from a Core Graphics image.

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
static func makePixelBufferAndCGImageFormat(cgImage: CGImage, pixelFormat: Format.Type = Format.self) throws -> (pixelBuffer: vImage.PixelBuffer<Format>, cgImageFormat: vImage_CGImageFormat)
```

#### Return Value

A new pixel buffer of type [`vImage.DynamicPixelFormat`](vimage/dynamicpixelformat.md) and a [`vImage_CGImageFormat`](vimage_cgimageformat.md) that describes the ordering and number of the color channels, the size and type of the data in the color channels, and whether or not the data is premultiplied by alpha.

#### Discussion

Use this function where you know the bits per component and bits per pixel of the [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance. These must match those of the buffer’s `pixelFormat`, otherwise this function returns `nil`.

## Parameters

- `cgImage`: The source Core Graphics image.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

- [static func makeDynamicPixelBufferAndCGImageFormat(cgImage: CGImage) throws -> (pixelBuffer: vImage.PixelBuffer<vImage.DynamicPixelFormat>, cgImageFormat: vImage_CGImageFormat)](vimage/pixelbuffer/makedynamicpixelbufferandcgimageformat(cgimage:).md)
  Returns a new dynamic pixel format pixel buffer and Core Graphics image format structure from a Core Graphics image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/makepixelbufferandcgimageformat(cgimage:pixelformat:))*