# delegateQueue

**Framework**: AVFoundation  
**Kind**: property

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

## See Also

- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](avplayeritemrenderedlegibleoutput/delegate.md)
  A delegate object for this output.
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemrenderedlegibleoutput/setdelegate(_:queue:).md)
  Sets the delegate object and the queue on which it’s invoked.
- [protocol AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md)
  A delegate that handles the rendered pixel buffers produced by a rendered legible output object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/delegatequeue)*