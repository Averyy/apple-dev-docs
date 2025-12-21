# AVCaptureAudioFileOutput

**Framework**: AVFoundation  
**Kind**: class

A capture output that records audio and saves the recorded audio to a file.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class AVCaptureAudioFileOutput
```

#### Overview

`AVCaptureAudioFileOutput` implements the complete file recording interface declared by [`AVCaptureFileOutput`](avcapturefileoutput.md) for writing media data to audio files. In addition, you can configure options specific to the audio file formats, including writing metadata collections to each file and specifying audio encoding options. `AVCaptureAudioFileOutput` does not, however, support [`startRecording(to:recordingDelegate:)`](avcapturefileoutput/startrecording(to:recordingdelegate:).md)—use [`startRecording(to:outputFileType:recordingDelegate:)`](avcaptureaudiofileoutput/startrecording(to:outputfiletype:recordingdelegate:).md) instead.

## Topics

### Discovering supported types
- [class func availableOutputFileTypes() -> [AVFileType]](avcaptureaudiofileoutput/availableoutputfiletypes.md)
  Returns an array containing UTIs identifying the file types `AVCaptureAudioFileOutput` can write.
### Starting a recording
- [func startRecording(to: URL, outputFileType: AVFileType, recordingDelegate: any AVCaptureFileOutputRecordingDelegate)](avcaptureaudiofileoutput/startrecording(to:outputfiletype:recordingdelegate:).md)
  Tells the receiver to start recording to a new file of the specified format, and specifies a delegate that will be notified when recording is finished.
### Configuring output
- [var audioSettings: [String : Any]?](avcaptureaudiofileoutput/audiosettings.md)
  The settings used to decode or re-encode audio before it is output by the receiver.
- [var metadata: [AVMetadataItem]](avcaptureaudiofileoutput/metadata.md)
  A collection of metadata to be written to the receiver’s output files.
### Creating output
- [init()](avcaptureaudiofileoutput/init.md)
  Creates a new audio file output.

## Relationships

### Inherits From
- [AVCaptureFileOutput](avcapturefileoutput.md)
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
- [class AVCaptureFileOutput](avcapturefileoutput.md)
  The abstract superclass for capture outputs that can record captured data to a file.
- [protocol AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md)
  Methods for monitoring or controlling the output of a media file capture.
- [protocol AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md)
  Methods for responding to events that occur while recording captured media to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiofileoutput)*