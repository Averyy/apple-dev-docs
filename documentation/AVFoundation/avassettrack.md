# AVAssetTrack

**Framework**: AVFoundation  
**Kind**: class

An object that models a track of media that an asset contains.

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
class AVAssetTrack
```

## Mentions

- [Loading media data asynchronously](loading-media-data-asynchronously.md)
- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)

#### Overview

An asset contains one or more tracks of media that the framework models using the [`AVAssetTrack`](avassettrack.md) class. A track object holds the uniformly typed media that an asset provides such as audio, video, or closed captions.

A track, like its containing [`AVAsset`](avasset.md), doesn’t load all of its media upon creation. Instead, it defers loading its data until you perform an operation that requires it. Because loading the data can take time, an asset track adopts the [`AVAsynchronousKeyValueLoading`](avasynchronouskeyvalueloading.md) protocol so you can load its property values asynchronously by calling the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method.

## Topics

### Identifying an Asset Track
- [var trackID: CMPersistentTrackID](avassettrack/trackid.md)
  The persistent unique identifier for this track.
- [var mediaType: AVMediaType](avassettrack/mediatype.md)
  The type of media that a track presents.
- [var asset: AVAsset?](avassettrack/asset.md)
  The asset object that contains this track.
### Loading Track Information
- [static var formatDescriptions: AVAsyncProperty<Root, [CMFormatDescription]>](avpartialasyncproperty/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [static var isPlayable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isplayable-6txa5.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [static var isDecodable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [static var isEnabled: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isenabled.md)
  A Boolean value that indicates whether the track is in an enabled state.
- [static var isSelfContained: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isselfcontained.md)
  A Boolean value that indicates whether the track references sample data only within its container file.
- [static var totalSampleDataLength: AVAsyncProperty<Root, Int64>](avpartialasyncproperty/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [static var mediaCharacteristics: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/mediacharacteristics.md)
  The media characteristics for the track.
### Loading Temporal Information
- [static var timeRange: AVAsyncProperty<Root, CMTimeRange>](avpartialasyncproperty/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [static var naturalTimeScale: AVAsyncProperty<Root, CMTimeScale>](avpartialasyncproperty/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [static var estimatedDataRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
### Loading Language Support
- [static var languageCode: AVAsyncProperty<Root, String?>](avpartialasyncproperty/languagecode.md)
  The language code of the track.
- [static var extendedLanguageTag: AVAsyncProperty<Root, String?>](avpartialasyncproperty/extendedlanguagetag.md)
  The language tag of the track.
### Loading Visual Characteristics
- [static var naturalSize: AVAsyncProperty<Root, CGSize>](avpartialasyncproperty/naturalsize.md)
  The natural dimensions of the media data that the track references.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-90jdn.md)
  The track’s transform preference to apply to its visual content during presentation or processing.
### Loading Audible Characteristics
- [static var preferredVolume: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredvolume-8q2yt.md)
  The track’s volume preference for playing its audible media.
- [static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.
### Loading Frame-Based Characteristics
- [static var nominalFrameRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [static var minFrameDuration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minframeduration.md)
  The minimum duration of the track’s frames.
- [static var requiresFrameReordering: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
### Loading Metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-6e14c.md)
  An array of metadata items for all metadata identifiers that have a value.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-73m58.md)
  An array of metadata items for all common metadata keys that have a value.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-5p9xg.md)
  An array of metadata formats available for the track.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](avassettrack/loadmetadata(for:completionhandler:).md)
  Loads metadata items that a track contains for the specified format.
### Loading Track Segments
- [static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]>](avpartialasyncproperty/segments.md)
  The time mappings from the track’s media samples to its timeline.
- [func loadSegment(forTrackTime: CMTime, completionHandler: (AVAssetTrackSegment?, (any Error)?) -> Void)](avassettrack/loadsegment(fortracktime:completionhandler:).md)
  Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [func loadSamplePresentationTime(forTrackTime: CMTime, completionHandler: (CMTime, (any Error)?) -> Void)](avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:).md)
  Loads a sample presentation time that maps to the specified track time.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.
### Loading Track Associations
- [static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]>](avpartialasyncproperty/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
- [func loadAssociatedTracks(ofType: AVAssetTrack.AssociationType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](avassettrack/loadassociatedtracks(oftype:completionhandler:).md)
  Loads associated tracks that have the specified association type.
### Creating Sample Cursors
- [func makeSampleCursor(presentationTimeStamp: CMTime) -> AVSampleCursor?](avassettrack/makesamplecursor(presentationtimestamp:).md)
  Creates a sample cursor and positions it at or near the specified presentation timestamp.
- [func makeSampleCursorAtFirstSampleInDecodeOrder() -> AVSampleCursor?](avassettrack/makesamplecursoratfirstsampleindecodeorder.md)
  Creates a sample cursor and positions it at the track’s first media sample in decode order.
- [func makeSampleCursorAtLastSampleInDecodeOrder() -> AVSampleCursor?](avassettrack/makesamplecursoratlastsampleindecodeorder.md)
  Creates a sample cursor and positions it at the track’s last media sample in decode order.
### Deprecated
- [Deprecated Symbols](avassettrack-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVCompositionTrack](avcompositiontrack.md)
- [AVFragmentedAssetTrack](avfragmentedassettrack.md)
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

- [class AVAsset](avasset.md)
  An object that models timed audiovisual media.
- [class AVURLAsset](avurlasset.md)
  An asset that represents media at a local or remote URL.
- [class AVAssetTrackSegment](avassettracksegment.md)
  An object that represents a time range segment of an asset track.
- [class AVAssetTrackGroup](avassettrackgroup.md)
  A group of related tracks in an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack)*