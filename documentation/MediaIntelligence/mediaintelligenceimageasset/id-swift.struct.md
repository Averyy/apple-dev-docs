# MediaIntelligenceImageAsset.ID

**Framework**: Media Intelligence  
**Kind**: struct  
**Role**: Structure

A unique identifier for an image asset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ID
```

#### Overview

[`MediaIntelligenceImageAsset.ID`](./id-swift.struct.md) is a string-backed identifier you assign to each image asset. The framework uses this value to track assets across calls to [`insertOrUpdateAssets(_:)`](../facegroupanalyzer/insertorupdateassets%28_%29.md) and [`deleteAssets(_:)`](../facegroupanalyzer/deleteassets%28_%29.md).

Choose identifiers that remain constant for a specified image. For example, a photo library asset identifier or a file path that doesn’t change.

## Topics

### Creating an ID
- [init(String)](./id-swift.struct/init%28_%29.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an asset
- [init(id: MediaIntelligenceImageAsset.ID, kind: MediaIntelligenceImageAsset.Kind)](./init%28id,kind%29.md)
  Creates an image asset with the specified identifier and kind.
- [MediaIntelligenceImageAsset.Kind](./kind-swift.enum.md)
  A value that describes the source of an image asset’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceimageasset/id-swift.struct)*