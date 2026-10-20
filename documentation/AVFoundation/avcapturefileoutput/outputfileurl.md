# outputFileURL

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The URL to which output is directed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var outputFileURL: URL? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSURL * outputFileURL;
```

## See Also

### Setting file output properties
- [var delegate: (any AVCaptureFileOutputDelegate)?](./delegate.md)
  The delegate object for the capture file output.
- [var maxRecordedDuration: CMTime](./maxrecordedduration.md)
  The longest duration allowed for the recording.
- [var maxRecordedFileSize: Int64](./maxrecordedfilesize.md)
  The maximum size, in bytes, of the data that should be recorded by the receiver.
- [var minFreeDiskSpaceLimit: Int64](./minfreediskspacelimit.md)
  The minimum amount of free space, in bytes, required for recording to continue on a given volume.
- [var recordedDuration: CMTime](./recordedduration.md)
  Indicates the duration of the media recorded to the current output file.
- [var recordedFileSize: Int64](./recordedfilesize.md)
  Indicates the size, in bytes, of the data recorded to the current output file.
- [var isRecording: Bool](./isrecording.md)
  Indicates whether recording is in progress.
- [var isRecordingPaused: Bool](./isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/outputfileurl)*