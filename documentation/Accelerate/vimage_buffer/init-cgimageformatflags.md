# init(cgImage:format:flags:)

**Framework**: Accelerate  
**Kind**: init

Creates a new buffer with the contents of a Core Graphics image using the supplied image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init(cgImage: CGImage, format: vImage_CGImageFormat, flags options: vImage.Options = .noFlags) throws
```

## Mentions

- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)

#### Discussion

This function converts the source Core Graphics image that the `cgImage` parameter specifies to the format that the `format` parameter describes.

For example, the following code converts a color image to grayscale and initializes the vImage buffer with the planar monochrome image data:

```swift
let format = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8,
    colorSpace: CGColorSpaceCreateDeviceGray(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

// `cgImage` is a color image.
let buffer = try vImage_Buffer(cgImage: cgImage,
                               format: format)
```

## Parameters

- `cgImage`: The source image.
- `format`: The desired image format.
- `options`: The options to use when performing the operation.

## See Also

- [init(cgImage: CGImage, flags: vImage.Options) throws](vimage_buffer/init(cgimage:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image.
- [func createCGImage(format: vImage_CGImageFormat, flags: vImage.Options) throws -> CGImage](vimage_buffer/createcgimage(format:flags:).md)
  Creates a Core Graphics image from the vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(cgimage:format:flags:))*