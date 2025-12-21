# PHASEAsset.AssetType

**Framework**: PHASE  
**Kind**: enum

Options that determine how PHASE manages sound assets in memory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum AssetType
```

#### Overview

To prepare for playback, the framework can decompress a sound asset or perform a format conversion, or both, depending on the type of the underlying asset data.

## Topics

### Types
- [PHASEAsset.AssetType.resident](phaseasset/assettype/resident.md)
  A sound asset that plays after fully loading in memory.
- [PHASEAsset.AssetType.streamed](phaseasset/assettype/streamed.md)
  A sound asset that streams from disk into memory as it plays.
### Initializers
- [init?(rawValue: Int)](phaseasset/assettype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasset/assettype)*