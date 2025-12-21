# PHASEAsset.AssetType.resident

**Framework**: PHASE  
**Kind**: case

A sound asset that plays after fully loading in memory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case resident
```

#### Discussion

If the sound asset is in memory, the framework prepares it for playback. If the asset is on disk, the framework loads it into memory, and prepares it for playback.

## See Also

- [PHASEAsset.AssetType.streamed](phaseasset/assettype/streamed.md)
  A sound asset that streams from disk into memory as it plays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasset/assettype/resident)*