# init(asset:automaticallyLoadedAssetKeys:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a player item for the asset, and automatically loads values for the specified properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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

The system automatically loads values for the specified property identifiers before the player item reaches an [`AVPlayerItem.Status.readyToPlay`](./status-swift.enum/readytoplay.md) state. In this state, calling [`status(of:)`](../avasynchronouskeyvalueloading/status%28of%29.md) on a specified property identifier returns a value of [`AVAsyncProperty.Status.loaded(_:)`](../avasyncproperty/status/loaded%28_%29.md) or [`AVAsyncProperty.Status.failed(_:)`](../avasyncproperty/status/failed%28_%29.md).

## Parameters

- `asset`: The asset to play.
- `automaticallyLoadedAssetKeys`: An array of property identifiers for which the system automatically loads a value.

## See Also

### Creating a player item
- [convenience init(url: URL)](./init%28url%29-1xrtk.md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](./init%28asset%29-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](./init%28asset%29-1nme9.md)
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](./init%28asset,automaticallyloadedassetkeys%29-85hal.md)
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](./init%28asset,automaticallyloadedassetkeys%29-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh)*