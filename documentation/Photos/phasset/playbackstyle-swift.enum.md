# PHAsset.PlaybackStyle

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

An enumeration of asset playback styles that dictate how to present an asset to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum PlaybackStyle
```

```c
enum PHAssetPlaybackStyle : NSInteger;
```

## Topics

### Playback Styles
- [PHAsset.PlaybackStyle.unsupported](./playbackstyle-swift.enum/unsupported.md)
  An enumeration indicating that the asset has an unsupported or undefined media playback type.
- [PHAsset.PlaybackStyle.image](./playbackstyle-swift.enum/image.md)
  An enumeration indicating that the asset should be displayed as a still image.
- [PHAsset.PlaybackStyle.imageAnimated](./playbackstyle-swift.enum/imageanimated.md)
  An enumeration indicating that the asset should be displayed as an animated image.
- [PHAsset.PlaybackStyle.livePhoto](./playbackstyle-swift.enum/livephoto.md)
  An enumeration indicating that the asset should be displayed as a Live Photo.
- [PHAsset.PlaybackStyle.video](./playbackstyle-swift.enum/video.md)
  An enumeration indicating that the asset should be displayed as a video.
- [PHAsset.PlaybackStyle.videoLooping](./playbackstyle-swift.enum/videolooping.md)
  An enumeration indicating that the asset should be displayed as a looping video.
### Initializers
- [init?(rawValue: Int)](./playbackstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying an Asset
- [var playbackStyle: PHAsset.PlaybackStyle](./playbackstyle-swift.property.md)
  An enumerated value that describes how to present an asset to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/playbackstyle-swift.enum)*