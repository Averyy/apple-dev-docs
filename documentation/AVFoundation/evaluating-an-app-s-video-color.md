# Evaluating an App’s Video Color

**Framework**: AVFoundation

Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.

#### Overview

AVFoundation automatically applies color management to video during playback. ColorSync creates a color transform that provides a color match between the video’s color space (as specified by the color tag in the media) and the specific chromaticity and gamma characteristics of your display.

ColorSync uses the display’s ICC profile to obtain its chromaticity and gamma characteristics. It then performs the color match using perceptual rendering intent to scale the video colors so they fit into the destination gamut specified by the display. AVFoundation applies this color transformation to each pixel of each frame in real time during video playback, ensuring the color fidelity of the original video.

> **Note**:  Viewers typically watch broadcast standards-based video in a dimly lit viewing environment such as a living room. The color management applied during playback lessens the contrast to preserve the correct tonality when viewing video in brighter viewing conditions.

 Viewers typically watch broadcast standards-based video in a dimly lit viewing environment such as a living room. The color management applied during playback lessens the contrast to preserve the correct tonality when viewing video in brighter viewing conditions.

##### Manage Color Reproduction

During playback, the color-management process changes the pixel values encoded in the video file to make them appear true to the original on the display. As a result of this color management, the [`Digital Color Meter app`](https://developer.apple.comhttps://support.apple.com/guide/digital-color-meter/welcome/mac) reports values from the display buffer that are different from the actual pixels encoded in the video file. Further, the Digital Color Meter app may report unequal pixel values between seemingly identical displays if their display profiles differ.

You can use a variety of techniques to verify that the system properly manages color in your video:

- Use test pattern files to evaluate the color characteristics of your app or workflow.
- Output the test pattern files to a vectorscope or waveform analyzer to review video signals.
- Use the test pattern files with a spectroradiometer or colorimeter to measure front-of-screen (FoS) luminance.

Appropriate color management of your video during playback requires tagging your content, using frameworks that offer implicit color management of video, and evaluating your results.

For more information about color tags, see [`Tagging Media with Video Color Information`](tagging-media-with-video-color-information.md).

##### Evaluate Video Using Test Pattern Files

Use test pattern files to evaluate the color characteristics of your AVFoundation-based app or workflow. These files produce expected results when displayed on Apple devices and operating systems. Open these files in the QuickTime Player App or with other apps or workflows that properly support the QuickTime File Format Specification. Read the display buffer pixel values using the Digital Color Meter app. See [`Evaluating Video Using QuickTime Test Pattern Files`](evaluating-video-using-quicktime-test-pattern-files.md).

##### Evaluate Video Using a Vectorscope or Waveform Analyzer

Output test patterns to a vectorscope or waveform analyzer to analyze the video signals. View the test pattern on a vectorscope and verify the correct colorspace conversion matrices. Verify the gamma, quantization errors, and range expansion and compression on a waveform monitor. See [`Evaluating an App’s Video Color Using Video Test Equipment`](evaluating-an-app-s-video-color-using-video-test-equipment.md).

##### Evaluate Video Using a Spectroradiometer or Colorimeter

Output the test pattern files to a spectroradiometer or colorimeter to measure front-of-screen (FoS) luminance. Measure and compare your results against the expected FoS values. See [`Evaluating an App’s Video Color Using Light-Measurement Instruments`](evaluating-an-app-s-video-color-using-light-measurement-instruments.md).

##### Ensure Accurate Color Application of Your Apps Video

To ensure application of the appropriate color management to your video during playback:

- Use high-level frameworks integrated with ColorSync, such as AVFoundation, for implicit color management.
- Tag all video content with color information to avoid inconsistent color across different devices. In most cases, the system treats untagged media as if the author created it in the SD color space. See [`Tagging Media with Video Color Information`](tagging-media-with-video-color-information.md).
- Evaluate all results using the techniques described here.

## Topics

### Video Evaluation
- [Evaluating Video Using QuickTime Test Pattern Files](evaluating-video-using-quicktime-test-pattern-files.md)
  Check color reproduction of your app or workflow by using test pattern files.
- [Evaluating an App’s Video Color Using Video Test Equipment](evaluating-an-app-s-video-color-using-video-test-equipment.md)
  Output test pattern files to a vectorscope or waveform analyzer to review the video signals.
- [Evaluating an App’s Video Color Using Light-Measurement Instruments](evaluating-an-app-s-video-color-using-light-measurement-instruments.md)
  Measure front-of-screen luminance by using test pattern files with a spectroradiometer or colorimeter.

## See Also

- [Writing Fragmented MPEG-4 Files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [class AVOutputSettingsAssistant](avoutputsettingsassistant.md)
  An object that builds audio and video output settings dictionaries.
- [class AVAssetWriter](avassetwriter.md)
  An object that writes media data to a container file.
- [class AVAssetWriterInput](avassetwriterinput.md)
  An object that appends media samples to a track in an asset writer’s output file.
- [class AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md)
  An object that appends video samples to an asset writer input.
- [class AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md)
  An object that appends tagged buffer groups to an asset writer input.
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/evaluating-an-app-s-video-color)*