# QLThumbnailProvider

**Framework**: Quick Look Thumbnailing  
**Kind**: class

An abstract base class for creating thumbnails of custom file types.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class QLThumbnailProvider
```

## Mentions

- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)

## Topics

### Essentials
- [func provideThumbnail(for: QLFileThumbnailRequest, (QLThumbnailReply?, (any Error)?) -> Void)](qlthumbnailprovider/providethumbnail(for:_:).md)
  Creates a thumbnail of a custom file type for a specific request.

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
- [class QLFileThumbnailRequest](qlfilethumbnailrequest.md)
  A request to generate a thumbnail for a custom file type.
- [class QLThumbnailReply](qlthumbnailreply.md)
  The object that provides a thumbnail for a custom file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailprovider)*