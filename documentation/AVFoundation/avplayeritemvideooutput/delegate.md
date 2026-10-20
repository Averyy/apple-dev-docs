# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate for the video output object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVPlayerItemOutputPullDelegate)? { get }
```

```objc
@property (weak, readonly, nullable) id<AVPlayerItemOutputPullDelegate> delegate;
```

## See Also

### Configuring the delegate
- [func setDelegate((any AVPlayerItemOutputPullDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the delegate and dispatch queue for the receiver.
- [protocol AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md)
  Methods you can implement to respond to pixel buffer changes.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which to call delegate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/delegate)*