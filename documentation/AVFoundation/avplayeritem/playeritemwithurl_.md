# playerItemWithURL:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new player item with a specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) playerItemWithURL:(NSURL *) URL;
```

## Return Value

A new player item, prepared to use `URL`.

## Discussion

This method immediately returns the item, but with the status [`AVPlayerItem.Status.unknown`](./status-swift.enum/unknown.md).

Associating the player item with an [`AVPlayer`](../avplayer.md) immediately begins enqueuing its media and preparing it for playback. If the URL contains valid data that can be used by the player item, its status later changes to [`AVPlayerItem.Status.readyToPlay`](./status-swift.enum/readytoplay.md). If the URL contains no valid data or otherwise can’t be used by the player item, its status later changes to [`AVPlayerItem.Status.failed`](./status-swift.enum/failed.md). You can determine the nature of the failure by querying the player item’s [`error`](./error.md) property.

## Parameters

- `URL`: A URL identifying the media resource to be played.

## See Also

### Creating a player item
- [convenience init(url: URL)](./init%28url%29-1xrtk.md)
  Creates a player item with a specified URL.
- [+ playerItemWithAsset:](./playeritemwithasset_.md)
  Returns a new player item for a specified asset.
- [convenience init(asset: AVAsset)](./init%28asset%29-87rjl.md)
  Creates a player item for a specified asset.
- [+ playerItemWithAsset:automaticallyLoadedAssetKeys:](./playeritemwithasset_automaticallyloadedassetkeys_.md)
  Creates a player item with the specified asset and the asset keys to automatically load.
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](./init%28asset,automaticallyloadedassetkeys%29-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/playeritemwithurl:)*