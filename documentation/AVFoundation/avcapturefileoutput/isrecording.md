# isRecording

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates whether recording is in progress.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
var isRecording: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRecording) BOOL recording;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the file output currently has a file to which it is writing new samples, [`false`](../../Swift/false.md) otherwise.

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
- [var outputFileURL: URL?](./outputfileurl.md)
  The URL to which output is directed.
- [var recordedDuration: CMTime](./recordedduration.md)
  Indicates the duration of the media recorded to the current output file.
- [var recordedFileSize: Int64](./recordedfilesize.md)
  Indicates the size, in bytes, of the data recorded to the current output file.
- [var isRecordingPaused: Bool](./isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/isrecording)*