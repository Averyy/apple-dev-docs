# AVCompositionTrack

**Framework**: AVFoundation  
**Kind**: class

A track in a composition that presents media of a uniform type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVCompositionTrack
```

#### Overview

This object provides an immutable composition track. The framework also provides a mutable subclass, [`AVMutableCompositionTrack`](avmutablecompositiontrack.md).

## Topics

### Accessing Track Information
- [var isPlayable: Bool](avcompositiontrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avcompositiontrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avcompositiontrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avcompositiontrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](avcompositiontrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avcompositiontrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
### Accessing Temporal Information
- [var timeRange: CMTimeRange](avcompositiontrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var naturalTimeScale: CMTimeScale](avcompositiontrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avcompositiontrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avcompositiontrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.
### Accessing Language Support
- [var languageCode: String?](avcompositiontrack/languagecode.md)
  The language code of the track.
- [var extendedLanguageTag: String?](avcompositiontrack/extendedlanguagetag.md)
  The language tag of the track.
### Managing Format Descriptions
- [var formatDescriptions: [Any]](avcompositiontrack/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [var formatDescriptionReplacements: [AVCompositionTrackFormatDescriptionReplacement]](avcompositiontrack/formatdescriptionreplacements.md)
  The replacement format descriptions.
- [class AVCompositionTrackFormatDescriptionReplacement](avcompositiontrackformatdescriptionreplacement.md)
  An object that represents a format description and its replacement.
### Accessing Visual Characteristics
- [var naturalSize: CGSize](avcompositiontrack/naturalsize.md)
  The natural dimensions of the media data that the track references.
- [var preferredTransform: CGAffineTransform](avcompositiontrack/preferredtransform.md)
  The track’s transform preference to apply to its visual content during presentation or processing.
### Accessing Audible Characteristics
- [var preferredVolume: Float](avcompositiontrack/preferredvolume.md)
  The track’s volume preference for playing its audible media.
- [var hasAudioSampleDependencies: Bool](avcompositiontrack/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.
### Accessing Frame-Based Characteristics
- [var nominalFrameRate: Float](avcompositiontrack/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [var minFrameDuration: CMTime](avcompositiontrack/minframeduration.md)
  The minimum duration of the track’s frames.
- [var requiresFrameReordering: Bool](avcompositiontrack/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
### Accessing Metadata
- [var metadata: [AVMetadataItem]](avcompositiontrack/metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [var commonMetadata: [AVMetadataItem]](avcompositiontrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avcompositiontrack/availablemetadataformats.md)
  An array of metadata formats available for the track.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avcompositiontrack/metadata(forformat:).md)
  Returns metadata items that a track contains for the specified format.
### Accessing Track Segments
- [var segments: [AVCompositionTrackSegment]](avcompositiontrack/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func segment(forTrackTime: CMTime) -> AVCompositionTrackSegment?](avcompositiontrack/segment(fortracktime:).md)
  Returns a segment whose target time range contains, or is closest to, the specified track time.
### Accessing Track Associations
- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](avcompositiontrack/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](avcompositiontrack/associatedtracks(oftype:).md)
  Returns an array of associated tracks that have the specified association type.
### Determining Sample Cursor Support
- [var canProvideSampleCursors: Bool](avcompositiontrack/canprovidesamplecursors.md)
  A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## Relationships

### Inherits From
- [AVAssetTrack](avassettrack.md)
### Inherited By
- [AVMutableCompositionTrack](avmutablecompositiontrack.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVComposition](avcomposition.md)
  An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.
- [class AVCompositionTrackSegment](avcompositiontracksegment.md)
  A track segment that maps a time from the source media track to the composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcompositiontrack)*