# init(asset:automaticallyLoadedAssetKeys:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a player item with the specified asset and the asset keys to automatically load.

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
init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)
```

```objc
- (instancetype) initWithAsset:(AVAsset *) asset automaticallyLoadedAssetKeys:(NSArray<NSString *> *) automaticallyLoadedAssetKeys;
```

## Return Value

An initialized instance of `AVPlayerItem`.

## Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the underlying [`AVAsset`](../avasset.md) before the player item achieves the status [`AVPlayerItem.Status.readyToPlay`](./status-swift.enum/readytoplay.md); i.e. when the item is ready to play, the value returned by invoking the [`asset`](./asset.md) property’s [`statusOfValue(forKey:error:)`](../avasynchronouskeyvalueloading/statusofvalue%28forkey,error%29.md) method will be one of the terminal status values, either [`AVKeyValueStatus.loaded`](../avkeyvaluestatus/loaded.md), [`AVKeyValueStatus.failed`](../avkeyvaluestatus/failed.md), or [`AVKeyValueStatus.cancelled`](../avkeyvaluestatus/cancelled.md).

## Parameters

- `asset`: An instance of [`AVAsset`](../avasset.md).
- `automaticallyLoadedAssetKeys`: An array of strings, each representing a property defined by [`AVAsset`](../avasset.md).

## See Also

### Creating a player item
- [convenience init(url: URL)](./init%28url%29-1xrtk.md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](./init%28asset%29-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](./init%28asset%29-1nme9.md)
- [convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](./init%28asset,automaticallyloadedassetkeys%29-5czjh.md)
  Creates a player item for the asset, and automatically loads values for the specified properties.
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](./init%28asset,automaticallyloadedassetkeys%29-85hal.md)
- [+ playerItemWithURL:](./playeritemwithurl_.md)
  Returns a new player item with a specified URL.
- [+ playerItemWithAsset:](./playeritemwithasset_.md)
  Returns a new player item for a specified asset.
- [+ playerItemWithAsset:automaticallyLoadedAssetKeys:](./playeritemwithasset_automaticallyloadedassetkeys_.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4)*