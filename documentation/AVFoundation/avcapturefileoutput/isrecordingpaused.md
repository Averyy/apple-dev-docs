# isRecordingPaused

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isRecordingPaused) BOOL recordingPaused;
```

#### Discussion

This property indicates recording to the file returned by [`outputFileURL`](./outputfileurl.md) has been previously paused using the [`pauseRecording()`](./pauserecording%28%29.md) method. When a recording is paused, captured samples are not written to the output file, but new samples can be written to the same file in the future by calling [`resumeRecording()`](./resumerecording%28%29.md).

## See Also

### Related Documentation
- [func pauseRecording()](./pauserecording%28%29.md)
  Pauses recording to the current output file.
- [func stopRecording()](./stoprecording%28%29.md)
  Tells the receiver to stop recording to the current file.
### Setting file output properties
- [var delegate: (any AVCaptureFileOutputDelegate)?](./delegate.md)
  The delegate object for the capture file output.
- [var maxRecordedDuration: CMTime](./maxrecordedduration.md)
  The longest duration allowed for the recording.
- [var maxRecordedFileSize: Int64](./maxrecordedfilesize.md)
  The maximum size, in bytes, of the data that should be recorded by the receiver.
- [var minFreeDiskSpaceLimit: Int64](./minfreediskspacelimit.md)
  The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [var outputFileURL: URL?](./outputfileurl.md)
  The URL to which output is directed.
- [var recordedDuration: CMTime](./recordedduration.md)
  Indicates the duration of the media recorded to the current output file.
- [var recordedFileSize: Int64](./recordedfilesize.md)
  Indicates the size, in bytes, of the data recorded to the current output file.
- [var isRecording: Bool](./isrecording.md)
  Indicates whether recording is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/isrecordingpaused)*