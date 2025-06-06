# Writing Fragmented MPEG-4 Files for HTTP Live Streaming

**Framework**: Avfoundation

Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.

**Availability**:
- macOS 11.0+
- Xcode 12.0+

#### Overview

> **Note**: This sample code project is associated with WWDC20 session [`10011: Authoring Fragmented MPEG-4 with AVAssetWriter`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10011).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

1. Edit the shared scheme called `fmp4Writer`.
2. Open the Run action.
3. Replace the  argument with the path to a movie file on your local hard drive.
4. Replace the  argument  with your desired output directory; for example `~/Desktop/fmp4writer/`.

## See Also

- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an App’s Video Color](evaluating-an-app-s-video-color.md)
  Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
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

*[View on Apple Developer](https://developer.apple.com/documentation/AVFoundation/writing-fragmented-mpeg-4-files-for-http-live-streaming)*