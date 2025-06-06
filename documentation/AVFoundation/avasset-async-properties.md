# AVAsset

**Framework**: AVFoundation

Asynchronous properties for assets.

## Topics

### Loading Duration and Timing
- [static var duration: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/duration.md)
  A time value that represents the duration of the asset.
- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](avpartialasyncproperty/tracks-48zyw.md)
  The tracks of media that an asset contains.
### Loading Track Groups
- [static var trackGroups: AVAsyncProperty<Root, [AVAssetTrackGroup]>](avpartialasyncproperty/trackgroups.md)
  The track groups an asset contains.
### Loading Metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](avpartialasyncproperty/commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](avpartialasyncproperty/creationdate.md)
  A metadata item that indicates the creation date of an asset.
- [static var lyrics: AVAsyncProperty<Root, String?>](avpartialasyncproperty/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Loading Suitability
- [static var isPlayable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isplayable-45h5v.md)
  A Boolean value that indicates whether an asset contains playable content.
- [static var isExportable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isexportable.md)
  A Boolean value that indicates whether you can export an asset using an export session.
- [static var isReadable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [static var isComposable: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscomposable.md)
  A Boolean value that indicates whether you can use the asset in a media composition.
- [static var isCompatibleWithSavedPhotosAlbum: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.
- [static var isCompatibleWithAirPlayVideo: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
### Loading Asset Preferences
- [static var preferredRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-80d13.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [static var preferredVolume: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredvolume-20mb3.md)
  The asset’s volume preference for playing its audible media.
- [static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria>](avpartialasyncproperty/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
### Loading Media Selections
- [static var allMediaSelections: AVAsyncProperty<Root, [AVMediaSelection]>](avpartialasyncproperty/allmediaselections.md)
  The available media selections for an asset.
- [static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection>](avpartialasyncproperty/preferredmediaselection.md)
  The default media selections for the media selection groups of an asset.
- [static var availableMediaCharacteristicsWithMediaSelectionOptions: AVAsyncProperty<Root, [AVMediaCharacteristic]>](avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md)
  The media characteristics that provide media selection options.
### Loading Chapter Metadata
- [static var availableChapterLocales: AVAsyncProperty<Root, [Locale]>](avpartialasyncproperty/availablechapterlocales.md)
  The locales of an asset’s chapter metadata.
### Loading Content Protections
- [static var hasProtectedContent: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Loading Fragment Support
- [static var canContainFragments: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [static var containsFragments: AVAsyncProperty<Root, Bool>](avpartialasyncproperty/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [static var overallDurationHint: AVAsyncProperty<Root, CMTime>](avpartialasyncproperty/overalldurationhint.md)
  A hint to the total duration of fragments that currently exist or may exist in the future.

## See Also

- [AVAssetTrack](avassettrack-async-properties.md)
  Asynchronous properties for asset tracks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset-async-properties)*