# AttachableAsImage

**Framework**: Swift Testing  
**Kind**: protocol  
**Role**: Protocol

A protocol describing images that can be converted to instances of [Attachment](./attachment.md).

**Availability**:
- Swift 6.3+
- Xcode 26.4+

## Declaration

```swift
protocol AttachableAsImage
```

## Overview

Instances of types conforming to this protocol do not themselves conform to [Attachable](./attachable.md). Instead, the testing library provides additional initializers on [Attachment](./attachment.md) that take instances of such types and handle converting them to image data when needed.

You do not generally need to add your own conformances to this protocol. For a list of types that automatically conform to this protocol, see [Attach images](./attachments.md#Attach-images).

## Topics

### Instance Methods
- [func withUnsafeBytes<R>(as: AttachableImageFormat, (UnsafeRawBufferPointer) throws -> R) throws -> R](./attachableasimage/withunsafebytes%28as,_%29.md)
  Encode a representation of this image in a given image format.

## See Also

### Attaching images to tests
- [struct AttachableImageFormat](./attachableimageformat.md)
  A type describing image formats supported by the system that can be used when attaching an image to a test.
- [init<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](./attachment/init%28_,named,as,sourcelocation%29.md)
  Initialize an instance of this type that encloses the given image.
- [static func record<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](./attachment/record%28_,named,as,sourcelocation%29.md)
  Attach an image to the current test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableasimage)*