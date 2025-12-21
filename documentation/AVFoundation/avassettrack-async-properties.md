# AVAssetTrack

**Framework**: AVFoundation

Asynchronous properties for asset tracks.

## Topics

### Loading track information
- [static var totalSampleDataLength: AVAsyncProperty<Root, Int64>](avpartialasyncproperty/totalsampledatalength.md)
  The total number of bytes of sample data the track requires.
- [static var formatDescriptions: AVAsyncProperty<Root, [CMFormatDescription]>](avpartialasyncproperty/formatdescriptions.md)
  The format descriptions of the media samples that a track references.
- [static var isDecodable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isdecodable.md)
  A Boolean value that indicates whether the track is decodable in the current environment.
- [static var isEnabled: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isenabled.md)
  A Boolean value that indicates whether the track is in an enabled state.
- [static var isPlayable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isplayable-6txa5.md)
  A Boolean value that indicates whether the track is playable in the current environment.
- [static var mediaCharacteristics: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/mediacharacteristics.md)
  The media characteristics for the track.
- [static var isSelfContained: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isselfcontained.md)
  A Boolean value that indicates whether the track references sample data only within its container file.
### Loading temporal information
- [static var timeRange: AVAsyncProperty<Root, CMTimeRange>](avpartialasyncproperty/timerange.md)
  The time range of the track within the overall timeline of the asset.
- [static var naturalTimeScale: AVAsyncProperty<Root, CMTimeScale>](avpartialasyncproperty/naturaltimescale.md)
  The natural time scale of the media that a track references.
- [static var estimatedDataRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/estimateddatarate.md)
  The estimated data rate, in bits per second, of the media that the track references.
### Loading language support
- [static var languageCode: AVAsyncProperty<Root, String?>](avpartialasyncproperty/languagecode.md)
  The language code of the track.
- [static var extendedLanguageTag: AVAsyncProperty<Root, String?>](avpartialasyncproperty/extendedlanguagetag.md)
  The language tag of the track.
### Loading visual characteristics
- [static var naturalSize: AVAsyncProperty<Root, CGSize>](avpartialasyncproperty/naturalsize.md)
  The natural dimensions of the media data that the track references.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-90jdn.md)
  The track’s transform preference to apply to its visual content during presentation or processing.
### Loading audible characteristics
- [static var preferredVolume: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredvolume-8q2yt.md)
  The track’s volume preference for playing its audible media.
- [static var hasAudioSampleDependencies: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/hasaudiosampledependencies.md)
  A Boolean value that indicates whether the track has sample dependencies.
### Loading frame-based characteristics
- [static var nominalFrameRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/nominalframerate.md)
  The frame rate of the track, in frames per second.
- [static var minFrameDuration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minframeduration.md)
  The minimum duration of the track’s frames.
- [static var requiresFrameReordering: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/requiresframereordering.md)
  A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.
### Loading metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-6e14c.md)
  An array of metadata items for all metadata identifiers that have a value.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-5p9xg.md)
  An array of metadata formats available for the track.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-73m58.md)
  An array of metadata items for all common metadata keys that have a value.
### Loading track segments
- [static var segments: AVAsyncProperty<Root, [AVAssetTrackSegment]>](avpartialasyncproperty/segments.md)
  The time mappings from the track’s media samples to its timeline.
### Loading track associations
- [static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]>](avpartialasyncproperty/availabletrackassociationtypes.md)
  An array of association types that the track uses to associate with other tracks.
### Creating sample cursors
- [static var canProvideSampleCursors: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/canprovidesamplecursors.md)
  A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## See Also

- [AVAsset](avasset-async-properties.md)
  Asynchronous properties for assets.
- [AVURLAsset](avurlasset-async-properties.md)
  Asynchronous properties for URL assets.
- [AVFragmentedAsset](avfragmentedasset-async-properties.md)
  Asynchronous properties for fragmented assets.
- [AVMetadataItem](avmetadataitem-async-properties.md)
  Asynchronous properties for metadata items.
- [AVComposition](avcomposition-async-properties.md)
  Asynchronous properties for compositions.
- [AVMutableComposition](avmutablecomposition-async-properties.md)
  Asynchronous properties for mutable compositions.
- [AVMovie](avmovie-async-properties.md)
  Asynchronous properties for movies.
- [AVMutableMovie](avmutablemovie-async-properties.md)
  Asynchronous properties for mutable movies.
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md)
  Asynchronous properties for fragmented movies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack-async-properties)*