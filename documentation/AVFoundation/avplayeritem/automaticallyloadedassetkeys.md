# automaticallyLoadedAssetKeys

**Framework**: AVFoundation  
**Kind**: property

The array of asset keys to be automatically loaded before the player item is ready to play.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var automaticallyLoadedAssetKeys: [String] { get }
```

#### Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the [`asset`](avplayeritem/asset.md) prior to the player item reaching a status of [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md). When this status is reached, the asset’s [`statusOfValue(forKey:error:)`](avasynchronouskeyvalueloading/statusofvalue(forkey:error:).md) method returns [`AVKeyValueStatus.loaded`](avkeyvaluestatus/loaded.md) for the status of all keys in the array. If loading of any of the asset’s key values fails, the player item’s [`status`](avplayeritem/status-swift.property.md) will change to [`AVPlayerItem.Status.failed`](avplayeritem/status-swift.enum/failed.md).

## See Also

- [var asset: AVAsset](avplayeritem/asset.md)
  The asset provided during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/automaticallyloadedassetkeys)*