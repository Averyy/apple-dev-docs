# SCStreamOutput

**Framework**: ScreenCaptureKit  
**Kind**: protocol  
**Role**: Protocol

A delegate protocol your app implements to receive capture stream output events.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol SCStreamOutput : NSObjectProtocol
```

```objc
@protocol SCStreamOutput <NSObject>
```

#### Overview

The [`SCStreamOutput`](./scstreamoutput.md) protocol provides a way to retrieve output from an [`SCStream`](./scstream.md).

After you call [`startCapture(completionHandler:)`](./scstream/startcapture%28completionhandler%29.md), the system provides frame data through the [`stream(_:didOutputSampleBuffer:of:)`](./scstreamoutput/stream%28_,didoutputsamplebuffer,of%29.md) method. You can inspect the [`CMSampleBuffer`](../CoreMedia/cmsamplebuffer.md) to retrieve image data, and inspect the sample buffer for metadata about the frame.

## Topics

### Receiving stream output
- [func stream(SCStream, didOutputSampleBuffer: CMSampleBuffer, of: SCStreamOutputType)](./scstreamoutput/stream%28_,didoutputsamplebuffer,of%29.md)
  Tells the delegate that a capture stream produced a frame.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Output processing
- [enum SCStreamOutputType](./scstreamoutputtype.md)
  Constants that represent output types for a stream frame.
- [struct SCStreamFrameInfo](./scstreamframeinfo.md)
  An instance that defines metadata keys for a stream frame.
- [enum SCFrameStatus](./scframestatus.md)
  Status values for a frame from a stream.
- [class SCClipBufferingOutput](./scclipbufferingoutput.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutput)*