# AVCaptureBroadcastVideoOutputDelegate

**Framework**: AVFoundation  
**Kind**: protocol

Protocol for receiving broadcast video output events and data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
protocol AVCaptureBroadcastVideoOutputDelegate : NSObjectProtocol
```

#### Overview

Objects conforming to this protocol can be set as delegates to receive notifications about broadcast video output operations, including dropped frames and ancillary data processing.

## Topics

### Responding to dropped frames
- [func broadcastVideoOutput(AVCaptureBroadcastVideoOutput, didDropVideoFrameWithPresentationTimeStamp: CMTime, from: AVCaptureConnection)](avcapturebroadcastvideooutputdelegate/broadcastvideooutput(_:diddropvideoframewithpresentationtimestamp:from:).md)
  Called when a video frame is dropped during broadcast video output processing.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVCaptureBroadcastVideoOutput](avcapturebroadcastvideooutput.md)
  [`AVCaptureBroadcastVideoOutput`](avcapturebroadcastvideooutput.md) is a subclass of [`AVCaptureOutput`](avcaptureoutput.md) that delivers broadcast-quality video and ancillary data through the device’s DisplayPort hardware interface (USB-C DP Alt Mode)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutputdelegate)*