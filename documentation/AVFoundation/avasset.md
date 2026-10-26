# AVAsset

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that models timed audiovisual media.

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
class AVAsset
```

```objc
@interface AVAsset : NSObject
```

## Mentions

- [Loading media data asynchronously](./loading-media-data-asynchronously.md)
- [Controlling the transport behavior of a player](./controlling-the-transport-behavior-of-a-player.md)
- [Exporting video to alternative formats](./exporting-video-to-alternative-formats.md)
- [Implementing simple enhanced buffering for your content](./implementing-simple-enhanced-buffering-for-your-content.md)
- [Retrieving media metadata](./retrieving-media-metadata.md)

#### Overview

An asset models file-based media like a QuickTime movie or an MP3 audio file, and also media streamed using HTTP Live Streaming (HLS). An asset is a container object for one or more instances of [`AVAssetTrack`](./avassettrack.md) that model the uniformly typed tracks of media. The most commonly used track types are audio and video, but assets may also contain supplementary tracks, like closed captions, subtitles, and timed metadata.

![A diagram of four rectangular items. The rectangle on the left represents AVAsset. A line connects it to three stacked rectangles on the right that represent AVAssetTrack (Video), AVAssetTrack (Audio), and AVAssetTrack (Subtitles) from top to bottom.](https://developer.apple.com/tutorials/images/com.apple.avfoundation/media-3845943@2x.png)

You load the tracks for an asset by asynchronously loading its [`tracks`](./avpartialasyncproperty/tracks-48zyw.md) property. In some cases, you may want to perform operations on a subset of an asset’s tracks rather than on its complete collection. For those situations, an asset provides methods to retrieve subsets of tracks according to particular criteria, such as identifier, media type, or characteristic.

## Topics

### Creating an asset
- [convenience init(url: URL)](./avasset/init%28url%29-42gl8.md)
  Creates an asset that models the media at the specified URL.
### Loading duration and timing
- [static var duration: AVAsyncProperty<Root, CMTime>](./avpartialasyncproperty/duration.md)
  A time value that represents the duration of the asset.
- [static var providesPreciseDurationAndTiming: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [static var minimumTimeOffsetFromLive: AVAsyncProperty<Root, CMTime>](./avpartialasyncproperty/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Loading tracks
- [static var tracks: AVAsyncProperty<Root, [AVAssetTrack]>](./avpartialasyncproperty/tracks-48zyw.md)
  The tracks of media that an asset contains.
- [func loadTrack(withTrackID: CMPersistentTrackID, completionHandler: (AVAssetTrack?, (any Error)?) -> Void)](./avasset/loadtrack%28withtrackid,completionhandler%29.md)
  Loads a track that contains the specified identifier.
- [func loadTracks(withMediaType: AVMediaType, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](./avasset/loadtracks%28withmediatype,completionhandler%29.md)
  Loads tracks that contain media of a specified type.
- [func loadTracks(withMediaCharacteristic: AVMediaCharacteristic, completionHandler: ([AVAssetTrack]?, (any Error)?) -> Void)](./avasset/loadtracks%28withmediacharacteristic,completionhandler%29.md)
  Loads tracks that contain media of a specified characteristic.
- [func findUnusedTrackID(completionHandler: (CMPersistentTrackID, (any Error)?) -> Void)](./avasset/findunusedtrackid%28completionhandler%29.md)
  Loads an identifier that no other track in the asset uses.
### Loading track groups
- [static var trackGroups: AVAsyncProperty<Root, [AVAssetTrackGroup]>](./avpartialasyncproperty/trackgroups.md)
  The track groups an asset contains.
### Loading metadata
- [static var metadata: AVAsyncProperty<Root, [AVMetadataItem]>](./avpartialasyncproperty/metadata-16qej.md)
  The metadata items that an asset contains for all metadata identifiers.
- [static var commonMetadata: AVAsyncProperty<Root, [AVMetadataItem]>](./avpartialasyncproperty/commonmetadata-3j3n4.md)
  The metadata items that an asset contains for common metadata identifiers.
- [static var availableMetadataFormats: AVAsyncProperty<Root, [AVMetadataFormat]>](./avpartialasyncproperty/availablemetadataformats-4yiq8.md)
  The formats of metadata that an asset contains.
- [func loadMetadata(for: AVMetadataFormat, completionHandler: ([AVMetadataItem]?, (any Error)?) -> Void)](./avasset/loadmetadata%28for,completionhandler%29.md)
  Loads an array of metadata items that the asset contains for the specified format.
- [static var creationDate: AVAsyncProperty<Root, AVMetadataItem?>](./avpartialasyncproperty/creationdate.md)
  A metadata item that indicates the creation date of an asset.
- [static var lyrics: AVAsyncProperty<Root, String?>](./avpartialasyncproperty/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Loading suitability
- [static var isPlayable: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/isplayable-45h5v.md)
  A Boolean value that indicates whether an asset contains playable content.
- [static var isExportable: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/isexportable.md)
  A Boolean value that indicates whether you can export an asset using an export session.
- [static var isReadable: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [static var isComposable: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/iscomposable.md)
  A Boolean value that indicates whether you can use the asset in a media composition.
- [static var isCompatibleWithAirPlayVideo: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [static var isCompatibleWithSavedPhotosAlbum: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.
### Loading asset preferences
- [static var preferredRate: AVAsyncProperty<Root, Float>](./avpartialasyncproperty/preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredVolume: AVAsyncProperty<Root, Float>](./avpartialasyncproperty/preferredvolume-20mb3.md)
  The asset’s volume preference for playing its audible media.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](./avpartialasyncproperty/preferredtransform-80d13.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria>](./avpartialasyncproperty/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [class AVDisplayCriteria](./avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.
### Loading media selections
- [static var allMediaSelections: AVAsyncProperty<Root, [AVMediaSelection]>](./avpartialasyncproperty/allmediaselections.md)
  The available media selections for an asset.
- [static var preferredMediaSelection: AVAsyncProperty<Root, AVMediaSelection>](./avpartialasyncproperty/preferredmediaselection.md)
  The default media selections for the media selection groups of an asset.
- [static var availableMediaCharacteristicsWithMediaSelectionOptions: AVAsyncProperty<Root, [AVMediaCharacteristic]>](./avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md)
  The media characteristics that provide media selection options.
- [func loadMediaSelectionGroup(for: AVMediaCharacteristic, completionHandler: (AVMediaSelectionGroup?, (any Error)?) -> Void)](./avasset/loadmediaselectiongroup%28for,completionhandler%29.md)
  Loads a media selection group that contains one or more options with the specified media characteristic.
### Loading chapter metadata
- [static var availableChapterLocales: AVAsyncProperty<Root, [Locale]>](./avpartialasyncproperty/availablechapterlocales.md)
  The locales of an asset’s chapter metadata.
- [func loadChapterMetadataGroups(withTitleLocale: Locale, containingItemsWithCommonKeys: [AVMetadataKey]) async throws -> [AVTimedMetadataGroup]](./avasset/loadchaptermetadatagroups%28withtitlelocale,containingitemswithcommonkeys%29.md)
  Loads chapter metadata that contains the specified title locale and common keys.
- [func loadChapterMetadataGroups(bestMatchingPreferredLanguages: [String], completionHandler: ([AVTimedMetadataGroup]?, (any Error)?) -> Void)](./avasset/loadchaptermetadatagroups%28bestmatchingpreferredlanguages,completionhandler%29.md)
  Loads chapter metadata with a locale that best matches the list of preferred languages.
- [- loadChapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:completionHandler:](./avasset/loadchaptermetadatagroupswithtitlelocale_containingitemswithcommonkeys_completionhandler_.md)
  Loads chapter metadata that contains the specified title locale and common keys.
### Loading content protections
- [static var hasProtectedContent: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Loading fragment support
- [static var canContainFragments: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [static var containsFragments: AVAsyncProperty<Root, Bool>](./avpartialasyncproperty/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [static var overallDurationHint: AVAsyncProperty<Root, CMTime>](./avpartialasyncproperty/overalldurationhint.md)
  A hint to the total duration of fragments that currently exist or may exist in the future.
### Canceling property loading
- [func cancelLoading()](./avasset/cancelloading%28%29.md)
  Cancels all pending requests to asynchronously load property values.
### Retrieving reference restrictions
- [var referenceRestrictions: AVAssetReferenceRestrictions](./avasset/referencerestrictions.md)
  The restrictions that an asset places on how it resolves references to external media.
- [struct AVAssetReferenceRestrictions](./avassetreferencerestrictions.md)
  Restrictions to use when resolving references to external media data.
### Deprecated
- [Deprecated symbols](./avasset-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Initializers
- [convenience init(URL: URL)](./avasset/init%28url%29-8cql6.md)
### Accessing duration and timing
- [duration](./avasset/duration.md)
  A time value that indicates the asset’s duration.
- [providesPreciseDurationAndTiming](./avasset/providesprecisedurationandtiming.md)
  A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](./avasset/minimumtimeoffsetfromlive.md)
  A time value that indicates how closely playback follows the latest live stream content.
### Accessing tracks
- [tracks](./avasset/tracks.md)
  The tracks an asset contains.
- [- trackWithTrackID:](./avasset/track%28withtrackid%29.md)
  Returns a track that contains the specified identifier.
- [- tracksWithMediaType:](./avasset/tracks%28withmediatype%29.md)
  Returns tracks that contain media of a specified type.
- [- tracksWithMediaCharacteristic:](./avasset/tracks%28withmediacharacteristic%29.md)
  Returns an array of asset tracks matching the specified media characteristic.
- [- unusedTrackID](./avasset/unusedtrackid%28%29.md)
  Returns an identifier that no other tracks in the asset use.
### Accessing track groups
- [trackGroups](./avasset/trackgroups.md)
  The track groups an asset contains.
### Accessing metadata
- [metadata](./avasset/metadata.md)
  An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](./avasset/commonmetadata.md)
  The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](./avasset/availablemetadataformats.md)
  The metadata formats this asset contains.
- [- metadataForFormat:](./avasset/metadata%28forformat%29.md)
  Returns an array of metadata items from the container with the specified format.
- [creationDate](./avasset/creationdate.md)
  A metadata item that indicates the asset’s creation date.
- [lyrics](./avasset/lyrics.md)
  The lyrics of the asset in a language suitable for the current locale.
### Accessing suitability
- [playable](./avasset/isplayable.md)
  A Boolean value that indicates whether the asset has playable content.
- [exportable](./avasset/isexportable.md)
  A Boolean value that indicates whether you can export this asset using an export session.
- [readable](./avasset/isreadable.md)
  A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [composable](./avasset/iscomposable.md)
  A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [compatibleWithAirPlayVideo](./avasset/iscompatiblewithairplayvideo.md)
  A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [compatibleWithSavedPhotosAlbum](./avasset/iscompatiblewithsavedphotosalbum.md)
  A Boolean value that indicates whether you can write the asset to the Saved Photos album.
### Accessing asset preferences
- [preferredRate](./avasset/preferredrate.md)
  The asset’s rate preference for playing its media.
- [preferredVolume](./avasset/preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [preferredTransform](./avasset/preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](./avasset/preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](./avasset/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
### Accessing media selections
- [allMediaSelections](./avasset/allmediaselections.md)
  The array of available media selections for this asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](./avasset/availablemediacharacteristicswithmediaselectionoptions.md)
  An array of media characteristics for which a media selection option is available.
- [- mediaSelectionGroupForMediaCharacteristic:](./avasset/mediaselectiongroup%28formediacharacteristic%29.md)
  Returns a media selection group that contains one or more options with the specified media characteristic.
### Accessing chapter metadata
- [availableChapterLocales](./avasset/availablechapterlocales.md)
  The locales of the asset’s chapter metadata.
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](./avasset/chaptermetadatagroups%28withtitlelocale,containingitemswithcommonkeys%29.md)
  Returns an array of chapters that contain the specified title locale and common keys.
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](./avasset/chaptermetadatagroups%28bestmatchingpreferredlanguages%29.md)
  Returns an array of chapters with a locale that best matches the list of preferred languages.
### Accessing content protections
- [hasProtectedContent](./avasset/hasprotectedcontent.md)
  A Boolean value that indicates whether the asset contains protected content.
### Accessing fragment support
- [canContainFragments](./avasset/cancontainfragments.md)
  A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](./avasset/containsfragments.md)
  A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](./avasset/overalldurationhint.md)
  The total duration of fragments that currently exist, or may exist in the future.
### Inspecting visual attributes
- [naturalSize](./avasset/naturalsize.md)
  The encoded or authored size of the visual portion of the asset.
### Instance Properties
- [constituentFileURLs](./avasset/constituentfileurls.md)
  The list of file URLs that collectively represent the media asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVComposition](./avcomposition.md)
- [AVMovie](./avmovie.md)
- [AVURLAsset](./avurlasset.md)
### Conforms To
- [AVAsynchronousKeyValueLoading](./avasynchronouskeyvalueloading.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Assets
- [class AVURLAsset](./avurlasset.md)
  An asset that represents media at a local or remote URL.
- [class AVAssetTrack](./avassettrack.md)
  An object that models a track of media that an asset contains.
- [class AVAssetTrackSegment](./avassettracksegment.md)
  An object that represents a time range segment of an asset track.
- [class AVAssetTrackGroup](./avassettrackgroup.md)
  A group of related tracks in an asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset)*