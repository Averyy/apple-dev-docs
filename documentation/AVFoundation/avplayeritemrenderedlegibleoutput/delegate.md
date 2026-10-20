# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A delegate object for this output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
weak var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<AVPlayerItemRenderedLegibleOutputPushDelegate> delegate;
```

## See Also

### Setting a delegate
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the delegate object and the queue on which it’s invoked.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegate)*