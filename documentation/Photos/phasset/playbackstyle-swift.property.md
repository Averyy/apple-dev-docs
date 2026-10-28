# playbackStyle

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

An enumerated value that describes how to present an asset to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var playbackStyle: PHAsset.PlaybackStyle { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetPlaybackStyle playbackStyle;
```

## Discussion

Use this value to choose how your app displays the asset in [`PHImageManager`](../phimagemanager.md) regardless of the media type backing the asset.

## See Also

### Displaying an Asset
- [PHAsset.PlaybackStyle](./playbackstyle-swift.enum.md)
  An enumeration of asset playback styles that dictate how to present an asset to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/playbackstyle-swift.property)*