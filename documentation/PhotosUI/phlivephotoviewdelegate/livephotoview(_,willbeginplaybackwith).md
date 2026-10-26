# livePhotoView(_:willBeginPlaybackWith:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when Live Photos playback is beginning.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, willBeginPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle)
```

```objc
- (void) livePhotoView:(PHLivePhotoView *) livePhotoView willBeginPlaybackWithStyle:(PHLivePhotoViewPlaybackStyle) playbackStyle;
```

## Parameters

- `livePhotoView`: The view beginning playback of Live Photo content.
- `playbackStyle`: The style of playback, indicating whether the content is to play in full or as a brief preview.

## See Also

### Responding to Live Photos Playback Events
- [func livePhotoView(PHLivePhotoView, canBeginPlaybackWith: PHLivePhotoViewPlaybackStyle) -> Bool](./livephotoview%28_,canbeginplaybackwith%29.md)
  Notifies the delegate to determine whether the Live Photo can begin playback.
- [func livePhotoView(PHLivePhotoView, didEndPlaybackWith: PHLivePhotoViewPlaybackStyle)](./livephotoview%28_,didendplaybackwith%29.md)
  Notifies the delegate when Live Photos playback ends.
- [func livePhotoView(PHLivePhotoView, extraMinimumTouchDurationFor: UITouch, with: PHLivePhotoViewPlaybackStyle) -> TimeInterval](./livephotoview%28_,extraminimumtouchdurationfor,with%29.md)
  Notifies the delegate to offset the timing of a touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:willbeginplaybackwith:))*