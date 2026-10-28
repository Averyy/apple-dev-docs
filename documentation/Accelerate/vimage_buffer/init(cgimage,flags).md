# init(cgImage:flags:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new buffer with the contents of a Core Graphics image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
init(cgImage: CGImage, flags options: vImage.Options = .noFlags) throws
```

## Discussion

This function initializes a vImage buffer using the format of the Core Graphics image.

## Parameters

- `cgImage`: The source image.
- `options`: The options to use when performing the operation.

## See Also

### Consuming and producing Core Graphics images
- [init(cgImage: CGImage, format: vImage_CGImageFormat, flags: vImage.Options) throws](./init%28cgimage,format,flags%29.md)
  Creates a new buffer with the contents of a Core Graphics image using the supplied image format.
- [func createCGImage(format: vImage_CGImageFormat, flags: vImage.Options) throws -> CGImage](./createcgimage%28format,flags%29.md)
  Creates a Core Graphics image from the vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/init(cgimage:flags:))*