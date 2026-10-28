# CVProResRawMetadata.RecommendedCrop

**Framework**: Core Video  
**Kind**: struct  
**Role**: Structure

Recommended pixels to discard in the image after raw conversion.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct RecommendedCrop
```

## Overview

The values may be nonintegral due to downscaling, in which case the handling of fractional parts is implementation-dependent.

## Topics

### Initializers
- [init(pixelsToDiscardAtStartOfEachRow: Float32, pixelsToDiscardAtEndOfEachRow: Float32, rowsOfPixelsToDiscardAtTop: Float32, rowsOfPixelsToDiscardAtBottom: Float32)](./recommendedcrop-swift.struct/init%28pixelstodiscardatstartofeachrow,pixelstodiscardatendofeachrow,rowsofpixelstodiscardattop,rowsofpixelstodiscardatbottom%29.md)
### Instance Properties
- [var pixelsToDiscardAtEndOfEachRow: Float32](./recommendedcrop-swift.struct/pixelstodiscardatendofeachrow.md)
  Pixels to discard from the end (right) of each row of the image.
- [var pixelsToDiscardAtStartOfEachRow: Float32](./recommendedcrop-swift.struct/pixelstodiscardatstartofeachrow.md)
  Pixels to discard from the start (left) of each row of the image.
- [var rowsOfPixelsToDiscardAtBottom: Float32](./recommendedcrop-swift.struct/rowsofpixelstodiscardatbottom.md)
  Rows of pixels to discard from the bottom of the image.
- [var rowsOfPixelsToDiscardAtTop: Float32](./recommendedcrop-swift.struct/rowsofpixelstodiscardattop.md)
  Rows of pixels to discard from the top of the image.
### Type Properties
- [static let zero: CVProResRawMetadata.RecommendedCrop](./recommendedcrop-swift.struct/zero.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../cvattachmentvaluerepresentable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvproresrawmetadata/recommendedcrop-swift.struct)*