# recordedFileSize

**Framework**: AVFoundation  
**Kind**: property

Indicates the size, in bytes, of the data recorded to the current output file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var recordedFileSize: Int64 { get }
```

#### Discussion

If a recording is in progress, this property returns the size in bytes of the data recorded so far.

## See Also

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
- [var isRecording: Bool](avcapturefileoutput/isrecording.md)
  Indicates whether recording is in progress.
- [var isRecordingPaused: Bool](avcapturefileoutput/isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/recordedfilesize)*