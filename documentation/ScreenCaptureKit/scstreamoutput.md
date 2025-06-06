# SCStreamOutput

**Framework**: ScreenCaptureKit  
**Kind**: protocol

A delegate protocol your app implements to receive capture stream output events.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
protocol SCStreamOutput : NSObjectProtocol
```

#### Overview

The [`SCStreamOutput`](scstreamoutput.md) protocol provides a way to retrieve output from an [`SCStream`](scstream.md).

After you call [`startCapture(completionHandler:)`](scstream/startcapture(completionhandler:).md), the system provides frame data through the [`stream(_:didOutputSampleBuffer:of:)`](scstreamoutput/stream(_:didoutputsamplebuffer:of:).md) method. You can inspect the [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) to retrieve image data, and inspect the sample buffer for metadata about the frame.

## Topics

### Receiving stream output
- [func stream(SCStream, didOutputSampleBuffer: CMSampleBuffer, of: SCStreamOutputType)](scstreamoutput/stream(_:didoutputsamplebuffer:of:).md)
  Tells the delegate that a capture stream produced a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum SCStreamOutputType](scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [struct SCStreamFrameInfo](scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](scframestatus.md)
  Status values for a frame from a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutput)*