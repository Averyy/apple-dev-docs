# init(asset:)

**Framework**: AVFoundation  
**Kind**: init

Creates a player item for a specified asset.

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
@MainActor
convenience init(asset: AVAsset)
```

#### Return Value

A new player item, initialized to play `asset`.

## Parameters

- `asset`: The   to be played.

## See Also

- [convenience init(url: URL)](avplayeritem/init(url:).md)
  Creates a player item with a specified URL.
- [convenience init(asset: any AVAsset & Sendable)](avplayeritem/init(asset:)-1nme9.md)
- [convenience init(asset: AVAsset, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-5czjh.md)
  Creates a player item for the asset, and automatically loads values for the specified properties.
- [convenience init(asset: any AVAsset & Sendable, automaticallyLoadedAssetKeys: [AVPartialAsyncProperty<AVAsset>])](avplayeritem/init(asset:automaticallyloadedassetkeys:)-85hal.md)
- [init(asset: AVAsset, automaticallyLoadedAssetKeys: [String]?)](avplayeritem/init(asset:automaticallyloadedassetkeys:)-8x4.md)
  Creates a player item with the specified asset and the asset keys to automatically load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/init(asset:)-87rjl)*