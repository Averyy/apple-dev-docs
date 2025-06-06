# AVAssetWriter

**Framework**: AVFoundation  
**Kind**: class

An object that writes media data to a container file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetWriter
```

#### Overview

You use an asset writer to write media to file formats such as the QuickTime movie file format and MPEG-4 file format. An asset writer automatically supports interleaving media data from concurrent tracks for efficient playback and storage. It can reencode media samples it writes to the output file, and may also write collections of metadata to the output file.

> ❗ **Important**:  An asset writer is a single-use object that writes one output file. Create multiple asset writer instances if your app requires writing multiple output files.

 An asset writer is a single-use object that writes one output file. Create multiple asset writer instances if your app requires writing multiple output files.

## Topics

### Creating an Asset Writer
- [convenience init(url: URL, fileType: AVFileType) throws](avassetwriter/init(url:filetype:).md)
  Returns a new object that writes media data to a container file at the output URL.
- [init(outputURL: URL, fileType: AVFileType) throws](avassetwriter/init(outputurl:filetype:).md)
  Creates an object that writes media data to a container file at the output URL.
- [init(contentType: UTType)](avassetwriter/init(contenttype:).md)
  Creates an object that outputs segment data in a specified container format.
### Configuring Inputs
- [var inputs: [AVAssetWriterInput]](avassetwriter/inputs.md)
  The inputs an asset writer contains.
- [var availableMediaTypes: [AVMediaType]](avassetwriter/availablemediatypes.md)
  The media types the asset writer supports adding as inputs.
- [func canApply(outputSettings: [String : Any]?, forMediaType: AVMediaType) -> Bool](avassetwriter/canapply(outputsettings:formediatype:).md)
  Determines whether the output file format supports the output settings for a specific media type.
- [func canAdd(AVAssetWriterInput) -> Bool](avassetwriter/canadd(_:)-6al7j.md)
  Determines whether the asset writer supports adding the input.
- [func add(AVAssetWriterInput)](avassetwriter/add(_:)-4c4d0.md)
  Adds an input to an asset writer.
### Configuring Input Groups
- [var inputGroups: [AVAssetWriterInputGroup]](avassetwriter/inputgroups.md)
  The input groups an asset writer contains.
- [func canAdd(AVAssetWriterInputGroup) -> Bool](avassetwriter/canadd(_:)-8s1oh.md)
  Determines whether the asset writer supports adding the input group.
- [func add(AVAssetWriterInputGroup)](avassetwriter/add(_:)-3san4.md)
  Adds an input group to an asset writer.
### Configuring Output
- [var metadata: [AVMetadataItem]](avassetwriter/metadata.md)
  An array of metadata items to write to the output file.
- [var shouldOptimizeForNetworkUse: Bool](avassetwriter/shouldoptimizefornetworkuse.md)
  A Boolean value that indicates whether to write the output file to make it more suitable for playback over a network.
- [var directoryForTemporaryFiles: URL?](avassetwriter/directoryfortemporaryfiles.md)
  A directory to contain temporary files that the export process generates.
### Configuring Fragment Output
- [var movieFragmentInterval: CMTime](avassetwriter/moviefragmentinterval.md)
  The interval at which to write movie fragments.
- [var initialMovieFragmentInterval: CMTime](avassetwriter/initialmoviefragmentinterval.md)
  The interval at which to write the initial movie fragment.
- [var initialMovieFragmentSequenceNumber: Int](avassetwriter/initialmoviefragmentsequencenumber.md)
  The sequence number of the initial movie fragment.
- [var producesCombinableFragments: Bool](avassetwriter/producescombinablefragments.md)
  A Boolean value that indicates whether the asset writer outputs movie fragments suitable for combining with others.
- [var overallDurationHint: CMTime](avassetwriter/overalldurationhint.md)
  A hint of the final duration of the output file.
- [var movieTimeScale: CMTimeScale](avassetwriter/movietimescale.md)
  The time scale of the movie.
### Managing Writing Sessions
- [func startWriting() -> Bool](avassetwriter/startwriting.md)
  Tells the writer to start writing its output.
- [func startSession(atSourceTime: CMTime)](avassetwriter/startsession(atsourcetime:).md)
  Starts an asset-writing session.
- [func endSession(atSourceTime: CMTime)](avassetwriter/endsession(atsourcetime:).md)
  Finishes an asset-writing session.
- [func finishWriting(completionHandler: () -> Void)](avassetwriter/finishwriting(completionhandler:).md)
  Marks all unfinished inputs as finished and completes the writing of the output file.
- [func cancelWriting()](avassetwriter/cancelwriting.md)
  Cancels the creation of the output file.
- [func finishWriting() -> Bool](avassetwriter/finishwriting.md)
  Completes the writing of the output file.
### Inspecting Writing Status
- [var status: AVAssetWriter.Status](avassetwriter/status-swift.property.md)
  The status of writing samples to the output file.
- [AVAssetWriter.Status](avassetwriter/status-swift.enum.md)
  Values that indicate the state of an asset writer.
- [var error: (any Error)?](avassetwriter/error.md)
  An error object that describes an asset-writing failure.
### Configuring Segment Writing
- [var delegate: (any AVAssetWriterDelegate)?](avassetwriter/delegate.md)
  A delegate object that responds to asset-writing events.
- [protocol AVAssetWriterDelegate](avassetwriterdelegate.md)
  A delegate protocol that defines the methods to implement to respond to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](avassetwriter/preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var initialSegmentStartTime: CMTime](avassetwriter/initialsegmentstarttime.md)
  The start time of the initial segment.
- [var outputFileTypeProfile: AVFileTypeProfile?](avassetwriter/outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](avassetwriter/flushsegment.md)
  Closes the current segment and outputs it to a delegate method.
### Accessing Output Settings
- [var outputURL: URL](avassetwriter/outputurl.md)
  The location of the container file that the writer outputs.
- [var outputFileType: AVFileType](avassetwriter/outputfiletype.md)
  The type of container file that the writer outputs.

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
- [class AVOutputSettingsAssistant](avoutputsettingsassistant.md)
  An object that builds audio and video output settings dictionaries.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter)*