# Transcript.ImageAttachment

**Framework**: Foundation Models  
**Kind**: struct

An image attachment in a transcript entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ImageAttachment
```

## Topics

### Creating an image attachment
- [init(_:orientation:)](transcript/imageattachment/init(_:orientation:).md)
  Creates an image attachment from a Core Graphics image.
- [init(imageURL: URL, orientation: CGImagePropertyOrientation?)](transcript/imageattachment/init(imageurl:orientation:).md)
  Creates an image attachment from a file URL pointing to an image.
### Inspecting an image attachment
- [var cgImage: CGImage](transcript/imageattachment/cgimage.md)
  The image as a Core Graphics image.
- [var ciImage: CIImage](transcript/imageattachment/ciimage.md)
- [var orientation: CGImagePropertyOrientation](transcript/imageattachment/orientation.md)
  The display orientation of the image.
- [var url: URL?](transcript/imageattachment/url.md)
  The URL of the original image asset, if the attachment was created from a URL.
### Getting the pixel buffer
- [func pixelBuffer(resolution: CGSize?, pixelFormat: OSType?) throws -> CVReadOnlyPixelBuffer](transcript/imageattachment/pixelbuffer(resolution:pixelformat:).md)
  Returns the image as a pixel buffer, optionally resampled to a given resolution and pixel format.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transcript.Attachment](transcript/attachment.md)
  The types of attached content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/imageattachment)*