# Transcript.ImageAttachment

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

An image attachment in a transcript entry.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ImageAttachment
```

## Topics

### Creating an image attachment
- [init(_:orientation:)](./imageattachment/init%28_,orientation%29.md)
  Creates an image attachment from a Core Graphics image.
- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](./imageattachment/init%28imageurl,orientation%29.md)
  Creates an image attachment from a file URL pointing to an image.
### Inspecting an image attachment
- [var cgImage: CGImage](./imageattachment/cgimage.md)
  The image as a Core Graphics image.
- [var ciImage: CIImage](./imageattachment/ciimage.md)
  The image as a Core Image image.
- [var orientation: CGImagePropertyOrientation](./imageattachment/orientation.md)
  The display orientation of the image.
- [var url: URL?](./imageattachment/url.md)
  The URL of the original image asset, if the attachment was created from a URL.
### Getting the pixel buffer
- [func pixelBuffer(resolution: CGSize?, pixelFormat: OSType?) throws -> CVReadOnlyPixelBuffer](./imageattachment/pixelbuffer%28resolution,pixelformat%29.md)
  Returns the image as a pixel buffer, optionally resampled to a given resolution and pixel format.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Attachments
- [Transcript.Attachment](./attachment.md)
  The types of attached content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/imageattachment)*