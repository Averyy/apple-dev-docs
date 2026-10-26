# livePhotoView(_:didEndPlaybackWith:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when Live Photos playback ends.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, didEndPlaybackWith playbackStyle: PHLivePhotoViewPlaybackStyle)
```

```objc
- (void) livePhotoView:(PHLivePhotoView *) livePhotoView didEndPlaybackWithStyle:(PHLivePhotoViewPlaybackStyle) playbackStyle;
```

## Parameters

- `livePhotoView`: The view that ended playback of Live Photo content.
- `playbackStyle`: The style of playback, indicating whether the content played in full or as a brief preview.

## See Also

### Responding to Live Photos Playback Events
- [func livePhotoView(PHLivePhotoView, canBeginPlaybackWith: PHLivePhotoViewPlaybackStyle) -> Bool](./livephotoview%28_,canbeginplaybackwith%29.md)
  Notifies the delegate to determine whether the Live Photo can begin playback.
- [func livePhotoView(PHLivePhotoView, willBeginPlaybackWith: PHLivePhotoViewPlaybackStyle)](./livephotoview%28_,willbeginplaybackwith%29.md)
  Notifies the delegate when Live Photos playback is beginning.
- [func livePhotoView(PHLivePhotoView, extraMinimumTouchDurationFor: UITouch, with: PHLivePhotoViewPlaybackStyle) -> TimeInterval](./livephotoview%28_,extraminimumtouchdurationfor,with%29.md)
  Notifies the delegate to offset the timing of a touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:didendplaybackwith:))*