# QLThumbnailGenerator.Request.RepresentationTypes

**Framework**: Quick Look Thumbnailing  
**Kind**: struct

The various types of thumbnails that you can request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct RepresentationTypes
```

#### Overview

Thumbnails come in one of three different types:

To request all thumbnail representations, use [`all`](qlthumbnailgenerator/request/representationtypes-swift.struct/all.md).

## Topics

### Creating a Thumbnail Type
- [init(rawValue: UInt)](qlthumbnailgenerator/request/representationtypes-swift.struct/init(rawvalue:).md)
  Creates a new thumbnail type object for a given value.
- [static var all: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/all.md)
  The thumbnail type to generate all possible thumbnail representations.
- [static var icon: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/icon.md)
  A file icon representation of a file.
- [static var lowQualityThumbnail: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/lowqualitythumbnail.md)
  A faster to generate version of the thumbnail that may sacrifice quality for speed.
- [static var thumbnail: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct/thumbnail.md)
  A thumbnail representation of a file.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var size: CGSize](qlthumbnailgenerator/request/size.md)
  The size of the thumbnails.
- [var scale: CGFloat](qlthumbnailgenerator/request/scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](qlthumbnailgenerator/request/contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](qlthumbnailgenerator/request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](qlthumbnailgenerator/request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/representationtypes-swift.struct)*