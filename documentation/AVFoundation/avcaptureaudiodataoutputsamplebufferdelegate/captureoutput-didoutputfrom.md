# captureOutput(_:didOutput:from:)

**Framework**: AVFoundation  
**Kind**: method

Notifies the delegate that a sample buffer was written.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
optional func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection)
```

## Parameters

- `output`: The capture output object.
- `sampleBuffer`: The sample buffer that was output.
- `connection`: The connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/captureoutput(_:didoutput:from:))*