# stream(_:didOutputSampleBuffer:of:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Tells the delegate that a capture stream produced a frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 18.2+
- macOS 12.3+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
optional func stream(_ stream: SCStream, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, of type: SCStreamOutputType)
```

## Parameters

- `stream`: The frame capture stream that produced this frame.
- `sampleBuffer`: The sample buffer containing capture data.
- `type`: The type of capture contained in the sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstreamoutput/stream(_:didoutputsamplebuffer:of:))*