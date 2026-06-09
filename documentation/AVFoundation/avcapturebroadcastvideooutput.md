# AVCaptureBroadcastVideoOutput

**Framework**: AVFoundation  
**Kind**: class

[`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class AVCaptureBroadcastVideoOutput
```

#### Overview

Not all [`AVCaptureDevice.Format`](avcapturedevice/format.md) instances support [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md). Before adding this output to a session, check the device format’s `AVCaptureDeviceFormat.unsupportedCaptureOutputClasses` property to verify that [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is not listed. If the current format does not support broadcast video output, the connection will be marked inactive and no samples will be delivered.

## Topics

### Creating a broadcast video output
- [init()](avcapturebroadcastvideooutput/init.md)
### Managing the Output
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [var delegateCallbackQueue: dispatch_queue_t?](avcapturebroadcastvideooutput/delegatecallbackqueue.md)
  The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](avcapturebroadcastvideooutputdelegate.md) methods will be called.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](avcapturebroadcastvideooutput/setdelegate(_:queue:).md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
### Managing Video Output
- [var videoSettings: [String : Any]?](avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.
### Dropped Frame Replacement
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum.md)
  Constants indicating the replacement policy when a video frame is dropped.
### Type Methods
- [class func new() -> Self](avcapturebroadcastvideooutput/new.md)

## Relationships

### Inherits From
- [AVCaptureOutput](avcaptureoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [protocol AVCaptureBroadcastVideoOutputDelegate](avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput)*