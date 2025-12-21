# AVAssetWriterInputGroup

**Framework**: AVFoundation  
**Kind**: class

A group of inputs with tracks that are mutually exclusive to each other for playback or processing.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetWriterInputGroup
```

#### Overview

Assets may contain multiple tracks of media that are mutually exclusive to each other when you play or process them. For example, an asset may contain multiple audio tracks for different spoken languages, but only one of them should play at a time. You use an input group to mark a collection of tracks as mutually exclusive to each other in the file the asset writer outputs.

> **Note**:  After associating several tracks by calling [`addTrackAssociation(withTrackOf:type:)`](avassetwriterinput/addtrackassociation(withtrackof:type:).md), you can examine the media selection options an asset writer outputs before it writes the file.

## Topics

### Creating an input group
- [init(inputs: [AVAssetWriterInput], defaultInput: AVAssetWriterInput?)](avassetwriterinputgroup/init(inputs:defaultinput:).md)
  Creates a group for the asset writer inputs.
### Accessing the inputs
- [var inputs: [AVAssetWriterInput]](avassetwriterinputgroup/inputs.md)
  The inputs with tracks that are mutually exclusive to each other for playback or processing.
- [var defaultInput: AVAssetWriterInput?](avassetwriterinputgroup/defaultinput.md)
  The default input for the group.

## Relationships

### Inherits From
- [AVMediaSelectionGroup](avmediaselectiongroup.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputgroup)*