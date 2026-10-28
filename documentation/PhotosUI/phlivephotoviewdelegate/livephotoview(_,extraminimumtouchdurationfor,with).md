# livePhotoView(_:extraMinimumTouchDurationFor:with:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate to offset the timing of a touch.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func livePhotoView(_ livePhotoView: PHLivePhotoView, extraMinimumTouchDurationFor touch: UITouch, with playbackStyle: PHLivePhotoViewPlaybackStyle) -> TimeInterval
```

```objc
- (NSTimeInterval) livePhotoView:(PHLivePhotoView *) livePhotoView extraMinimumTouchDurationForTouch:(UITouch *) touch withStyle:(PHLivePhotoViewPlaybackStyle) playbackStyle;
```

## Return Value

The time interval offset.

## Parameters

- `livePhotoView`: The view that ends playback of Live Photos content.
- `touch`: The touch to offset the timing for.
- `playbackStyle`: The style of playback, indicating whether the content plays in full or as a brief preview.

## See Also

### Responding to Live Photos Playback Events
- [func livePhotoView(PHLivePhotoView, canBeginPlaybackWith: PHLivePhotoViewPlaybackStyle) -> Bool](./livephotoview%28_,canbeginplaybackwith%29.md)
  Notifies the delegate to determine whether the Live Photo can begin playback.
- [func livePhotoView(PHLivePhotoView, willBeginPlaybackWith: PHLivePhotoViewPlaybackStyle)](./livephotoview%28_,willbeginplaybackwith%29.md)
  Notifies the delegate when Live Photos playback is beginning.
- [func livePhotoView(PHLivePhotoView, didEndPlaybackWith: PHLivePhotoViewPlaybackStyle)](./livephotoview%28_,didendplaybackwith%29.md)
  Notifies the delegate when Live Photos playback ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate/livephotoview(_:extraminimumtouchdurationfor:with:))*