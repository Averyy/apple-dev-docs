# AVCaptureFileOutputRecordingDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods for responding to events that occur while recording captured media to a file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```swift
protocol AVCaptureFileOutputRecordingDelegate : NSObjectProtocol
```

```objc
@protocol AVCaptureFileOutputRecordingDelegate <NSObject>
```

## Overview

Defines an interface for delegates of [`AVCaptureFileOutput`](./avcapturefileoutput.md) to respond to events that occur in the process of recording a single file.

The delegate of an `AVCaptureFileOutput` object must adopt the `AVCaptureFileOutputRecordingDelegate` protocol.

## Topics

### Delegate methods
- [func fileOutput(AVCaptureFileOutput, didStartRecordingTo: URL, from: [AVCaptureConnection])](./avcapturefileoutputrecordingdelegate/fileoutput%28_,didstartrecordingto,from%29.md)
  Informs the delegate when the output has started writing to a file.
- [func fileOutput(AVCaptureFileOutput, didStartRecordingTo: URL, startPTS: CMTime, from: [AVCaptureConnection])](./avcapturefileoutputrecordingdelegate/fileoutput%28_,didstartrecordingto,startpts,from%29.md)
- [func fileOutput(AVCaptureFileOutput, willFinishRecordingTo: URL, from: [AVCaptureConnection], error: (any Error)?)](./avcapturefileoutputrecordingdelegate/fileoutput%28_,willfinishrecordingto,from,error%29.md)
  Informs the delegate when the output will stop writing new samples to a file.
- [func fileOutput(AVCaptureFileOutput, didFinishRecordingTo: URL, from: [AVCaptureConnection], error: (any Error)?)](./avcapturefileoutputrecordingdelegate/fileoutput%28_,didfinishrecordingto,from,error%29.md)
  Informs the delegate when all pending data has been written to an output file.
- [func fileOutput(AVCaptureFileOutput, didPauseRecordingTo: URL, from: [AVCaptureConnection])](./avcapturefileoutputrecordingdelegate/fileoutput%28_,didpauserecordingto,from%29.md)
  Called whenever the output is recording to a file and successfully pauses the recording at the request of a client.
- [func fileOutput(AVCaptureFileOutput, didResumeRecordingTo: URL, from: [AVCaptureConnection])](./avcapturefileoutputrecordingdelegate/fileoutput%28_,didresumerecordingto,from%29.md)
  Called whenever the output, at the request of the client, successfully resumes a file recording that was paused.

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
- [protocol AVCaptureFileOutputDelegate](./avcapturefileoutputdelegate.md)
  Methods for monitoring or controlling the output of a media file capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate)*