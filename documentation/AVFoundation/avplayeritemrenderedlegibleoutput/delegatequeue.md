# delegateQueue

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dispatch queue on which the output calls the delegate object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var delegateQueue: dispatch_queue_t? { get }
```

```objc
@property (nonatomic, readonly, nullable) dispatch_queue_t delegateQueue;
```

## See Also

### Setting a delegate
- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](./delegate.md)
  A delegate object for this output.
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./setdelegate%28_,queue%29.md)
  Sets the delegate object and the queue on which it’s invoked.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegatequeue)*