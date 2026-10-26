# delegate

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An object to be notified when Live Photo playback begins or ends.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any PHLivePhotoViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, readwrite, nullable) id<PHLivePhotoViewDelegate> delegate;
```

## See Also

### Responding to Playback Events
- [protocol PHLivePhotoViewDelegate](../phlivephotoviewdelegate.md)
  The [`PHLivePhotoViewDelegate`](../phlivephotoviewdelegate.md) protocol describes messages sent by a [`PHLivePhotoView`](../phlivephotoview.md) instance in response to playback events when playing the motion and sound content associated with a Live Photo. To receive these messages, implement the methods in this protocol in one of your controller objects and assign that object to the [`delegate`](./delegate.md) property of a Live Photo view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview/delegate)*