# AVCaptureDepthDataOutputDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Methods for receiving depth data produced by a depth capture output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
protocol AVCaptureDepthDataOutputDelegate : NSObjectProtocol
```

## Topics

### Receiving Depth Data
- [func depthDataOutput(AVCaptureDepthDataOutput, didOutput: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection)](avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:).md)
  Provides newly captured depth data to the delegate.
- [func depthDataOutput(AVCaptureDepthDataOutput, didDrop: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection, reason: AVCaptureOutput.DataDroppedReason)](avcapturedepthdataoutputdelegate/depthdataoutput(_:diddrop:timestamp:connection:reason:).md)
  Informs the delegate that captured depth data was not processed.
- [AVCaptureOutput.DataDroppedReason](avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setDelegate((any AVCaptureDepthDataOutputDelegate)?, callbackQueue: dispatch_queue_t?)](avcapturedepthdataoutput/setdelegate(_:callbackqueue:).md)
  Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [var delegate: (any AVCaptureDepthDataOutputDelegate)?](avcapturedepthdataoutput/delegate.md)
  A delegate object that receives depth data.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturedepthdataoutput/delegatecallbackqueue.md)
  A dispatch queue for delivering depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate)*