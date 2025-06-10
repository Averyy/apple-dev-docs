# Converting projected video to Apple Projected Media Profile

**Framework**: AVFoundation

Convert content with equirectangular or half-equirectangular projection to APMP.

**Availability**:
- macOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 297: [`Learn about the Apple Projected Media Profile`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/297).

##### Configure the Sample Code Project

The app takes a path to a monoscopic or stereoscopic (frame-packed) side-by-side or over-under stereo input video file as a single command-line argument. To run the app in Xcode, click the Run button to convert the included side-by-side frame-packed stereoscopic 180 sample asset (`Lighthouse_sbs.mp4`), or choose Product > Scheme > Edit Scheme, and edit the path to your file on the Arguments tab of the Run build scheme action.

To add projected media metadata to an output file, pass one of the following two options:

Other options:

By default, the project’s scheme loads a side-by-side video from the Xcode project folder named `Lighthouse_sbs.mp4`.

## See Also

- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Writing Fragmented MPEG-4 Files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/converting-projected-video-to-apple-projected-media-profile)*