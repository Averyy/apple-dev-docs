# delegate

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemrenderedlegibleoutput/setdelegate(_:queue:).md)
  Sets the delegate object and the queue on which it’s invoked.
- [var delegateQueue: dispatch_queue_t?](avplayeritemrenderedlegibleoutput/delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegate)*