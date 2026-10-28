# livePhoto

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The unedited Live Photo content of the editing input.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var livePhoto: PHLivePhoto? { get }
```

```objc
@property (strong, readonly, nullable) PHLivePhoto * livePhoto;
```

## Discussion

To edit the video and photo content of the Live Photo, create a [`PHLivePhotoEditingContext`](../phlivephotoeditingcontext.md) object using this [`PHContentEditingInput`](../phcontenteditinginput.md) object.

If the editing input does not represent a Live Photo, this property’s value is `nil`, indicating that you cannot use this [`PHContentEditingInput`](../phcontenteditinginput.md) object to create a Live Photo editing context.

## See Also

### Working with Live Photo Assets
- [var playbackStyle: PHAsset.PlaybackStyle](./playbackstyle.md)
  The style in which to present this content to the user.
- [PHAsset.PlaybackStyle](../phasset/playbackstyle-swift.enum.md)
  An enumeration of asset playback styles that dictate how to present an asset to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditinginput/livephoto)*