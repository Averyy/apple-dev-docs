# PHASEAsset.AssetType.streamed

**Framework**: PHASE  
**Kind**: case

A sound asset that streams from disk into memory as it plays.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case streamed
```

#### Discussion

If the asset is on disk, the framework streams the asset’s data from disk into memory and prepares the asset during playback. If the asset is in memory, the framework streams from memory and prepares the asset during playback.

## See Also

- [PHASEAsset.AssetType.resident](phaseasset/assettype/resident.md)
  A sound asset that plays after fully loading in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseasset/assettype/streamed)*