# MPNowPlayingInfoCenter

**Framework**: Media Player  
**Kind**: class

An object for setting the Now Playing information for media that your app plays.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPNowPlayingInfoCenter
```

## Mentions

- [Providing animated artwork for media items](providing-animated-artwork-for-media-items.md)

#### Overview

If your app also provides Now Playing information containing information about the current track, use this object to update that information at appropriate times. This object contains a [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) dictionary describing the playing item.

> ❗ **Important**:  Siri can provide suggestions in search, News, Safari, and other apps using on-device information that you contribute through the Now Playing APIs. Users can control Siri on-device learning through Siri and Search settings for your app.

The system displays Now Playing information on the device’s Lock Screen and in the media controls in Control Center. If the user directs playback of your media to Apple TV using AirPlay, the Now Playing information appears on the television screen. If the user connects a device to an iPod accessory, such as in a car, the accessory may display Now Playing information.

> ❗ **Important**:  To ensure that your app interacts successfully with the widest possible range of accessories, provide values for as many information properties as you can in the [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) dictionary.

The information you can specify includes all of the Now Playing metadata properties (see the Accessing Now Playing metadata properties topic group below), and the following subset of [`MPMediaItem`](mpmediaitem.md) properties:

- [`MPMediaItemPropertyAlbumTitle`](mpmediaitempropertyalbumtitle.md)
- [`MPMediaItemPropertyAlbumTrackCount`](mpmediaitempropertyalbumtrackcount.md)
- [`MPMediaItemPropertyAlbumTrackNumber`](mpmediaitempropertyalbumtracknumber.md)
- [`MPMediaItemPropertyArtist`](mpmediaitempropertyartist.md)
- [`MPMediaItemPropertyArtwork`](mpmediaitempropertyartwork.md)
- [`MPMediaItemPropertyComposer`](mpmediaitempropertycomposer.md)
- [`MPMediaItemPropertyDiscCount`](mpmediaitempropertydisccount.md)
- [`MPMediaItemPropertyDiscNumber`](mpmediaitempropertydiscnumber.md)
- [`MPMediaItemPropertyGenre`](mpmediaitempropertygenre.md)
- [`MPMediaItemPropertyMediaType`](mpmediaitempropertymediatype.md)
- [`MPMediaItemPropertyPersistentID`](mpmediaitempropertypersistentid.md)
- [`MPMediaItemPropertyPlaybackDuration`](mpmediaitempropertyplaybackduration.md)
- [`MPMediaItemPropertyTitle`](mpmediaitempropertytitle.md)

You don’t have direct control over what information the system displays, or its formatting. You set the values in the [`nowPlayingInfo`](mpnowplayinginfocenter/nowplayinginfo.md) dictionary and the system or the connected accessory handles displaying the information in a consistent manner for all apps.

You can ensure that your app interacts well with other apps providing Now Playing information by following the best practices in the [`Becoming a now playable app`](becoming-a-now-playable-app.md) sample code project.

> ❗ **Important**:  In iOS 17.2 and later, the Journal app encourages people to reflect and write about their day-to-day experiences, including media they listened to or watched. If your app donates media information to [`MPNowPlayingInfoCenter`](mpnowplayinginfocenter.md), and you choose not to opt-out, the media played may appear as a suggestion in the Journal app, or other apps that use the Journaling Suggestions framework.

## Topics

### Working with the default Now Playing info center
- [class func `default`() -> MPNowPlayingInfoCenter](mpnowplayinginfocenter/default.md)
  Returns the singleton Now Playing info center.
- [var nowPlayingInfo: [String : Any]?](mpnowplayinginfocenter/nowplayinginfo.md)
  The current Now Playing information for the default Now Playing info center.
- [enum MPNowPlayingInfoMediaType](mpnowplayinginfomediatype.md)
  The type of media currently playing.
- [class var supportedAnimatedArtworkKeys: [String]](mpnowplayinginfocenter/supportedanimatedartworkkeys.md)
  Keys related to animated artwork that are supported by the current platform.
### Setting the playback state in macOS
- [var playbackState: MPNowPlayingPlaybackState](mpnowplayinginfocenter/playbackstate.md)
  The current playback state of the app.
- [enum MPNowPlayingPlaybackState](mpnowplayingplaybackstate.md)
  The playback state of the app.
### Accessing Now Playing metadata properties
- [let MPNowPlayingInfoCollectionIdentifier: String](mpnowplayinginfocollectionidentifier.md)
  The identifier of the collection the Now Playing item belongs to.
- [let MPNowPlayingInfoPropertyAdTimeRanges: String](mpnowplayinginfopropertyadtimeranges.md)
  A list of ad breaks in the Now Playing item.
- [let MPNowPlayingInfoPropertyAvailableLanguageOptions: String](mpnowplayinginfopropertyavailablelanguageoptions.md)
  The available language option groups for the Now Playing item.
- [let MPNowPlayingInfoPropertyAssetURL: String](mpnowplayinginfopropertyasseturl.md)
  The URL pointing to the Now Playing item’s underlying asset.
- [let MPNowPlayingInfoPropertyChapterCount: String](mpnowplayinginfopropertychaptercount.md)
  The total number of chapters in the Now Playing item.
- [let MPNowPlayingInfoPropertyChapterNumber: String](mpnowplayinginfopropertychapternumber.md)
  The number corresponding to the currently playing chapter.
- [let MPNowPlayingInfoPropertyCreditsStartTime: String](mpnowplayinginfopropertycreditsstarttime.md)
  The start time for the credits, in seconds, without ads, for the Now Playing item.
- [let MPNowPlayingInfoPropertyCurrentLanguageOptions: String](mpnowplayinginfopropertycurrentlanguageoptions.md)
  The currently active language options for the Now Playing item.
- [let MPNowPlayingInfoPropertyCurrentPlaybackDate: String](mpnowplayinginfopropertycurrentplaybackdate.md)
  The date associated with the current elapsed playback time.
- [let MPNowPlayingInfoPropertyDefaultPlaybackRate: String](mpnowplayinginfopropertydefaultplaybackrate.md)
  The default playback rate for the Now Playing item.
- [let MPNowPlayingInfoPropertyElapsedPlaybackTime: String](mpnowplayinginfopropertyelapsedplaybacktime.md)
  The elapsed time of the Now Playing item, in seconds.
- [let MPNowPlayingInfoPropertyExcludeFromSuggestions: String](mpnowplayinginfopropertyexcludefromsuggestions.md)
  A number that denotes whether to exclude the Now Playing item from content suggestions.
- [let MPNowPlayingInfoPropertyExternalContentIdentifier: String](mpnowplayinginfopropertyexternalcontentidentifier.md)
  The opaque identifier that uniquely identifies the Now Playing item, even through app relaunches.
- [let MPNowPlayingInfoPropertyExternalUserProfileIdentifier: String](mpnowplayinginfopropertyexternaluserprofileidentifier.md)
  The opaque identifier that uniquely identifies the profile the Now Playing item plays from, even through app relaunches.
- [let MPNowPlayingInfoPropertyInternationalStandardRecordingCode: String](mpnowplayinginfopropertyinternationalstandardrecordingcode.md)
  The International Standard Recording Code (ISRC) of the Now Playing item.
- [let MPNowPlayingInfoPropertyIsLiveStream: String](mpnowplayinginfopropertyislivestream.md)
  A number that denotes whether the Now Playing item is a live stream.
- [let MPNowPlayingInfoPropertyMediaType: String](mpnowplayinginfopropertymediatype.md)
  The media type of the Now Playing item.
- [let MPNowPlayingInfoPropertyPlaybackProgress: String](mpnowplayinginfopropertyplaybackprogress.md)
  The current progress of the Now Playing item.
- [let MPNowPlayingInfoPropertyPlaybackRate: String](mpnowplayinginfopropertyplaybackrate.md)
  The playback rate of the Now Playing item.
- [let MPNowPlayingInfoPropertyPlaybackQueueCount: String](mpnowplayinginfopropertyplaybackqueuecount.md)
  The total number of items in the app’s playback queue.
- [let MPNowPlayingInfoPropertyPlaybackQueueIndex: String](mpnowplayinginfopropertyplaybackqueueindex.md)
  The index of the Now Playing item in the app’s playback queue.
- [let MPNowPlayingInfoPropertyServiceIdentifier: String](mpnowplayinginfopropertyserviceidentifier.md)
  The service provider associated with the Now Playing item.
- [let MPNowPlayingInfoProperty1x1AnimatedArtwork: String](mpnowplayinginfoproperty1x1animatedartwork.md)
  1:1 (square) animated artwork for the current media item.
- [let MPNowPlayingInfoProperty3x4AnimatedArtwork: String](mpnowplayinginfoproperty3x4animatedartwork.md)
  3:4 (tall) animated artwork for the current media item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Becoming a now playable app](becoming-a-now-playable-app.md)
  Ensure your app is eligible to become the Now Playing app by adopting best practices for providing Now Playing info and registering for remote command center actions.
- [class MPNowPlayingSession](mpnowplayingsession.md)
  An object that manages Now Playing information and remote commands for multiple players.
- [class MPNowPlayingInfoLanguageOption](mpnowplayinginfolanguageoption.md)
  A set of interfaces for setting the language option for the Now Playing item.
- [class MPNowPlayingInfoLanguageOptionGroup](mpnowplayinginfolanguageoptiongroup.md)
  A grouped set of language options where only a single language option can be active at a time.
- [Language option characteristic constants](language-option-characteristic-constants.md)
  The constants for defining language characteristics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)*