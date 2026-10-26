# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s delegate.

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
@property (weak, readonly) id<AVPlayerItemSampleBufferOutputDelegate> delegate;
```

## See Also

### Configuring the delegate
- [delegateQueue](./delegatequeue.md)
  The dispatch queue where the delegate is messaged.
- [- setDelegate:queue:](./setdelegate_queue_.md)
  Sets the receiver’s delegate and a dispatch queue on which the delegate will be called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput/delegate)*