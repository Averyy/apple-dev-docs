# AVMutableMovieTrack

**Framework**: AVFoundation  
**Kind**: class

A mutable track that conforms to the QuickTime or ISO base media file format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVMutableMovieTrack
```

## Topics

### Managing time ranges
- [func insertTimeRange(CMTimeRange, of: AVAssetTrack, at: CMTime, copySampleData: Bool) throws](avmutablemovietrack/inserttimerange(_:of:at:copysampledata:).md)
  Inserts a portion of an asset track into the target movie.
- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovietrack/insertemptytimerange(_:).md)
  Adds an empty time range to a track.
- [func removeTimeRange(CMTimeRange)](avmutablemovietrack/removetimerange(_:).md)
  Removes the specified time range from a track.
- [func scaleTimeRange(CMTimeRange, toDuration: CMTime)](avmutablemovietrack/scaletimerange(_:toduration:).md)
  Changes the duration of a time range in a track.
### Appending sample data
- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> (decodeTime: CMTime, presentationTime: CMTime)](avmutablemovietrack/append(_:).md)
  Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [func append(CMSampleBuffer, decodeTime: UnsafeMutablePointer<CMTime>?, presentationTime: UnsafeMutablePointer<CMTime>?) throws](avmutablemovietrack/append(_:decodetime:presentationtime:).md)
  Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [func insertMediaTimeRange(CMTimeRange, into: CMTimeRange) -> Bool](avmutablemovietrack/insertmediatimerange(_:into:).md)
  Inserts a reference to a media time range into a track.
### Accessing media chunks
- [var preferredMediaChunkAlignment: Int](avmutablemovietrack/preferredmediachunkalignment.md)
  The boundary for media chunk alignment for file types that support media chunk alignment.
- [var preferredMediaChunkDuration: CMTime](avmutablemovietrack/preferredmediachunkduration.md)
  The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.
- [var preferredMediaChunkSize: Int](avmutablemovietrack/preferredmediachunksize.md)
  The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.
### Changing format descriptions
- [var formatDescriptions: [Any]](avmutablemovietrack/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [func replaceFormatDescription(CMFormatDescription, with: CMFormatDescription)](avmutablemovietrack/replaceformatdescription(_:with:).md)
  Replaces the track’s format description with a new format description.
### Configuring track information
- [var isModified: Bool](avmutablemovietrack/ismodified.md)
  A Boolean value that indicates whether a track is in a modified state.
- [var alternateGroupID: Int](avmutablemovietrack/alternategroupid.md)
  A number that identifies the track as a member of a particular alternate group.
- [var mediaDataStorage: AVMediaDataStorage?](avmutablemovietrack/mediadatastorage.md)
  A storage container for the media data to be added to a track.
- [var sampleReferenceBaseURL: URL?](avmutablemovietrack/samplereferencebaseurl.md)
  The base URL for sample references.
### Accessing track information
- [var isPlayable: Bool](avmutablemovietrack/isplayable.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [var isDecodable: Bool](avmutablemovietrack/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [var isEnabled: Bool](avmutablemovietrack/isenabled.md)
  A Boolean value that indicates whether the track’s container enables it.
- [var isSelfContained: Bool](avmutablemovietrack/isselfcontained.md)
  A Boolean value that indicates whether this track references sample data only within its container file.
- [var hasProtectedContent: Bool](avmutablemovietrack/hasprotectedcontent.md)
  A Boolean value that indicates whether a track contains protected content.
- [var totalSampleDataLength: Int64](avmutablemovietrack/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [func hasMediaCharacteristic(AVMediaCharacteristic) -> Bool](avmutablemovietrack/hasmediacharacteristic(_:).md)
  Returns a Boolean value that indicates whether the track references media with the specified media characteristic.
### Accessing temporal information
- [var timeRange: CMTimeRange](avmutablemovietrack/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [var timescale: CMTimeScale](avmutablemovietrack/timescale.md)
  The time scale for tracks that contain the `moov` atom.
- [var naturalTimeScale: CMTimeScale](avmutablemovietrack/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [var estimatedDataRate: Float](avmutablemovietrack/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
- [func samplePresentationTime(forTrackTime: CMTime) -> CMTime](avmutablemovietrack/samplepresentationtime(fortracktime:).md)
  Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.
### Accessing language support
- [var languageCode: String?](avmutablemovietrack/languagecode.md)
  The language code of the track.
- [var extendedLanguageTag: String?](avmutablemovietrack/extendedlanguagetag.md)
  The language tag of the track.
### Accessing visual characteristics
- [var naturalSize: CGSize](avmutablemovietrack/naturalsize.md)
  The dimensions used to display the visual media data for the track.
- [var preferredTransform: CGAffineTransform](avmutablemovietrack/preferredtransform.md)
  The transform performed on the visual media data of the track for display purposes.
- [var layer: Int](avmutablemovietrack/layer.md)
  The layer level for the visual media of the track.
- [var cleanApertureDimensions: CGSize](avmutablemovietrack/cleanaperturedimensions.md)
  The clean aperture dimension of the track.
- [var productionApertureDimensions: CGSize](avmutablemovietrack/productionaperturedimensions.md)
  The production aperture dimensions of the track.
- [var encodedPixelsDimensions: CGSize](avmutablemovietrack/encodedpixelsdimensions.md)
  The encoded pixels dimensions of the track.
### Accessing audible characteristics
- [var preferredVolume: Float](avmutablemovietrack/preferredvolume.md)
  The preferred volume for the audible medata data of the track.
- [var hasAudioSampleDependencies: Bool](avmutablemovietrack/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.
### Accessing frame-based characteristics
- [var nominalFrameRate: Float](avmutablemovietrack/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [var minFrameDuration: CMTime](avmutablemovietrack/minframeduration.md)
  The minimum duration of the track’s frames.
- [var requiresFrameReordering: Bool](avmutablemovietrack/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
### Accessing metadata
- [var metadata: [AVMetadataItem]](avmutablemovietrack/metadata.md)
  An array of metadata stored by the track.
- [var commonMetadata: [AVMetadataItem]](avmutablemovietrack/commonmetadata.md)
  An array of metadata items for all common metadata keys that have a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovietrack/availablemetadataformats.md)
  An array of metadata formats available for the track.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovietrack/metadata(forformat:).md)
  Returns metadata items that a track contains for the specified format.
### Accessing track segments
- [var segments: [AVAssetTrackSegment]](avmutablemovietrack/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func segment(forTrackTime: CMTime) -> AVAssetTrackSegment?](avmutablemovietrack/segment(fortracktime:).md)
  Returns a segment whose target time range contains, or is closest to, the specified track time.
### Managing track associations
- [var availableTrackAssociationTypes: [AVAssetTrack.AssociationType]](avmutablemovietrack/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func associatedTracks(ofType: AVAssetTrack.AssociationType) -> [AVAssetTrack]](avmutablemovietrack/associatedtracks(oftype:).md)
  Returns an array of associated tracks that have the specified association type.
- [func addTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](avmutablemovietrack/addtrackassociation(to:type:).md)
  Creates a specific type of track association between two tracks.
- [func removeTrackAssociation(to: AVMovieTrack, type: AVAssetTrack.AssociationType)](avmutablemovietrack/removetrackassociation(to:type:).md)
  Removes a specific type of track association between two tracks.
### Determining sample cursor support
- [var canProvideSampleCursors: Bool](avmutablemovietrack/canprovidesamplecursors.md)
  A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## Relationships

### Inherits From
- [AVMovieTrack](avmovietrack.md)
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

- [class AVMutableMovie](avmutablemovie.md)
  A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack)*