# AVMutableMovie

**Framework**: AVFoundation  
**Kind**: class

A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class AVMutableMovie
```

#### Overview

This class is a mutable subclass of [`AVMovie`](avmovie.md) that provides methods that support movie editing. For example, you can use a mutable movie to copy media data from one track and paste it into another. You can also use this object to create track references from one track to another (for example, to set one track as a chapter track of another track). To perform editing operations on individual tracks, use the associated classes [`AVMovieTrack`](avmovietrack.md) and [`AVMutableMovieTrack`](avmutablemovietrack.md).

You use movie objects only when operating on format-specific features of a QuickTime or ISO base media file. You typically don’t use these classes to open and play QuickTime movie files or ISO base media files. Instead, you use [`AVURLAsset`](avurlasset.md) and [`AVPlayerItem`](avplayeritem.md).

When performing media insertions, a movie interleaves media data from tracks in the source asset to optimize the movie file for playback. However, performing a series of media insertions may result in a movie file that’s not optimally interleaved. You can optimize a movie file for playback by exporting it with an [`AVAssetExportSession`](avassetexportsession.md) object using the export preset [`AVAssetExportPresetPassthrough`](avassetexportpresetpassthrough.md), and setting the [`shouldOptimizeForNetworkUse`](avassetexportsession/shouldoptimizefornetworkuse.md) property value to [`true`](https://developer.apple.com/documentation/swift/true).

## Topics

### Creating a Movie
- [init(url: URL, options: [String : Any]?, error: ()) throws](avmutablemovie/init(url:options:error:).md)
  Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [init(data: Data, options: [String : Any]?, error: ()) throws](avmutablemovie/init(data:options:error:).md)
  Creates a mutable movie object from a movie stored in a data object.
- [init(settingsFrom: AVMovie?, options: [String : Any]?) throws](avmutablemovie/init(settingsfrom:options:).md)
  Creates a mutable movie object without tracks.
### Configuring a Movie
- [var isModified: Bool](avmutablemovie/ismodified.md)
  A Boolean value that indicates whether the movie is in a modified state.
- [var timescale: CMTimeScale](avmutablemovie/timescale.md)
  The time scale of the movie.
- [var interleavingPeriod: CMTime](avmutablemovie/interleavingperiod.md)
  A time period indicating the duration for interleaving runs of samples for each track.
- [var defaultMediaDataStorage: AVMediaDataStorage?](avmutablemovie/defaultmediadatastorage.md)
  The default storage container for media data that you add to a movie.
### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVMutableMovieTrack]>](avpartialasyncproperty/tracks-2lj40.md)
  The tracks that a movie contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVMutableMovieTrack?, (any Error)?) -> Void)](avmutablemovie/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](avmutablemovie/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVMutableMovieTrack]?, (any Error)?) -> Void)](avmutablemovie/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Accessing Tracks
- [var tracks: [AVMutableMovieTrack]](avmutablemovie/tracks.md)
  The tracks that a movie contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVMutableMovieTrack?](avmutablemovie/track(withtrackid:).md)
  Retrieves a track in the movie that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediatype:).md)
  Retrieves tracks in the movie that present media of the specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVMutableMovieTrack]](avmutablemovie/tracks(withmediacharacteristic:).md)
  Retrieve tracks in the movie that present media of the specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avmutablemovie/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.
### Accessing Track Groups
- [var trackGroups: [AVAssetTrackGroup]](avmutablemovie/trackgroups.md)
  The track groups an asset contains.
### Managing Tracks
- [func mutableTrack(compatibleWith: AVAssetTrack) -> AVMutableMovieTrack?](avmutablemovie/mutabletrack(compatiblewith:).md)
  Provides a reference to a track from a mutable movie into which you can insert any time range.
- [func addMutableTrack(withMediaType: AVMediaType, copySettingsFrom: AVAssetTrack?, options: [String : Any]?) -> AVMutableMovieTrack?](avmutablemovie/addmutabletrack(withmediatype:copysettingsfrom:options:).md)
  Adds an empty track to the target movie.
- [func addMutableTracksCopyingSettings(from: [AVAssetTrack], options: [String : Any]?) -> [AVMutableMovieTrack]](avmutablemovie/addmutabletrackscopyingsettings(from:options:).md)
  Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [func removeTrack(AVMovieTrack)](avmutablemovie/removetrack(_:).md)
  Removes the specified track from the target movie.
### Managing Time Ranges
- [func insertEmptyTimeRange(CMTimeRange)](avmutablemovie/insertemptytimerange(_:).md)
  Adds an empty time range to a movie.
- [func insertTimeRange(CMTimeRange, of: AVAsset, at: CMTime, copySampleData: Bool) throws](avmutablemovie/inserttimerange(_:of:at:copysampledata:).md)
  Inserts all of the tracks in a specified time range of an asset into a movie.
- [func scale(CMTimeRange, toDuration: CMTime)](avmutablemovie/scale(_:toduration:).md)
  Changes the duration of a time range in a movie.
- [func removeTimeRange(CMTimeRange)](avmutablemovie/removetimerange(_:).md)
  Removes the specified time range from a movie.
### Accessing Duration and Timing
- [var duration: CMTime](avmutablemovie/duration.md)
  A time value that indicates the asset’s duration.
- [var providesPreciseDurationAndTiming: Bool](avmutablemovie/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [var minimumTimeOffsetFromLive: CMTime](avmutablemovie/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Accessing Metadata
- [var metadata: [AVMetadataItem]](avmutablemovie/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avmutablemovie/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avmutablemovie/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avmutablemovie/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avmutablemovie/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avmutablemovie/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Determining Suitability
- [var isPlayable: Bool](avmutablemovie/isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isReadable: Bool](avmutablemovie/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](avmutablemovie/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](avmutablemovie/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithAirPlayVideo: Bool](avmutablemovie/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](avmutablemovie/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.
### Inspecting Preferences
- [var preferredRate: Float](avmutablemovie/preferredrate.md)
  The asset’s rate preference for playing its media.
- [var preferredVolume: Float](avmutablemovie/preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredTransform: CGAffineTransform](avmutablemovie/preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [var preferredMediaSelection: AVMediaSelection](avmutablemovie/preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
### Accessing Media Selections
- [var allMediaSelections: [AVMediaSelection]](avmutablemovie/allmediaselections.md)
  The array of available media selections for this asset.
- [var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic]](avmutablemovie/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.
- [func mediaSelectionGroup(forMediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?](avmutablemovie/mediaselectiongroup(formediacharacteristic:).md)
  Returns a media selection group that contains one or more options with the specified media characteristic.
### Accessing Chapter Metadata
- [var availableChapterLocales: [Locale]](avmutablemovie/availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [func chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](avmutablemovie/chaptermetadatagroups(bestmatchingpreferredlanguages:).md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.
- [func chapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]](avmutablemovie/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Returns an array of chapters that contain the specified title locale and common keys.
### Determining Content Protections
- [var hasProtectedContent: Bool](avmutablemovie/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Determining Fragment Support
- [var canContainFragments: Bool](avmutablemovie/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [var containsFragments: Bool](avmutablemovie/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [var overallDurationHint: CMTime](avmutablemovie/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.

## Relationships

### Inherits From
- [AVMovie](avmovie.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVMutableMovieTrack](avmutablemovietrack.md)
  A mutable track that conforms to the QuickTime or ISO base media file format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie)*