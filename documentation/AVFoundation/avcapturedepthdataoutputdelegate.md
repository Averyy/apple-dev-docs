# AVCaptureDepthDataOutputDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol AVCaptureDepthDataOutputDelegate <NSObject>
```

## Topics

### Receiving depth data
- [func depthDataOutput(AVCaptureDepthDataOutput, didOutput: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection)](./avcapturedepthdataoutputdelegate/depthdataoutput%28_,didoutput,timestamp,connection%29.md)
  Provides newly captured depth data to the delegate.
- [func depthDataOutput(AVCaptureDepthDataOutput, didDrop: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection, reason: AVCaptureOutput.DataDroppedReason)](./avcapturedepthdataoutputdelegate/depthdataoutput%28_,diddrop,timestamp,connection,reason%29.md)
  Informs the delegate that captured depth data was not processed.
- [AVCaptureOutput.DataDroppedReason](./avcaptureoutput/datadroppedreason.md)
  Constants that define reasons for why the system dropped a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Receiving captured depth data
- [func setDelegate((any AVCaptureDepthDataOutputDelegate)?, callbackQueue: dispatch_queue_t?)](./avcapturedepthdataoutput/setdelegate%28_,callbackqueue%29.md)
  Designates a delegate object to receive depth data and a dispatch queue for delivering that data.
- [var delegate: (any AVCaptureDepthDataOutputDelegate)?](./avcapturedepthdataoutput/delegate.md)
  A delegate object that receives depth data.
- [var delegateCallbackQueue: dispatch_queue_t?](./avcapturedepthdataoutput/delegatecallbackqueue.md)
  A dispatch queue for delivering depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate)*