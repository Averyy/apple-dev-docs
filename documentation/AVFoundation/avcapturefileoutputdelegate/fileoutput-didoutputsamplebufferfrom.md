# fileOutput(_:didOutputSampleBuffer:from:)

**Framework**: AVFoundation  
**Kind**: method

Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func fileOutput(_ output: AVCaptureFileOutput, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection)
```

#### Discussion

This method is called whenever the file output receives a single sample buffer (a single video frame or audio buffer, for example) from the given connection. This gives delegates an opportunity to start and stop recording or change output files at an exact sample boundary. If called from within this method, the file output’s [`startRecording(to:recordingDelegate:)`](avcapturefileoutput/startrecording(to:recordingdelegate:).md) and [`resumeRecording()`](avcapturefileoutput/resumerecording().md) methods are guaranteed to include the received sample buffer in the new file, whereas calls to [`stopRecording()`](avcapturefileoutput/stoprecording().md) and [`pauseRecording()`](avcapturefileoutput/pauserecording().md) are guaranteed to include all samples leading up to those in the current sample buffer in the existing file.

You can gather information particular to the samples by inspecting the `CMSampleBuffer` object. Sample buffers always contain a single frame of video if called from this method but may also contain multiple samples of audio. For B-frame video formats, samples are always delivered in presentation order.

If you need to reference the `CMSampleBuffer` object outside of the scope of this method, you must retain it and then release it when you have finished with it.

To maintain optimal performance, some sample buffers directly reference pools of memory that may need to be reused by the device system and other capture inputs. This is frequently the case for uncompressed device native capture where memory blocks are copied as little as possible. If multiple sample buffers reference such pools of memory for too long, inputs will no longer be able to copy new samples into memory and those samples will be dropped. If your application is causing samples to be dropped by retaining the provided `CMSampleBuffer` objects for too long, but it needs access to the sample data for a long period of time, consider copying the data into a new buffer and then calling `CFRelease` on the sample buffer (if it was previously retained) so that the memory it references can be reused.

You should not assume that this method will be called on a specific thread. In addition, this method is called frequently, so it must be efficient to prevent capture performance problems.

## Parameters

- `output`: The capture file output that is receiving the media data.
- `sampleBuffer`: A   object containing the sample data and additional information about the sample, such as its format and presentation time.
- `connection`: The   object attached to the file output from which the sample data was received.

## See Also

- [func fileOutputShouldProvideSampleAccurateRecordingStart(AVCaptureFileOutput) -> Bool](avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart(_:).md)
  Allows a client to opt in to frame accurate recording in [`fileOutput(_:didOutputSampleBuffer:from:)`](avcapturefileoutputdelegate/fileoutput(_:didoutputsamplebuffer:from:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate/fileoutput(_:didoutputsamplebuffer:from:))*