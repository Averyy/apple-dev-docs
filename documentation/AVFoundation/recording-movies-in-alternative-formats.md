# Recording movies in alternative formats

**Framework**: AVFoundation

Change the default format for capturing movie files.

#### Overview

You use [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md) to capture QuickTime movie files, and the framework chooses the HEVC format by default on most iPhone and iPad models. However, you can change the default format in advance if you know you need a different format.

If your app shares the captured video using a system share sheet, the system automatically converts the video to a format thatʼs compatible with the destination device. However, if your app saves or shares captured video internally, for applications outside the system share sheet, you need to use a video-capture format thatʼs compatible with all target devices. This article shows you how to change the capture format dynamically, so that videos captured in your app begin in the desired format.

##### Change the Default Capture Format

You can change the default format at capture time by specifying it in the output settings for capturing movie files. Each capture device has a dictionary of settings that you adjust to control properties of the output movie file. For example, to capture video in H.264/MPEG-4 AVC, set the output settings key [`AVVideoCodecKey`](avvideocodeckey.md) to [`h264`](avvideocodectype/h264.md), as the example below shows:

For a list of supported capture codecs, see [`AVVideoCodecType`](avvideocodectype.md).

##### Convert Previously Captured Movie Files

In addition to saving or sharing captured video using a different default format, you can also convert existing movie file content by generating a new movie file based on the contents of the existing file. For details on how, see [`Exporting video to alternative formats`](exporting-video-to-alternative-formats.md).

## See Also

- [static let h264: AVVideoCodecType](avvideocodectype/h264.md)
  The H.264 video codec.
- [static let hevc: AVVideoCodecType](avvideocodectype/hevc.md)
  The HEVC video codec.
- [static let jpeg: AVVideoCodecType](avvideocodectype/jpeg.md)
  The JPEG video codec.
- [static let proRes422: AVVideoCodecType](avvideocodectype/prores422.md)
  The Apple ProRes 422 video codec.
- [static let proRes4444: AVVideoCodecType](avvideocodectype/prores4444.md)
  The Apple ProRes 4444 video codec.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/recording-movies-in-alternative-formats)*