# PHLivePhotoViewDelegate

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

The [`PHLivePhotoViewDelegate`](./phlivephotoviewdelegate.md) protocol describes messages sent by a [`PHLivePhotoView`](./phlivephotoview.md) instance in response to playback events when playing the motion and sound content associated with a Live Photo. To receive these messages, implement the methods in this protocol in one of your controller objects and assign that object to the [`delegate`](./phlivephotoview/delegate.md) property of a Live Photo view.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol PHLivePhotoViewDelegate : NSObjectProtocol
```

```objc
@protocol PHLivePhotoViewDelegate <NSObject>
```

## Topics

### Responding to Live Photos Playback Events
- [func livePhotoView(PHLivePhotoView, canBeginPlaybackWith: PHLivePhotoViewPlaybackStyle) -> Bool](./phlivephotoviewdelegate/livephotoview%28_,canbeginplaybackwith%29.md)
  Notifies the delegate to determine whether the Live Photo can begin playback.
- [func livePhotoView(PHLivePhotoView, willBeginPlaybackWith: PHLivePhotoViewPlaybackStyle)](./phlivephotoviewdelegate/livephotoview%28_,willbeginplaybackwith%29.md)
  Notifies the delegate when Live Photos playback is beginning.
- [func livePhotoView(PHLivePhotoView, didEndPlaybackWith: PHLivePhotoViewPlaybackStyle)](./phlivephotoviewdelegate/livephotoview%28_,didendplaybackwith%29.md)
  Notifies the delegate when Live Photos playback ends.
- [func livePhotoView(PHLivePhotoView, extraMinimumTouchDurationFor: UITouch, with: PHLivePhotoViewPlaybackStyle) -> TimeInterval](./phlivephotoviewdelegate/livephotoview%28_,extraminimumtouchdurationfor,with%29.md)
  Notifies the delegate to offset the timing of a touch.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to Playback Events
- [var delegate: (any PHLivePhotoViewDelegate)?](./phlivephotoview/delegate.md)
  An object to be notified when Live Photo playback begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoviewdelegate)*