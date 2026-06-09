# CVProResRawMetadata.RecommendedCrop

**Framework**: Core Video  
**Kind**: struct

Recommended pixels to discard in the image after raw conversion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RecommendedCrop
```

#### Overview

The values may be nonintegral due to downscaling, in which case the handling of fractional parts is implementation-dependent.

## Topics

### Initializers
- [init(pixelsToDiscardAtStartOfEachRow: Float32, pixelsToDiscardAtEndOfEachRow: Float32, rowsOfPixelsToDiscardAtTop: Float32, rowsOfPixelsToDiscardAtBottom: Float32)](cvproresrawmetadata/recommendedcrop-swift.struct/init(pixelstodiscardatstartofeachrow:pixelstodiscardatendofeachrow:rowsofpixelstodiscardattop:rowsofpixelstodiscardatbottom:).md)
### Instance Properties
- [var pixelsToDiscardAtEndOfEachRow: Float32](cvproresrawmetadata/recommendedcrop-swift.struct/pixelstodiscardatendofeachrow.md)
  Pixels to discard from the end (right) of each row of the image.
- [var pixelsToDiscardAtStartOfEachRow: Float32](cvproresrawmetadata/recommendedcrop-swift.struct/pixelstodiscardatstartofeachrow.md)
  Pixels to discard from the start (left) of each row of the image.
- [var rowsOfPixelsToDiscardAtBottom: Float32](cvproresrawmetadata/recommendedcrop-swift.struct/rowsofpixelstodiscardatbottom.md)
  Rows of pixels to discard from the bottom of the image.
- [var rowsOfPixelsToDiscardAtTop: Float32](cvproresrawmetadata/recommendedcrop-swift.struct/rowsofpixelstodiscardattop.md)
  Rows of pixels to discard from the top of the image.
### Type Properties
- [static let zero: CVProResRawMetadata.RecommendedCrop](cvproresrawmetadata/recommendedcrop-swift.struct/zero.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/recommendedcrop-swift.struct)*