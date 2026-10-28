# AttachableImageFormat

**Framework**: Swift Testing  
**Kind**: struct  
**Role**: Structure

A type describing image formats supported by the system that can be used when attaching an image to a test.

**Availability**:
- Swift 6.3+
- Xcode 26.4+

## Declaration

```swift
struct AttachableImageFormat
```

## Overview

When you attach an image to a test, you can pass an instance of this type to [`record(_:named:as:sourceLocation:)`](./attachment/record%28_,named,as,sourcelocation%29.md) so that the testing library knows the image format you’d like to use. If you don’t pass an instance of this type, the testing library infers which format to use based on the attachment’s preferred name.

The testing library always supports the PNG and JPEG image formats. The set of additional supported image formats is platform-specific:

- On Apple platforms, you can use [CGImageDestinationCopyTypeIdentifiers()](../ImageIO/cgimagedestinationcopytypeidentifiers%28%29.md) from the [Image I/O framework](../ImageIO/ImageIO.md) to determine which formats are supported.
- On Windows, you can use [IWICImagingFactory.CreateComponentEnumerator()](https://learn.microsoft.com/en-us/windows/win32/api/wincodec/nf-wincodec-iwicimagingfactory-createcomponentenumerator) to enumerate the available image encoders.

## Topics

### Initializers
- [init(contentType: UTType, encodingQuality: Float)](./attachableimageformat/init%28contenttype,encodingquality%29.md)
  Initialize an instance of this type with the given content type and encoding quality.
- [init?(pathExtension: String, encodingQuality: Float)](./attachableimageformat/init%28pathextension,encodingquality%29.md)
  Construct an instance of this type with the given path extension and encoding quality.
### Instance Properties
- [var contentType: UTType](./attachableimageformat/contenttype.md)
  The content type corresponding to this image format.
- [var encodingQuality: Float](./attachableimageformat/encodingquality.md)
  The encoding quality to use for this image format.
### Type Properties
- [static var jpeg: AttachableImageFormat](./attachableimageformat/jpeg.md)
  The JPEG image format with maximum encoding quality.
- [static var png: AttachableImageFormat](./attachableimageformat/png.md)
  The PNG image format.
### Type Methods
- [static func jpeg(withEncodingQuality: Float) -> AttachableImageFormat](./attachableimageformat/jpeg%28withencodingquality%29.md)
  The JPEG image format.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./attachableimageformat/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./attachableimageformat/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Attaching images to tests
- [protocol AttachableAsImage](./attachableasimage.md)
  A protocol describing images that can be converted to instances of [Attachment](./attachment.md).
- [init<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](./attachment/init%28_,named,as,sourcelocation%29.md)
  Initialize an instance of this type that encloses the given image.
- [static func record<T>(T, named: String?, as: AttachableImageFormat?, sourceLocation: SourceLocation)](./attachment/record%28_,named,as,sourcelocation%29.md)
  Attach an image to the current test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableimageformat)*