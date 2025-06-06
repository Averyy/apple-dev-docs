# TVMediaItem

**Framework**: TVMLKit  
**Kind**: class

A single audio or video item associated with the Apple TV JavaScript player.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVMediaItem
```

#### Overview

A `TVMediaItem` object contains read-only information about a media item associated with the JavaScript player. You can use this information with your own custom [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) objects exposed through a [`TVPlayer`](tvplayer.md) object. For example, you can retrieve audio track information from the JavaScript player and play the track through a [`TVPlayer`](tvplayer.md) object.

## Topics

### Rating Media Content
- [var containsExplicitContent: Bool](tvmediaitem/containsexplicitcontent.md)
  A Boolean value indicating whether the item contains adult-oriented content.
- [var contentRatingDomain: TVMediaItem.ContentRatingDomain?](tvmediaitem/contentratingdomain-swift.property.md)
  The media domain that the rating applies to.
- [TVMediaItem.ContentRatingDomain](tvmediaitem/contentratingdomain-swift.struct.md)
  A value identifying the media’s content rating domain.
- [var contentRatingRanking: NSNumber?](tvmediaitem/contentratingranking.md)
  The rating for a video item.
### Identifying Media Items
- [var artworkImageURL: URL?](tvmediaitem/artworkimageurl.md)
  The URL path to the artwork that accompanies the media item.
- [var itemDescription: String?](tvmediaitem/itemdescription.md)
  The description for a media item.
- [var subtitle: String?](tvmediaitem/subtitle.md)
  The subtitle for a media item.
- [var title: String?](tvmediaitem/title.md)
  The title for a media item.
- [var type: TVMediaItem.MediaType?](tvmediaitem/type.md)
  The type of media item.
- [TVMediaItem.MediaType](tvmediaitem/mediatype.md)
  A value indicating whether the media is audio or video.
- [var url: URL?](tvmediaitem/url.md)
  The URL path to the media item.
- [var userInfo: [String : Any]](tvmediaitem/userinfo.md)
  User-defined metadata, like a developer-specific identifier, for a media item.
### Setting Timing Options
- [var highlightGroups: [TVMediaItem.HighlightGroup]](tvmediaitem/highlightgroups.md)
  An array containing groups of individual highlights in a media item.
- [TVMediaItem.HighlightGroup](tvmediaitem/highlightgroup.md)
  A container for groups of highlights for a media item.
- [var interstitials: [TVMediaItem.TimeRange]](tvmediaitem/interstitials.md)
  An array of time intervals that indicate where to insert media items into another, single media item.
- [TVMediaItem.TimeRange](tvmediaitem/timerange.md)
  An object that defines a time range in a media item.
- [var resumeTime: TimeInterval](tvmediaitem/resumetime.md)
  The number of seconds from the beginning of a media item to the point where that media item begins playing.

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

- [class TVPlaylist](tvplaylist.md)
  A collection of media items associated with the Apple TV JavaScript player.
- [class TVPlayer](tvplayer.md)
  A customizable native media player used to control playback from the JavaScript player used in an Apple TV client-server app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvmediaitem)*