# playerItemWithAsset:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new player item for a specified asset.

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
+ (instancetype) playerItemWithAsset:(AVAsset *) asset;
```

#### Return Value

A new player item, initialized to play `asset`.

#### Discussion

This method is equivalent to invoking [`playerItemWithAsset:automaticallyLoadedAssetKeys:`](./playeritemwithasset_automaticallyloadedassetkeys_.md), passing `["duration"]` as the value of `automaticallyLoadedAssetKeys`.

## Parameters

- `asset`: The [`AVAsset`](../avasset.md) to be played.

## See Also

### Creating a player item
- [+ playerItemWithURL:](./playeritemwithurl_.md)
  Returns a new player item with a specified URL.
- [convenience init(url: URL)](./init%28url%29-1xrtk.md)
  Creates a player item with a specified URL.
- [convenience init(asset: AVAsset)](./init%28asset%29-87rjl.md)
  Creates a player item for a specified asset.
- [+ playerItemWithAsset:automaticallyLoadedAssetKeys:](./playeritemwithasset_automaticallyloadedassetkeys_.md)
  Creates a player item with the specified asset and the asset keys to automatically load.
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](./init%28asset,automaticallyloadedassetkeys%29-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/playeritemwithasset:)*