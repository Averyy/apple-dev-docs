# Media reading and writing

**Framework**: AVFoundation

Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.

## Topics

### Media export
- [Exporting video to alternative formats](exporting-video-to-alternative-formats.md)
  Convert an existing movie file to a different format.
- [class AVAssetExportSession](avassetexportsession.md)
  An object that exports assets in a format that you specify using an export preset.
### Image generation
- [Creating images from a video asset](creating-images-from-a-video-asset.md)
  Display images for specific times within the media timeline by generating images from a video’s frames.
- [class AVAssetImageGenerator](avassetimagegenerator.md)
  An object that generates images from a video asset.
### Media reading
- [Reading multiview 3D video files](reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReader](avassetreader.md)
  An object that reads media data from an asset.
- [class AVAssetReaderOutput](avassetreaderoutput.md)
  An abstract class that defines the interface to read media samples from an asset reader.
- [class AVAssetReaderTrackOutput](avassetreadertrackoutput.md)
  An object that reads media data from a single track of an asset.
- [class AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.
### Media writing
- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md)
  Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Writing fragmented MPEG-4 files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging media with video color information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an app’s video color](evaluating-an-app-s-video-color.md)
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
### Captions
- [Caption authoring](caption-authoring.md)
  Create captions and subtitles in industry-standard formats.

## See Also

- [Media assets](media-assets.md)
  Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- [Media types and utilities](media-types-and-utilities.md)
  Identify the types of content and file formats that AVFoundation supports.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/media-reading-and-writing)*