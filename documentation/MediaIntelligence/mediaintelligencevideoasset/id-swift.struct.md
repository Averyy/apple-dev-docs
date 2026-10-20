# MediaIntelligenceVideoAsset.ID

**Framework**: Media Intelligence  
**Kind**: struct  
**Role**: Structure

A unique identifier for a video asset.

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

This value is a string-backed identifier that you assign to each video asset. Choose a value that uniquely identifies the video in your app, such as a file name or a database key.

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
- [init(id: MediaIntelligenceVideoAsset.ID, kind: MediaIntelligenceVideoAsset.Kind)](./init%28id,kind%29.md)
  Creates a video asset with the specified identifier and kind.
- [MediaIntelligenceVideoAsset.Kind](./kind-swift.enum.md)
  A value that describes the source of a video asset’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligencevideoasset/id-swift.struct)*