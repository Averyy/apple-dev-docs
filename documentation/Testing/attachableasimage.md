# AttachableAsImage

**Framework**: Swift Testing  
**Kind**: protocol

A protocol describing images that can be converted to instances of [`Attachment`](https://developer.apple.comhttps://developer.apple.com/documentation/testing/attachment).

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
protocol AttachableAsImage
```

#### Overview

Instances of types conforming to this protocol do not themselves conform to [`Attachable`](https://developer.apple.comhttps://developer.apple.com/documentation/testing/attachable). Instead, the testing library provides additional initializers on [`Attachment`](https://developer.apple.comhttps://developer.apple.com/documentation/testing/attachment) that take instances of such types and handle converting them to image data when needed.

You do not generally need to add your own conformances to this protocol. For a list of types that automatically conform to this protocol, see [`Attach images`](attachments#Attach-images.md).

## Topics

### Instance Methods
- [func withUnsafeBytes<R>(as: AttachableImageFormat, (UnsafeRawBufferPointer) throws -> R) throws -> R](attachableasimage/withunsafebytes(as:_:).md)
  Encode a representation of this image in a given image format.

## See Also

- [struct AttachableImageFormat](attachableimageformat.md)
  A type describing image formats supported by the system that can be used when attaching an image to a test.
- [init<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](attachment/init(_:named:as:sourcelocation:).md)
  Initialize an instance of this type that encloses the given image.
- [static func record<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](attachment/record(_:named:as:sourcelocation:).md)
  Attach an image to the current test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableasimage)*