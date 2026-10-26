# setDelegate:queue:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s delegate and a dispatch queue on which the delegate will be called.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
- (void) setDelegate:(id<AVPlayerItemSampleBufferOutputDelegate>) delegate queue:(dispatch_queue_t) delegateQueue;
```

## Parameters

- `delegate`:  An object conforming to AVPlayerItemSampleBufferOutputDelegate protocol.
- `delegateQueue`:  A dispatch queue on which all delegate methods will be called.

## See Also

### Configuring the delegate
- [delegate](./delegate.md)
  The receiver’s delegate.
- [delegateQueue](./delegatequeue.md)
  The dispatch queue where the delegate is messaged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/setdelegate:queue:)*