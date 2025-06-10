# init(cgImage:flags:)

**Framework**: Accelerate  
**Kind**: init

Creates a new buffer with the contents of a Core Graphics image.

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
init(cgImage: CGImage, flags options: vImage.Options = .noFlags) throws
```

#### Discussion

This function initializes a vImage buffer using the format of the Core Graphics image.

## Parameters

- `cgImage`: The source image.
- `options`: The options to use when performing the operation.

## See Also

- [init(cgImage: CGImage, format: vImage_CGImageFormat, flags: vImage.Options) throws](vimage_buffer/init(cgimage:format:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image using the supplied image format.
- [func createCGImage(format: vImage_CGImageFormat, flags: vImage.Options) throws -> CGImage](vimage_buffer/createcgimage(format:flags:).md)
  Creates a Core Graphics image from the vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(cgimage:flags:))*