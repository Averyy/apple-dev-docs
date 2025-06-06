# pauseRecording()

**Framework**: AVFoundation  
**Kind**: method

Pauses recording to the current output file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 10.7+
- tvOS 18.0+

## Declaration

```swift
func pauseRecording()
```

#### Discussion

This method causes the receiver to stop writing captured samples to the current output file returned by [`outputFileURL`](avcapturefileoutput/outputfileurl.md), but leaves the file open so that samples can be written to it in the future, if [`resumeRecording()`](avcapturefileoutput/resumerecording().md) is called. This allows you to record multiple media segments that are not contiguous in time to a single file.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the last samples written to the current file are guaranteed to be those that were output immediately before those in the sample buffer passed to that method.

## See Also

- [var isRecordingPaused: Bool](avcapturefileoutput/isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.
- [func startRecording(to: URL, recordingDelegate: any AVCaptureFileOutputRecordingDelegate)](avcapturefileoutput/startrecording(to:recordingdelegate:).md)
  Starts recording media to the specified output URL.
- [func stopRecording()](avcapturefileoutput/stoprecording.md)
  Tells the receiver to stop recording to the current file.
- [func resumeRecording()](avcapturefileoutput/resumerecording.md)
  Resumes recording to the current output file after it was previously paused using [`pauseRecording()`](avcapturefileoutput/pauserecording().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/pauserecording())*