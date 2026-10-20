# QLThumbnailRepresentation.RepresentationType

**Framework**: Quick Look Thumbnailing  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum QLThumbnailRepresentationType : NSInteger;
```

## Mentions

- [Providing Thumbnails of Your Custom File Types](../providing-thumbnails-of-your-custom-file-types.md)

## Topics

### Enumeration Cases
- [QLThumbnailRepresentation.RepresentationType.icon](./representationtype/icon.md)
  A file icon representation of an image.
- [QLThumbnailRepresentation.RepresentationType.lowQualityThumbnail](./representationtype/lowqualitythumbnail.md)
  A cached thumbnail representation of an image.
- [QLThumbnailRepresentation.RepresentationType.thumbnail](./representationtype/thumbnail.md)
  A thumbnail representation of an image.
### Initializers
- [init?(rawValue: Int)](./representationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Thumbnail Images
- [var cgImage: CGImage](./cgimage.md)
  A thumbnail in the form of a Core Graphics image object.
- [var nsImage: NSImage](./nsimage.md)
  A thumbnail in the form of an AppKit image object.
- [var uiImage: UIImage](./uiimage.md)
  A thumbnail in the form of a UIKit image object.
- [var type: QLThumbnailRepresentation.RepresentationType](./type.md)
  The type of thumbnail.
- [var contentRect: CGRect](./contentrect.md)
  The rectangle within the thumbnail image of the document that represents its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation/representationtype)*