# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate that receives timecode updates from the timecode generator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var delegate: (any AVCaptureTimecodeGeneratorDelegate)? { get }
```

```objc
@property (nonatomic, readonly, nullable) id<AVCaptureTimecodeGeneratorDelegate> delegate;
```

#### Discussion

You can use your [`delegate`](./delegate.md) to receive real-time timecode updates. Implement the `timecodeGenerator:didReceiveUpdate:` method in your delegate to handle updates.

## See Also

### Handling delegate callbacks
- [var delegateCallbackQueue: dispatch_queue_t?](./delegatecallbackqueue.md)
  The dispatch queue on which delegate callbacks are invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/delegate)*