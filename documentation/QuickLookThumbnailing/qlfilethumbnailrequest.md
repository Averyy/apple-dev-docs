# QLFileThumbnailRequest

**Framework**: Quick Look Thumbnailing  
**Kind**: class

A request to generate a thumbnail for a custom file type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class QLFileThumbnailRequest
```

## Topics

### Describing the Requested Thumbnail
- [var maximumSize: CGSize](qlfilethumbnailrequest/maximumsize.md)
  The maximum accepted size of a thumbnail.
- [var minimumSize: CGSize](qlfilethumbnailrequest/minimumsize.md)
  The minimum accepted size of a thumbnail.
- [var scale: CGFloat](qlfilethumbnailrequest/scale.md)
  The scale of the requested thumbnail.
- [var fileURL: URL](qlfilethumbnailrequest/fileurl.md)
  The URL of the image file to use for the thumbnail.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)
  Implement a Thumbnail Extension to allow the operating system and other apps to display thumbnails of your custom files.
- [class QLThumbnailProvider](qlthumbnailprovider.md)
  An abstract base class for creating thumbnails of custom file types.
- [class QLThumbnailReply](qlthumbnailreply.md)
  The object that provides a thumbnail for a custom file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlfilethumbnailrequest)*