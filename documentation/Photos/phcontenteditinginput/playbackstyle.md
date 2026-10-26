# playbackStyle

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The style in which to present this content to the user.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var playbackStyle: PHAsset.PlaybackStyle { get }
```

```objc
@property (nonatomic, assign, readonly) PHAssetPlaybackStyle playbackStyle;
```

#### Discussion

Use this value to specify the type of view and the appropriate APIs on the content editing input to display this content.

## See Also

### Working with Live Photo Assets
- [var livePhoto: PHLivePhoto?](./livephoto.md)
  The unedited Live Photo content of the editing input.
- [PHAsset.PlaybackStyle](../phasset/playbackstyle-swift.enum.md)
  An enumeration of asset playback styles that dictate how to present an asset to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/playbackstyle)*