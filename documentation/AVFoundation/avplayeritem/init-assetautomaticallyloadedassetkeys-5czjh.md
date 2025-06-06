# init(asset:automaticallyLoadedAssetKeys:)

**Framework**: AVFoundation  
**Kind**: init

Creates a player item for the asset, and automatically loads values for the specified properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>] = [])
```

#### Discussion

The system automatically loads values for the specified property identifiers before the player item reaches an [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md) state. In this state, calling [`status(of:)`](avasynchronouskeyvalueloading/status(of:).md) on a specified property identifier returns a value of [`AVAsyncProperty.Status.loaded(_:)`](avasyncproperty/status/loaded(_:).md) or [`AVAsyncProperty.Status.failed(_:)`](avasyncproperty/status/failed(_:).md).

## Parameters

- `asset`: The asset to play.
- `automaticallyLoadedAssetKeys`: An array of property identifiers for which the system automatically loads a value.

## See Also

- [convenience init(url: URL)](avplayeritem/init(url:).md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](avplayeritem/init(asset:)-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](avplayeritem/init(asset:)-1nme9.md)
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal.md)
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh)*