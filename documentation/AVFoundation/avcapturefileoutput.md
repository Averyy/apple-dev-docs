# AVCaptureFileOutput

**Framework**: AVFoundation  
**Kind**: class

The abstract superclass for capture outputs that can record captured data to a file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureFileOutput
```

## Topics

### Setting File Output Properties
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
- [var isRecordingPaused: Bool](avcapturefileoutput/isrecordingpaused.md)
  Indicates whether recording to the current output file is paused.
### Starting, Stopping, Pausing, and Resuming Playback
- [func startRecording(to: URL, recordingDelegate: any AVCaptureFileOutputRecordingDelegate)](avcapturefileoutput/startrecording(to:recordingdelegate:).md)
  Starts recording media to the specified output URL.
- [func stopRecording()](avcapturefileoutput/stoprecording.md)
  Tells the receiver to stop recording to the current file.
- [func pauseRecording()](avcapturefileoutput/pauserecording.md)
  Pauses recording to the current output file.
- [func resumeRecording()](avcapturefileoutput/resumerecording.md)
  Resumes recording to the current output file after it was previously paused using [`pauseRecording()`](avcapturefileoutput/pauserecording().md).

## Relationships

### Inherits From
- [AVCaptureOutput](avcaptureoutput.md)
### Inherited By
- [AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md)
- [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md)
  Change the default format for capturing movie files.
- [class AVCaptureMovieFileOutput](avcapturemoviefileoutput.md)
  A capture output that records video and audio to a QuickTime movie file.
- [class AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md)
  A capture output that records audio and saves the recorded audio to a file.
- [protocol AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md)
  Methods for monitoring or controlling the output of a media file capture.
- [protocol AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md)
  Methods for responding to events that occur while recording captured media to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput)*