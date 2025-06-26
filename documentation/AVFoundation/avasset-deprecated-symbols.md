# Deprecated Symbols

**Framework**: AVFoundation

Review unsupported symbols and their replacements.

#### Overview

[`AVAsset`](avasset.md) doesn’t support using its synchronous property accessors that can block the calling thread. Instead, use the [`load(_:isolation:)`](avasynchronouskeyvalueloading/load(_:isolation:).md) method to load [`AVAsyncProperty`](avasyncproperty.md) values asynchronously.

## Topics

### Accessing Duration and Timing
- [var duration: CMTime](avasset/duration.md)
  A time value that indicates the asset’s duration.
- [var providesPreciseDurationAndTiming: Bool](avasset/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [var minimumTimeOffsetFromLive: CMTime](avasset/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Accessing Tracks
- [var tracks: [AVAssetTrack]](avasset/tracks.md)
  The tracks an asset contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVAssetTrack?](avasset/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVAssetTrack]](avasset/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVAssetTrack]](avasset/tracks(withmediacharacteristic:).md)
  Returns an array of asset tracks matching the specified media characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avasset/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.
### Accessing Track Groups
- [var trackGroups: [AVAssetTrackGroup]](avasset/trackgroups.md)
  The track groups an asset contains.
### Accessing Metadata
- [var metadata: [AVMetadataItem]](avasset/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avasset/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avasset/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avasset/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avasset/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avasset/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Accessing Suitability
- [var isPlayable: Bool](avasset/isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isExportable: Bool](avasset/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isReadable: Bool](avasset/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isComposable: Bool](avasset/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithAirPlayVideo: Bool](avasset/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](avasset/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.
### Accessing Asset Preferences
- [var preferredRate: Float](avasset/preferredrate.md)
  The asset’s rate preference for playing its media.
- [var preferredVolume: Float](avasset/preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredTransform: CGAffineTransform](avasset/preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [var preferredDisplayCriteria: AVDisplayCriteria](avasset/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [var preferredMediaSelection: AVMediaSelection](avasset/preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
### Accessing Media Selections
- [var allMediaSelections: [AVMediaSelection]](avasset/allmediaselections.md)
  The array of available media selections for this asset.
- [var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic]](avasset/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.
- [func mediaSelectionGroup(forMediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?](avasset/mediaselectiongroup(formediacharacteristic:).md)
  Returns a media selection group that contains one or more options with the specified media characteristic.
### Accessing Chapter Metadata
- [var availableChapterLocales: [Locale]](avasset/availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [func chapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]](avasset/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Returns an array of chapters that contain the specified title locale and common keys.
- [func chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](avasset/chaptermetadatagroups(bestmatchingpreferredlanguages:).md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.
### Accessing Content Protections
- [var hasProtectedContent: Bool](avasset/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Accessing Fragment Support
- [var canContainFragments: Bool](avasset/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [var containsFragments: Bool](avasset/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [var overallDurationHint: CMTime](avasset/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.
### Inspecting Visual Attributes
- [var naturalSize: CGSize](avasset/naturalsize.md)
  The encoded or authored size of the visual portion of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset-deprecated-symbols)*