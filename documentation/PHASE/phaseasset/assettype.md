# PHASEAsset.AssetType

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Options that determine how PHASE manages sound assets in memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum AssetType
```

```c
enum PHASEAssetType : NSInteger;
```

#### Overview

To prepare for playback, the framework can decompress a sound asset or perform a format conversion, or both, depending on the type of the underlying asset data.

## Topics

### Types
- [PHASEAsset.AssetType.resident](./assettype/resident.md)
  A sound asset that plays after fully loading in memory.
- [PHASEAsset.AssetType.streamed](./assettype/streamed.md)
  A sound asset that streams from disk into memory as it plays.
### Initializers
- [init?(rawValue: Int)](./assettype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasset/assettype)*