# fileOutputShouldProvideSampleAccurateRecordingStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Allows a client to opt in to frame accurate recording in [`fileOutput(_:didOutputSampleBuffer:from:)`](avcapturefileoutputdelegate/fileoutput(_:didoutputsamplebuffer:from:).md).

**Availability**:
- macOS 10.8+

## Declaration

```swift
func fileOutputShouldProvideSampleAccurateRecordingStart(_ output: AVCaptureFileOutput) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if frame accurate recording is required; otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

In apps linked before OS X Mountain Lion, delegates that implement the [`fileOutput(_:didOutputSampleBuffer:from:)`](avcapturefileoutputdelegate/fileoutput(_:didoutputsamplebuffer:from:).md) method can ensure that starting and stopping a recording is frame accurate by calling [`startRecording(to:recordingDelegate:)`](avcapturefileoutput/startrecording(to:recordingdelegate:).md) or [`stopRecording()`](avcapturefileoutput/stoprecording().md) from within the callback. Frame accurate recording requires the capture output to apply outputSettings when the session starts running, so it is ready to start and/or stop recording on any given frame boundary. Applying compression settings for the entire length of the session has power, thermal, and CPU implications.

In apps linked on or after OS X Mountain Lion, delegates must implement this method to indicate whether frame accurate recording is required. The capture file output calls this method only once when the delegate is added and never again. If your delegate returns [`false`](https://developer.apple.com/documentation/swift/false), the capture file output applies compression settings only when [`startRecording(to:recordingDelegate:)`](avcapturefileoutput/startrecording(to:recordingdelegate:).md) is called and disables these settings once the recording stops.

## Parameters

- `output`: The capture file output instance that is associated with the delegate.

## See Also

- [func fileOutput(AVCaptureFileOutput, didOutputSampleBuffer: CMSampleBuffer, from: AVCaptureConnection)](avcapturefileoutputdelegate/fileoutput(_:didoutputsamplebuffer:from:).md)
  Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(_:))*