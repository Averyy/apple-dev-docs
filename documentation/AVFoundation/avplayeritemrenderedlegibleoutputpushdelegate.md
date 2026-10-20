# AVPlayerItemRenderedLegibleOutputPushDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A delegate that handles the rendered pixel buffers produced by a rendered legible output object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
protocol AVPlayerItemRenderedLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

```objc
@protocol AVPlayerItemRenderedLegibleOutputPushDelegate <AVPlayerItemOutputPushDelegate>
```

## Topics

### Handling rendered pixel buffers
- [func renderedLegibleOutput(AVPlayerItemRenderedLegibleOutput, didOutputRenderedCaptionImages: [AVRenderedCaptionImage], forItemTime: CMTime)](./avplayeritemrenderedlegibleoutputpushdelegate/renderedlegibleoutput%28_,didoutputrenderedcaptionimages,foritemtime%29.md)
  Tells the delegate that new rendered caption images are available.

## Relationships

### Inherits From
- [AVPlayerItemOutputPushDelegate](./avplayeritemoutputpushdelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting a delegate
- [var delegate: (any AVPlayerItemRenderedLegibleOutputPushDelegate)?](./avplayeritemrenderedlegibleoutput/delegate.md)
  A delegate object for this output.
- [func setDelegate((any AVPlayerItemRenderedLegibleOutputPushDelegate)?, queue: dispatch_queue_t?)](./avplayeritemrenderedlegibleoutput/setdelegate%28_,queue%29.md)
  Sets the delegate object and the queue on which it’s invoked.
- [var delegateQueue: dispatch_queue_t?](./avplayeritemrenderedlegibleoutput/delegatequeue.md)
  The dispatch queue on which the output calls the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutputpushdelegate)*