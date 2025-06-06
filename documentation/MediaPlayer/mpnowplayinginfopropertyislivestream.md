# MPNowPlayingInfoPropertyIsLiveStream

**Framework**: Media Player  
**Kind**: var

A number that denotes whether the Now Playing item is a live stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPNowPlayingInfoPropertyIsLiveStream: String
```

#### Discussion

Value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object configured as a `boolean`. A value of `1.0` indicates the now playing item is a live stream.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyislivestream)*