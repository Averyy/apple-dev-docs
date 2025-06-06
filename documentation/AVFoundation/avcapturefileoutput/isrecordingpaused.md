# isRecordingPaused

**Framework**: AVFoundation  
**Kind**: property

Indicates whether recording to the current output file is paused.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 10.7+
- tvOS 18.0+

## Declaration

```swift
var isRecordingPaused: Bool { get }
```

#### Discussion

This property indicates recording to the file returned by [`outputFileURL`](avcapturefileoutput/outputfileurl.md) has been previously paused using the [`pauseRecording()`](avcapturefileoutput/pauserecording().md) method. When a recording is paused, captured samples are not written to the output file, but new samples can be written to the same file in the future by calling [`resumeRecording()`](avcapturefileoutput/resumerecording().md).

## See Also

- [func pauseRecording()](avcapturefileoutput/pauserecording.md)
  Pauses recording to the current output file.
- [func stopRecording()](avcapturefileoutput/stoprecording.md)
  Tells the receiver to stop recording to the current file.
- [var delegate: (any AVCaptureFileOutputDelegate)?](avcapturefileoutput/delegate.md)
  The delegate object for the capture file output.
- [var maxRecordedDuration: CMTime](avcapturefileoutput/maxrecordedduration.md)
  The longest duration allowed for the recording.
- [var maxRecordedFileSize: Int64](avcapturefileoutput/maxrecordedfilesize.md)
  The maximum size, in bytes, of the data that should be recorded by the receiver.
- [var minFreeDiskSpaceLimit: Int64](avcapturefileoutput/minfreediskspacelimit.md)
  The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [var outputFileURL: URL?](avcapturefileoutput/outputfileurl.md)
  The URL to which output is directed.
- [var recordedDuration: CMTime](avcapturefileoutput/recordedduration.md)
  Indicates the duration of the media recorded to the current output file.
- [var recordedFileSize: Int64](avcapturefileoutput/recordedfilesize.md)
  Indicates the size, in bytes, of the data recorded to the current output file.
- [var isRecording: Bool](avcapturefileoutput/isrecording.md)
  Indicates whether recording is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/isrecordingpaused)*