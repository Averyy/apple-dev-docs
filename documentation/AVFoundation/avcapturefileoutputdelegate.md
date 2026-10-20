# AVCaptureFileOutputDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods for monitoring or controlling the output of a media file capture.

**Availability**:
- macOS 10.7+

## Declaration

```swift
protocol AVCaptureFileOutputDelegate : NSObjectProtocol
```

```objc
@protocol AVCaptureFileOutputDelegate <NSObject>
```

#### Overview

The `AVCaptureFileOutputDelegate` protocol defines an interface for delegates of an [`AVCaptureFileOutput`](./avcapturefileoutput.md) object to monitor and control recordings along exact sample boundaries.

## Topics

### Sample processing
- [func fileOutputShouldProvideSampleAccurateRecordingStart(AVCaptureFileOutput) -> Bool](./avcapturefileoutputdelegate/fileoutputshouldprovidesampleaccuraterecordingstart%28_%29.md)
  Allows a client to opt in to frame accurate recording in [`fileOutput(_:didOutputSampleBuffer:from:)`](./avcapturefileoutputdelegate/fileoutput%28_,didoutputsamplebuffer,from%29.md).
- [func fileOutput(AVCaptureFileOutput, didOutputSampleBuffer: CMSampleBuffer, from: AVCaptureConnection)](./avcapturefileoutputdelegate/fileoutput%28_,didoutputsamplebuffer,from%29.md)
  Gives the delegate the opportunity to inspect samples as they are received by the output and start and stop recording at exact times.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### File capture
- [Recording movies in alternative formats](./recording-movies-in-alternative-formats.md)
  Change the default format for capturing movie files.
- [class AVCaptureMovieFileOutput](./avcapturemoviefileoutput.md)
  A capture output that records video and audio to a QuickTime movie file.
- [class AVCaptureAudioFileOutput](./avcaptureaudiofileoutput.md)
  A capture output that records audio and saves the recorded audio to a file.
- [class AVCaptureFileOutput](./avcapturefileoutput.md)
  The abstract superclass for capture outputs that can record captured data to a file.
- [protocol AVCaptureFileOutputRecordingDelegate](./avcapturefileoutputrecordingdelegate.md)
  Methods for responding to events that occur while recording captured media to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputdelegate)*