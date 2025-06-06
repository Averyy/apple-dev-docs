# init(asset:automaticallyLoadedAssetKeys:)

**Framework**: AVFoundation  
**Kind**: init

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
@MainActor
init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)
```

#### Return Value

An initialized instance of `AVPlayerItem`.

#### Discussion

The value of each key in `automaticallyLoadedAssetKeys` will automatically be loaded by the underlying [`AVAsset`](avasset.md) before the player item achieves the status [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md); i.e. when the item is ready to play, the value returned by invoking the [`asset`](avplayeritem/asset.md) property’s [`statusOfValue(forKey:error:)`](avasynchronouskeyvalueloading/statusofvalue(forkey:error:).md) method will be one of the terminal status values, either [`AVKeyValueStatus.loaded`](avkeyvaluestatus/loaded.md), [`AVKeyValueStatus.failed`](avkeyvaluestatus/failed.md), or [`AVKeyValueStatus.cancelled`](avkeyvaluestatus/cancelled.md).

## Parameters

- `asset`: An instance of  .
- `automaticallyLoadedAssetKeys`: An array of strings, each representing a property defined by  .

## See Also

- [convenience init(url: URL)](avplayeritem/init(url:).md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](avplayeritem/init(asset:)-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](avplayeritem/init(asset:)-1nme9.md)
- [convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh.md)
  Creates a player item for the asset, and automatically loads values for the specified properties.
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4)*