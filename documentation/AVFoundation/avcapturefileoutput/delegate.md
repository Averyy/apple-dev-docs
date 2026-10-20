# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate object for the capture file output.

**Availability**:
- macOS 10.7+

## Declaration

```swift
unowned(unsafe) var delegate: (any AVCaptureFileOutputDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<AVCaptureFileOutputDelegate> delegate;
```

#### Discussion

The delegate is an object conforming to the [`AVCaptureFileOutputDelegate`](../avcapturefileoutputdelegate.md) protocol that will be able to monitor and control recording along exact sample boundaries.

## See Also

### Setting file output properties
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
- [var isRecordingPaused: Bool](./isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/delegate)*