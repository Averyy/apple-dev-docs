# init(url:)

**Framework**: AVFoundation  
**Kind**: init

Creates a player item with a specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
convenience init(url URL: URL)
```

#### Return Value

A new player item, prepared to use `URL`.

#### Discussion

This method immediately returns the item, but with the status [`AVPlayerItem.Status.unknown`](avplayeritem/status-swift.enum/unknown.md).

Associating the player item with an [`AVPlayer`](avplayer.md) immediately begins enqueuing its media and preparing it for playback. If the URL contains valid data that can be used by the player item, its status later changes to [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md). If the URL contains no valid data or otherwise can’t be used by the player item, its status later changes to [`AVPlayerItem.Status.failed`](avplayeritem/status-swift.enum/failed.md). You can determine the nature of the failure by querying the player item’s [`error`](avplayeritem/error.md) property.

## Parameters

- `URL`: A URL identifying the media resource to be played.

## See Also

- [convenience init(asset: AVAsset)](avplayeritem/init(asset:)-87rjl.md)
  Creates a player item for a specified asset.
- [convenience init(asset: any AVAsset & Sendable)](avplayeritem/init(asset:)-1nme9.md)
- [convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh.md)
  Creates a player item for the asset, and automatically loads values for the specified properties.
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal.md)
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(url:))*