# AVComposition

**Framework**: AVFoundation  
**Kind**: class

An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.

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
class AVComposition
```

#### Overview

A composition is a container for one or more tracks of media. Its tracks are instances of [`AVCompositionTrack`](avcompositiontrack.md) that present media of a uniform type like audio or video. A track itself is a container for one or more segments of media, which are instances of [`AVCompositionTrackSegment`](avcompositiontracksegment.md), a type that represents a region of media in the source track.

## Topics

### Loading Tracks
- [static var tracks: AVAsyncProperty<Root, [AVCompositionTrack]>](avpartialasyncproperty/tracks-9eows.md)
  The tracks that a composition contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVCompositionTrack?, (any Error)?) -> Void)](avcomposition/loadtrack(withtrackid:completionhandler:).md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVCompositionTrack]?, (any Error)?) -> Void)](avcomposition/loadtracks(withmediatype:completionhandler:).md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVCompositionTrack]?, (any Error)?) -> Void)](avcomposition/loadtracks(withmediacharacteristic:completionhandler:).md)
  Loads tracks that contain media of a specified characteristic.
### Accessing Tracks
- [var tracks: [AVCompositionTrack]](avcomposition/tracks.md)
  The tracks that a composition contains.
- [func track(withTrackID: CMPersistentTrackID) -> AVCompositionTrack?](avcomposition/track(withtrackid:).md)
  Returns a track that contains the specified identifier.
- [func tracks(withMediaType: AVMediaType) -> [AVCompositionTrack]](avcomposition/tracks(withmediatype:).md)
  Returns tracks that contain media of a specified type.
- [func tracks(withMediaCharacteristic: AVMediaCharacteristic) -> [AVCompositionTrack]](avcomposition/tracks(withmediacharacteristic:).md)
  Returns tracks that contain media of a specified characteristic.
- [func unusedTrackID() -> CMPersistentTrackID](avcomposition/unusedtrackid.md)
  Returns an identifier that no other tracks in the asset use.
### Accessing Track Groups
- [var trackGroups: [AVAssetTrackGroup]](avcomposition/trackgroups.md)
  The track groups an asset contains.
### Accessing Duration and Timing
- [var duration: CMTime](avcomposition/duration.md)
  A time value that indicates the asset’s duration.
- [var providesPreciseDurationAndTiming: Bool](avcomposition/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [var minimumTimeOffsetFromLive: CMTime](avcomposition/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Accessing Metadata
- [var metadata: [AVMetadataItem]](avcomposition/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [var commonMetadata: [AVMetadataItem]](avcomposition/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [var availableMetadataFormats: [AVMetadataFormat]](avcomposition/availablemetadataformats.md)
  The metadata formats this asset contains.
- [func metadata(forFormat: AVMetadataFormat) -> [AVMetadataItem]](avcomposition/metadata(forformat:).md)
  Returns an array of metadata items from the container with the specified format.
- [var creationDate: AVMetadataItem?](avcomposition/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [var lyrics: String?](avcomposition/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Determining Suitability
- [var isPlayable: Bool](avcomposition/isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [var isReadable: Bool](avcomposition/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [var isExportable: Bool](avcomposition/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [var isComposable: Bool](avcomposition/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [var isCompatibleWithAirPlayVideo: Bool](avcomposition/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [var isCompatibleWithSavedPhotosAlbum: Bool](avcomposition/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the composition to the Saved Photos album.
### Inspecting Preferences
- [var preferredRate: Float](avcomposition/preferredrate.md)
  The asset’s rate preference for playing its media.
- [var preferredVolume: Float](avcomposition/preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredTransform: CGAffineTransform](avcomposition/preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [var preferredMediaSelection: AVMediaSelection](avcomposition/preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
- [var preferredDisplayCriteria: AVDisplayCriteria](avcomposition/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
### Accessing Media Selections
- [var allMediaSelections: [AVMediaSelection]](avcomposition/allmediaselections.md)
  The array of available media selections for this asset.
- [var availableMediaCharacteristicsWithMediaSelectionOptions: [AVMediaCharacteristic]](avcomposition/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.
- [func mediaSelectionGroup(forMediaCharacteristic: AVMediaCharacteristic) -> AVMediaSelectionGroup?](avcomposition/mediaselectiongroup(formediacharacteristic:).md)
  Returns a media selection group that contains one or more options with the specified media characteristic.
### Accessing Chapter Metadata
- [var availableChapterLocales: [Locale]](avcomposition/availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [func chapterMetadataGroups(bestMatchingPreferredLanguages: [String]) -> [AVTimedMetadataGroup]](avcomposition/chaptermetadatagroups(bestmatchingpreferredlanguages:).md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.
- [func chapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]?) -> [AVTimedMetadataGroup]](avcomposition/chaptermetadatagroups(withtitlelocale:containingitemswithcommonkeys:).md)
  Returns an array of chapters that contain the specified title locale and common keys.
### Accessing Visual Dimensions
- [var naturalSize: CGSize](avcomposition/naturalsize.md)
  The authored size of the visual portion of the composition.
### Accessing Initialization Options
- [var urlAssetInitializationOptions: [String : Any]](avcomposition/urlassetinitializationoptions.md)
  The options you used to create a composition.
### Determining Content Protections
- [var hasProtectedContent: Bool](avcomposition/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Determining Fragment Support
- [var canContainFragments: Bool](avcomposition/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [var containsFragments: Bool](avcomposition/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [var overallDurationHint: CMTime](avcomposition/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.

## Relationships

### Inherits From
- [AVAsset](avasset.md)
### Inherited By
- [AVMutableComposition](avmutablecomposition.md)
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

- [class AVCompositionTrack](avcompositiontrack.md)
  A track in a composition that presents media of a uniform type.
- [class AVCompositionTrackSegment](avcompositiontracksegment.md)
  A track segment that maps a time from the source media track to the composition track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition)*