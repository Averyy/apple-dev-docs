# maxRecordedDuration

**Framework**: AVFoundation  
**Kind**: property

The longest duration allowed for the recording.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var maxRecordedDuration: CMTime { get set }
```

#### Discussion

This property specifies a hard limit on the duration of recorded files. Recording is stopped when the limit is reached and the [`fileOutput(_:didFinishRecordingTo:from:error:)`](avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:).md) delegate method is invoked with an appropriate error. The default value of this property is [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid), which indicates no limit.

## See Also

- [var delegate: (any AVCaptureFileOutputDelegate)?](avcapturefileoutput/delegate.md)
  The delegate object for the capture file output.
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
- [var isRecordingPaused: Bool](avcapturefileoutput/isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/maxrecordedduration)*