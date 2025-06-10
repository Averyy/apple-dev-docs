# Audio and video capture

**Framework**: AVFoundation

Capture audio and video directly to media files, or capture streams of media for direct access to media sample buffers.

## Topics

### File capture
- [Recording movies in alternative formats](recording-movies-in-alternative-formats.md)
  Change the default format for capturing movie files.
- [class AVCaptureMovieFileOutput](avcapturemoviefileoutput.md)
  A capture output that records video and audio to a QuickTime movie file.
- [class AVCaptureAudioFileOutput](avcaptureaudiofileoutput.md)
  A capture output that records audio and saves the recorded audio to a file.
- [class AVCaptureFileOutput](avcapturefileoutput.md)
  The abstract superclass for capture outputs that can record captured data to a file.
- [protocol AVCaptureFileOutputDelegate](avcapturefileoutputdelegate.md)
  Methods for monitoring or controlling the output of a media file capture.
- [protocol AVCaptureFileOutputRecordingDelegate](avcapturefileoutputrecordingdelegate.md)
  Methods for responding to events that occur while recording captured media to a file.
### Stream capture
- [Capturing Spatial Audio in your iOS app](capturing-spatial-audio-in-your-ios-app.md)
  Enhance your app’s audio recording capabilities by supporting Spatial Audio capture.
- [class AVCaptureVideoDataOutput](avcapturevideodataoutput.md)
  A capture output that records video and provides access to video frames for processing.
- [class AVCaptureAudioDataOutput](avcaptureaudiodataoutput.md)
  A capture output that records audio and provides access to audio sample buffers as they are recorded.
### Mac screen capture
- [class AVCaptureScreenInput](avcapturescreeninput.md)
  A capture input for recording from a screen in macOS.

## See Also

- [Capture setup](capture-setup.md)
  Configure built-in cameras and microphones, and external capture devices, for media capture.
- [Photo capture](photo-capture.md)
  Capture high-quality still images, Live Photos, and supporting photo data.
- [Additional data capture](additional-data-capture.md)
  Capture additional data including depth and metadata, and synchronize capture from multiple outputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/audio-and-video-capture)*