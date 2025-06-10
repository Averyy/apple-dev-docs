# createCGImage(format:flags:)

**Framework**: Accelerate  
**Kind**: method

Creates a Core Graphics image from the vImage buffer.

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
func createCGImage(format: vImage_CGImageFormat, flags options: vImage.Options = .noFlags) throws -> CGImage
```

## Mentions

- [Creating a Core Graphics Image from a vImage Buffer](creating-a-core-graphics-image-from-a-vimage-buffer.md)

#### Return Value

A Core Graphics image that represents the contents of the vImage buffer.

## Parameters

- `format`: The desired format.
- `options`: The options to use when performing the operation.

## See Also

- [init(cgImage: CGImage, flags: vImage.Options) throws](vimage_buffer/init(cgimage:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image.
- [init(cgImage: CGImage, format: vImage_CGImageFormat, flags: vImage.Options) throws](vimage_buffer/init(cgimage:format:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image using the supplied image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/createcgimage(format:flags:))*