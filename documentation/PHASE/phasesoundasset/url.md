# url

**Framework**: PHASE  
**Kind**: property

The URL of the sound asset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL? { get }
```

#### Discussion

This property has a value when an app creates the asset with [`registerSoundAsset(url:identifier:assetType:channelLayout:normalizationMode:)`](phaseassetregistry/registersoundasset(url:identifier:assettype:channellayout:normalizationmode:).md); otherwise the value is `nil`.

## See Also

- [var data: Data?](phasesoundasset/data.md)
  A storage buffer for the sound asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundasset/url)*