# setDelegate(_:queue:)

**Framework**: AVFoundation  
**Kind**: method

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

## Parameters

- `delegate`: A delegate object for this output.
- `delegateQueue`: A dispatch queue on which the system calls all delegate methods.

## See Also

- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](avplayeritemrenderedlegibleoutput/delegate.md)
  A delegate object for this output.
- [var delegateQueue: dispatch_queue_t?](avplayeritemrenderedlegibleoutput/delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/setdelegate(_:queue:))*