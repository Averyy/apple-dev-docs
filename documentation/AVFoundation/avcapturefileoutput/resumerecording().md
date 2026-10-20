# resumeRecording()

**Framework**: AVFoundation  
**Kind**: method

Resumes recording to the current output file after it was previously paused using [`pauseRecording()`](avcapturefileoutput/pauserecording().md).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 10.7+
- tvOS 18.0+

## Declaration

```swift
func resumeRecording()
```

#### Discussion

This method causes the receiver to resume writing captured samples to the current output file returned by [`outputFileURL`](avcapturefileoutput/outputfileurl.md), after recording was previously paused using [`pauseRecording()`](avcapturefileoutput/pauserecording().md). This allows you to record multiple media segments that are not contiguous in time to a single file.

In macOS, if this method is called within the captureOutput:didOutputSampleBuffer:fromConnection: delegate method, the first samples written to the current file are guaranteed to be those contained in the sample buffer passed to        that method.

## See Also

- [var isRecordingPaused: Bool](avcapturefileoutput/isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.
- [func startRecording(to: URL, recordingDelegate: any AVCaptureFileOutputRecordingDelegate)](avcapturefileoutput/startrecording(to:recordingdelegate:).md)
  Starts recording media to the specified output URL.
- [func stopRecording()](avcapturefileoutput/stoprecording.md)
  Tells the receiver to stop recording to the current file.
- [func pauseRecording()](avcapturefileoutput/pauserecording.md)
  Pauses recording to the current output file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/resumerecording())*