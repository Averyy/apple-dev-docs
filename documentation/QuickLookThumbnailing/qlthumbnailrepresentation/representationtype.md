# QLThumbnailRepresentation.RepresentationType

**Framework**: Quick Look Thumbnailing  
**Kind**: enum

The different types of thumbnails that you can create.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum RepresentationType
```

## Mentions

- [Providing Thumbnails of Your Custom File Types](providing-thumbnails-of-your-custom-file-types.md)

## Topics

### Enumeration Cases
- [QLThumbnailRepresentation.RepresentationType.icon](qlthumbnailrepresentation/representationtype/icon.md)
  A file icon representation of an image.
- [QLThumbnailRepresentation.RepresentationType.lowQualityThumbnail](qlthumbnailrepresentation/representationtype/lowqualitythumbnail.md)
  A cached thumbnail representation of an image.
- [QLThumbnailRepresentation.RepresentationType.thumbnail](qlthumbnailrepresentation/representationtype/thumbnail.md)
  A thumbnail representation of an image.
### Initializers
- [init?(rawValue: Int)](qlthumbnailrepresentation/representationtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var cgImage: CGImage](qlthumbnailrepresentation/cgimage.md)
  A thumbnail in the form of a Core Graphics image object.
- [var nsImage: NSImage](qlthumbnailrepresentation/nsimage.md)
  A thumbnail in the form of an AppKit image object.
- [var uiImage: UIImage](qlthumbnailrepresentation/uiimage.md)
  A thumbnail in the form of a UIKit image object.
- [var type: QLThumbnailRepresentation.RepresentationType](qlthumbnailrepresentation/type.md)
  The type of thumbnail.
- [var contentRect: CGRect](qlthumbnailrepresentation/contentrect.md)
  The rectangle within the thumbnail image of the document that represents its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation/representationtype)*