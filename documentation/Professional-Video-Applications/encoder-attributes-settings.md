# Encoder Attributes Settings

**Framework**: Professional-Video-Applications  
**Role**: API Collection

Encoder attributes specify the audio and video configuration values for the output format.

## Overview

You specify the encoder attributes as the keys and values in the dictionary the [`settingsAttributes()`](../professional_video_applications/compressorextensionsettings/settingsattributes%28%29.md) method returns. The available encoder attribute keys are listed below.

## Topics

### Encoder Attribute Keys
- [var kCEAllowsSegmentationKey: String](../professional_video_applications/kceallowssegmentationkey.md)
  Specifies whether the extension supports segmentation of the source media.
- [var kCEFileExtensionKey: String](../professional_video_applications/kcefileextensionkey.md)
  Specifies the extension of the output file.
- [var kCEFieldOrderKey: String](../professional_video_applications/kcefieldorderkey.md)
  Specifies the output scanning method.
- [var kCEColorSpaceKey: String](../professional_video_applications/kcecolorspacekey.md)
  Specifies the color space supported in the output file.
- [var kCEAudioChannelLayoutKey: String](../professional_video_applications/kceaudiochannellayoutkey.md)
  Specifies the audio channel layout for the output file.
- [var kCEVideoEnabledKey: String](../professional_video_applications/kcevideoenabledkey.md)
  Specifies whether video is enabled in the output file.
- [var kCEAudioEnabledKey: String](../professional_video_applications/kceaudioenabledkey.md)
  Specifies whether audio is enabled in the output file.
- [var kCEAudioSampleFloatKey: String](../professional_video_applications/kceaudiosamplefloatkey.md)
  Specifies whether audio samples are in floating-point value.
- [var kCEAudioSampleRateKey: String](../professional_video_applications/kceaudiosampleratekey.md)
  Specifies the sample rate of audio in the output file.
- [var kCEAudioSampleSizeKey: String](../professional_video_applications/kceaudiosamplesizekey.md)
  Specifies the number of bits per audio sample in the output file.
- [var kCEWidthKey: String](../professional_video_applications/kcewidthkey.md)
  Specifies the width of the encoded video.
- [var kCEHeightKey: String](../professional_video_applications/kceheightkey.md)
  Specifies the height of the encoded video.
- [var kCEAutoRateKey: String](../professional_video_applications/kceautoratekey.md)
  Specifies whether the frame rate is set to automatic in the encoder settings.
- [var kCEAutoWidthKey: String](../professional_video_applications/kceautowidthkey.md)
  Specifies whether the output file width is set to automatic in the encoder settings.
- [var kCEAutoHeightKey: String](../professional_video_applications/kceautoheightkey.md)
  Specifies whether the output file height is set to automatic in the encoder settings.
- [var kCEPixelAspectKey: String](../professional_video_applications/kcepixelaspectkey.md)
  Specifies the aspect ratio of the output frame pixels.
- [var kCENumeratorKey: String](../professional_video_applications/kcenumeratorkey.md)
  Specifies the numerator of a ratio-based output frame rate.
- [var kCEDenominatorKey: String](../professional_video_applications/kcedenominatorkey.md)
  Specifies the denominator of a ratio-based output frame rate.
- [var kCEFrameRateKey: String](../professional_video_applications/kceframeratekey.md)
  Specifies the frame rate of the output file.
- [var kCEMarkerURLKey: String](../professional_video_applications/kcemarkerurlkey.md)
  Specifies the chapter marker URL when the marker image comes from a file stored on the web server.
- [var kCEMarkerTimeKey: String](../professional_video_applications/kcemarkertimekey.md)
  Specifies the chapter marker start time, in seconds.
- [var kCEMarkerNameKey: String](../professional_video_applications/kcemarkernamekey.md)
  Specifies the chapter marker name.
- [var kCEMarkerKindKey: String](../professional_video_applications/kcemarkerkindkey.md)
  Specifies the kind of marker.
- [var kCEMarkerImageSourceTimeKey: String](../professional_video_applications/kcemarkerimagesourcetimekey.md)
  Specifies a source file chapter marker’s start time, in seconds.
- [var kCEMarkerImageSourceFrameNumberKey: String](../professional_video_applications/kcemarkerimagesourceframenumberkey.md)
  Specifies a source file chapter marker’s start time, as a frame number.
- [var kCEMarkerImageFileURLKey: String](../professional_video_applications/kcemarkerimagefileurlkey.md)
  Specifies the marker’s file URL when the marker image comes from a local file.
- [var kCEMarkerFrameNumberKey: String](../professional_video_applications/kcemarkerframenumberkey.md)
  Specifies the output chapter marker’s start time, as a frame number.
- [var kCEMarkerDurationKey: String](../professional_video_applications/kcemarkerdurationkey.md)
  Specifies the duration of the chapter marker, as number of frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/encoder-attributes-settings)*