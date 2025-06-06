# Deprecated Symbols

**Framework**: AVFoundation

Review unsupported symbols and their replacements.

#### Overview

[`AVAssetTrack`](avassettrack.md) doesn’t support using its synchronous property accessors that can block the calling thread. Instead, use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to load [`AVAsyncProperty`](avasyncproperty.md) values asynchronously.

## Topics

### Accessing Track Information
- [var formatDescriptions: [Any]](avassettrack/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [var isPlayable: Bool](avassettrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avassettrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avassettrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avassettrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var totalSampleDataLength: Int64](avassettrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avassettrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
### Accessing Temporal Information
- [var timeRange: CMTimeRange](avassettrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var naturalTimeScale: CMTimeScale](avassettrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avassettrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
### Accessing Language Support
- [var languageCode: String?](avassettrack/languagecode.md)
  The language code of the track.
- [var extendedLanguageTag: String?](avassettrack/extendedlanguagetag.md)
  The language tag of the track.
### Accessing Visual Characteristics
- [var naturalSize: CGSize](avassettrack/naturalsize.md)
  The natural dimensions of the media data that the track references.
- [var preferredTransform: CGAffineTransform](avassettrack/preferredtransform.md)
  The track’s transform preference to apply to its visual content during presentation or processing.
### Accessing Audible Characteristics
- [var preferredVolume: Float](avassettrack/preferredvolume.md)
  The track’s volume preference for playing its audible media.
- [var hasAudioSampleDependencies: Bool](avassettrack/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.
### Accessing Frame-Based Characteristics
- [var nominalFrameRate: Float](avassettrack/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [var minFrameDuration: CMTime](avassettrack/minframeduration.md)
  The minimum duration of the track’s frames.
- [var requiresFrameReordering: Bool](avassettrack/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
### Accessing Metadata
- [var metadata: [AVMetadataItem]](avassettrack/metadata.md)
  An array of metadata items for all metadata identifiers that have a value.
- [var commonMetadata: [AVMetadataItem]](avassettrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avassettrack/availablemetadataformats.md)
  An array of metadata formats available for the track.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avassettrack/metadata(forformat:).md)
  Returns metadata items that a track contains for the specified format.
### Accessing Track Segments
- [var segments: [AVAssetTrackSegment]](avassettrack/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func segment(forTrackTime: CMTime) -> AVAssetTrackSegment?](avassettrack/segment(fortracktime:).md)
  Retrieves a segment with a target time range that contains, or is closest to, the specified track time.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avassettrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.
### Accessing Track Associations
- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](avassettrack/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](avassettrack/associatedtracks(oftype:).md)
  Returns an array of associated tracks that have the specified association type.
### Creating Sample Cursors
- [var canProvideSampleCursors: Bool](avassettrack/canprovidesamplecursors.md)
  A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack-deprecated-symbols)*