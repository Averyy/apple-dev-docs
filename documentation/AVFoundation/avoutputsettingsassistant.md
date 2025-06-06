# AVOutputSettingsAssistant

**Framework**: AVFoundation  
**Kind**: class

An object that builds audio and video output settings dictionaries.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVOutputSettingsAssistant
```

#### Overview

Use an output settings assistant to create the audio and video settings that you use to configure instances of [`AVAssetWriter`](avassetwriter.md) and [`AVAssetWriterInput`](avassetwriterinput.md). You create an assistant with a specific preset configuration, such as [`hevc3840x2160WithAlpha`](avoutputsettingspreset/hevc3840x2160withalpha.md) or [`preset1920x1080`](avoutputsettingspreset/preset1920x1080.md). You can accept the settings dictionaries as is to generate a file that conforms to the criteria that the preset implies. You may also use the dictionaries it generates as a base configuration that you can customize as you require.

Providing the assistant additional details about your source media helps it generate more complete results. For example, setting a value for its [`sourceVideoFormat`](avoutputsettingsassistant/sourcevideoformat.md) property ensures that the assistant generates settings that don’t scale up video frames from a smaller size.

## Topics

### Creating an Assistant
- [convenience init?(preset: AVOutputSettingsPreset)](avoutputsettingsassistant/init(preset:).md)
  Creates an output setting assistant with a preset configuration.
- [struct AVOutputSettingsPreset](avoutputsettingspreset.md)
  A structure that defines preset configurations for an output settings assistant.
- [class func availableOutputSettingsPresets() -> [AVOutputSettingsPreset]](avoutputsettingsassistant/availableoutputsettingspresets.md)
  Returns an array of preset values to use to initialize an output settings assistant.
### Configuring Output Settings
- [var outputFileType: AVFileType](avoutputsettingsassistant/outputfiletype.md)
  A uniform type identifier (UTI) that indicates the type of file to write.
- [var audioSettings: [String : Any]?](avoutputsettingsassistant/audiosettings.md)
  An audio settings dictionary.
- [var sourceAudioFormat: CMAudioFormatDescription?](avoutputsettingsassistant/sourceaudioformat.md)
  The format of the source audio data.
- [var videoSettings: [String : Any]?](avoutputsettingsassistant/videosettings.md)
  A video settings dictionary.
- [var sourceVideoFormat: CMVideoFormatDescription?](avoutputsettingsassistant/sourcevideoformat.md)
  The format of the source video data.
- [var sourceVideoMinFrameDuration: CMTime](avoutputsettingsassistant/sourcevideominframeduration.md)
  A time value that describes the minimum frame duration of the video data.
- [var sourceVideoAverageFrameDuration: CMTime](avoutputsettingsassistant/sourcevideoaverageframeduration.md)
  A time value that describes the average frame duration of the video data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Writing Fragmented MPEG-4 Files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an App’s Video Color](evaluating-an-app-s-video-color.md)
  Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avoutputsettingsassistant)*