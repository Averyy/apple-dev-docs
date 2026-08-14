# MediaIntelligenceImageAsset.ID

**Framework**: Media Intelligence  
**Kind**: struct

A unique identifier for an image asset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ID
```

#### Overview

[`MediaIntelligenceImageAsset.ID`](mediaintelligenceimageasset/id-swift.struct.md) is a string-backed identifier you assign to each image asset. The framework uses this value to track assets across calls to [`insertOrUpdateAssets(_:)`](facegroupanalyzer/insertorupdateassets(_:).md) and [`deleteAssets(_:)`](facegroupanalyzer/deleteassets(_:).md).

Choose identifiers that remain constant for a specified image. For example, a photo library asset identifier or a file path that doesn’t change.

## Topics

### Creating an ID
- [init(String)](mediaintelligenceimageasset/id-swift.struct/init(_:).md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(id: MediaIntelligenceImageAsset.ID, kind: MediaIntelligenceImageAsset.Kind)](mediaintelligenceimageasset/init(id:kind:).md)
  Creates an image asset with the specified identifier and kind.
- [MediaIntelligenceImageAsset.Kind](mediaintelligenceimageasset/kind-swift.enum.md)
  A value that describes the source of an image asset’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligenceimageasset/id-swift.struct)*