# maxRecordedFileSize

**Framework**: AVFoundation  
**Kind**: property

The maximum size, in bytes, of the data that should be recorded by the receiver.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var maxRecordedFileSize: Int64 { get set }
```

#### Discussion

This property specifies a hard limit on the data size of recorded files. Recording is stopped when the limit is reached and the [`fileOutput(_:didFinishRecordingTo:from:error:)`](avcapturefileoutputrecordingdelegate/fileoutput(_:didfinishrecordingto:from:error:).md) delegate method is invoked with an appropriate error. The default value of this property is `0`, which indicates no limit.

## See Also

- [var delegate: (any AVCaptureFileOutputDelegate)?](avcapturefileoutput/delegate.md)
  The delegate object for the capture file output.
- [var maxRecordedDuration: CMTime](avcapturefileoutput/maxrecordedduration.md)
  The longest duration allowed for the recording.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/maxrecordedfilesize)*