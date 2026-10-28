# AVCaptureBroadcastVideoOutput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

[`AVCaptureBroadcastVideoOutput`](./avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](./avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class AVCaptureBroadcastVideoOutput
```

```objc
@interface AVCaptureBroadcastVideoOutput : AVCaptureOutput
```

## Overview

Not all [`AVCaptureDevice.Format`](./avcapturedevice/format.md) instances support [`AVCaptureBroadcastVideoOutput`](./avcapturebroadcastvideooutput.md). Before adding this output to a session, check the device format’s `AVCaptureDeviceFormat.unsupportedCaptureOutputClasses` property to verify that [`AVCaptureBroadcastVideoOutput`](./avcapturebroadcastvideooutput.md) is not listed. If the current format does not support broadcast video output, the connection will be marked inactive and no samples will be delivered.

## Topics

### Creating a broadcast video output
- [init()](./avcapturebroadcastvideooutput/init%28%29.md)
### Managing the Output
- [var delegate: (any AVCaptureBroadcastVideoOutputDelegate)?](./avcapturebroadcastvideooutput/delegate.md)
  The receiver’s delegate.
- [var delegateCallbackQueue: dispatch_queue_t?](./avcapturebroadcastvideooutput/delegatecallbackqueue.md)
  The dispatch queue on which all [`AVCaptureBroadcastVideoOutputDelegate`](./avcapturebroadcastvideooutputdelegate.md) methods will be called.
- [func setDelegate((any AVCaptureBroadcastVideoOutputDelegate)?, queue: dispatch_queue_t?)](./avcapturebroadcastvideooutput/setdelegate%28_,queue%29.md)
  Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.
### Managing Video Output
- [var videoSettings: [String : Any]?](./avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](./avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](./avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](./avcapturebroadcastvideooutput/resetframebuffer%28%29.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](./avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.
### Dropped Frame Replacement
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](./avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum.md)
  Constants indicating the replacement policy when a video frame is dropped.
### Instance Properties
- [var ancillaryDataEncoder: AVCaptureAncillaryDataEncoder](./avcapturebroadcastvideooutput/ancillarydataencoder.md)
  The AVCaptureAncillaryDataEncoder that sends per-frame lens/camera/user-defined acquisition data along with the video buffer.
### Type Methods
- [class func new() -> Self](./avcapturebroadcastvideooutput/new%28%29.md)

## Relationships

### Inherits From
- [AVCaptureOutput](./avcaptureoutput.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [protocol AVCaptureBroadcastVideoOutputDelegate](./avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
### Broadcast video output
- [protocol AVCaptureBroadcastVideoOutputDelegate](./avcapturebroadcastvideooutputdelegate.md)
  Protocol for receiving broadcast video output events and data.
- [class AVCaptureAncillaryDataEncoder](./avcaptureancillarydataencoder.md)
- [struct AVCaptureAncillaryDataUserKey](./avcaptureancillarydatauserkey.md)
  Clients may use an AVCaptureAncillaryDataUserKey to inspect the [`currentUserDefinedAncillaryData`](./avcaptureancillarydataencoder/currentuserdefinedancillarydata.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput)*