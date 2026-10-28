# fileOutputShouldProvideSampleAccurateRecordingStart(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allows a client to opt in to frame accurate recording in [`fileOutput(_:didOutputSampleBuffer:from:)`](./fileoutput%28_,didoutputsamplebuffer,from%29.md).

**Availability**:
- macOS 10.8+

## Declaration

```swift
func fileOutputShouldProvideSampleAccurateRecordingStart(_ output: AVCaptureFileOutput) -> Bool
```

```objc
- (BOOL) captureOutputShouldProvideSampleAccurateRecordingStart:(AVCaptureOutput *) output;
```

## Return Value

[`true`](../../Swift/true.md) if frame accurate recording is required; otherwise [`false`](../../Swift/false.md).

## Discussion

In apps linked before OS X Mountain Lion, delegates that implement the [`fileOutput(_:didOutputSampleBuffer:from:)`](./fileoutput%28_,didoutputsamplebuffer,from%29.md) method can ensure that starting and stopping a recording is frame accurate by calling [`startRecording(to:recordingDelegate:)`](../avcapturefileoutput/startrecording%28to,recordingdelegate%29.md) or [`stopRecording()`](../avcapturefileoutput/stoprecording%28%29.md) from within the callback. Frame accurate recording requires the capture output to apply outputSettings when the session starts running, so it is ready to start and/or stop recording on any given frame boundary. Applying compression settings for the entire length of the session has power, thermal, and CPU implications.

In apps linked on or after OS X Mountain Lion, delegates must implement this method to indicate whether frame accurate recording is required. The capture file output calls this method only once when the delegate is added and never again. If your delegate returns [`false`](../../Swift/false.md), the capture file output applies compression settings only when [`startRecording(to:recordingDelegate:)`](../avcapturefileoutput/startrecording%28to,recordingdelegate%29.md) is called and disables these settings once the recording stops.

## Parameters

- `output`: The capture file output instance that is associated with the delegate.

## See Also

### Sample processing
- [func fileOutput(AVCaptureFileOutput, didOutputSampleBuffer: CMSampleBuffer, from: AVCaptureConnection)](./fileoutput%28_,didoutputsamplebuffer,from%29.md)
  Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(_:))*