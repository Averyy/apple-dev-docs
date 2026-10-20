# QLThumbnailGenerator.Request.RepresentationTypes

**Framework**: Quick Look Thumbnailing  
**Kind**: struct  
**Role**: Structure

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

```c
enum QLThumbnailGenerationRequestRepresentationTypes : NSUInteger;
```

#### Overview

Thumbnails come in one of three different types:

- **[`icon`](./representationtypes-swift.struct/icon.md)**: A file icon representation.
- **[`lowQualityThumbnail`](./representationtypes-swift.struct/lowqualitythumbnail.md)**: A faster to generate version of the thumbnail that may sacrifice quality for speed.
- **[`thumbnail`](./representationtypes-swift.struct/thumbnail.md)**: A high-quality thumbnail.

To request all thumbnail representations, use [`all`](./representationtypes-swift.struct/all.md).

## Topics

### Creating a Thumbnail Type
- [init(rawValue: UInt)](./representationtypes-swift.struct/init%28rawvalue%29.md)
  Creates a new thumbnail type object for a given value.
- [static var all: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct/all.md)
  The thumbnail type to generate all possible thumbnail representations.
- [static var icon: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct/icon.md)
  A file icon representation of a file.
- [static var lowQualityThumbnail: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct/lowqualitythumbnail.md)
  A faster to generate version of the thumbnail that may sacrifice quality for speed.
- [static var thumbnail: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct/thumbnail.md)
  A thumbnail representation of a file.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)

## See Also

### Describing the Requested Thumbnail
- [var size: CGSize](./size.md)
  The size of the thumbnails.
- [var scale: CGFloat](./scale.md)
  The pixel density of the display on the intended device.
- [var contentType: UTType!](./contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](./minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](./iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/representationtypes-swift.struct)*