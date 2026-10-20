# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the delegate object and the queue on which it’s invoked.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
func setDelegate(_ delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

```objc
- (void) setDelegate:(id<AVPlayerItemRenderedLegibleOutputPushDelegate>) delegate queue:(dispatch_queue_t) delegateQueue;
```

## Parameters

- `delegate`: A delegate object for this output.
- `delegateQueue`: A dispatch queue on which the system calls all delegate methods.

## See Also

### Setting a delegate
- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](./delegate.md)
  A delegate object for this output.
- [var delegateQueue: dispatch_queue_t?](./delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](../avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/setdelegate(_:queue:))*