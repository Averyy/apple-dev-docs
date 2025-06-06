# QLThumbnailReply

**Framework**: Quick Look Thumbnailing  
**Kind**: class

The object that provides a thumbnail for a custom file type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class QLThumbnailReply
```

## Mentions

- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)

## Topics

### Creating a Thumbnail
- [convenience init(contextSize: CGSize, currentContextDrawing: () -> Bool)](qlthumbnailreply/init(contextsize:currentcontextdrawing:).md)
  Creates a new thumbnail for a custom file type in the current context.
- [convenience init(contextSize: CGSize, drawing: (CGContext) -> Bool)](qlthumbnailreply/init(contextsize:drawing:).md)
  Creates a new thumbnail for a custom file type in the given context.
- [convenience init(imageFileURL: URL)](qlthumbnailreply/init(imagefileurl:).md)
  Creates a new thumbnail for a custom file type using a file at the given URL.
### Customizing a Thumbnail Reply
- [var extensionBadge: String](qlthumbnailreply/extensionbadge.md)
  A short string that identifies the file type that the system uses as a badge when producing an icon thumbnail.

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
- [class QLFileThumbnailRequest](qlfilethumbnailrequest.md)
  A request to generate a thumbnail for a custom file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailreply)*