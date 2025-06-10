# MPMediaItem

**Framework**: Media Player  
**Kind**: class

A collection of properties that represents a single item in the media library.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMediaItem
```

#### Overview

A media item has an overall unique identifier, accessed using the [`MPMediaItemPropertyPersistentID`](mpmediaitempropertypersistentid.md) property key, as well as specific identifiers for its metadata. These identifiers persists across application launches.

A media item can have a wide range of metadata associated with it. You access this metadata using the [`value(forProperty:)`](mpmediaentity/value(forproperty:).md) method along with the property keys described in this document. You can also access metadata in a batch fashion using the [`enumerateValues(forProperties:using:)`](mpmediaentity/enumeratevalues(forproperties:using:).md) method. Anytime the app accesses more than one property, enumerating over a set of property keys is more efficient than fetching each individual property. [`MPMediaEntity`](mpmediaentity.md) defines both of these methods, the abstract superclass of [`MPMediaItemCollection`](mpmediaitemcollection.md), and described in `MPMediaEntity`.

You use attributes of media items to build media queries for searching the Media library. [`MPMediaType`](mpmediatype.md), [`General media item property keys`](general-media-item-property-keys.md), and `Podcast Item Property Keys` describe these attributes. In addition, [`Media entity property keys`](media-entity-property-keys.md) describes the [`MPMediaEntityPropertyPersistentID`](mpmediaentitypropertypersistentid.md) property, and [`MPMediaQuery`](mpmediaquery.md) describes media queries.

## Topics

### Media item properties
- [var albumArtist: String?](mpmediaitem/albumartist.md)
  The primary performing artist for an album.
- [var albumArtistPersistentID: MPMediaEntityPersistentID](mpmediaitem/albumartistpersistentid.md)
  The persistent identifier for the primary performing artist for an album.
- [var albumPersistentID: MPMediaEntityPersistentID](mpmediaitem/albumpersistentid.md)
  The persistent identifier for an album.
- [var albumTitle: String?](mpmediaitem/albumtitle.md)
  The title of an album, such as , rather than the title of an individual song on the album, such as “Crater Dance.”
- [var albumTrackCount: Int](mpmediaitem/albumtrackcount.md)
  The number of tracks for the album that contains the media item.
- [var albumTrackNumber: Int](mpmediaitem/albumtracknumber.md)
  The track number of the media item, for a media item that’s part of an album.
- [var artist: String?](mpmediaitem/artist.md)
  The performing artists for a media item, which may vary from the primary artist for the album that a media item belongs to.
- [var artistPersistentID: MPMediaEntityPersistentID](mpmediaitem/artistpersistentid.md)
  The persistent identifier for an artist.
- [var artwork: MPMediaItemArtwork?](mpmediaitem/artwork.md)
  The artwork image for the media item.
- [var assetURL: URL?](mpmediaitem/asseturl.md)
  The URL that points to the media item.
- [var beatsPerMinute: Int](mpmediaitem/beatsperminute.md)
  The number of musical beats per minute for the media item.
- [var bookmarkTime: TimeInterval](mpmediaitem/bookmarktime.md)
  The time of the user’s most recent interaction with the bookmark in the media item.
- [var isCloudItem: Bool](mpmediaitem/isclouditem.md)
  A Boolean value that indicates whether the media item is an iCloud Music Library item.
- [var comments: String?](mpmediaitem/comments.md)
  Textual information about the media item.
- [var isCompilation: Bool](mpmediaitem/iscompilation.md)
  A Boolean value that indicates whether the media item is part of a compilation.
- [var isPreorder: Bool](mpmediaitem/ispreorder.md)
  A Boolean value that indicates whether the media item is a preorder.
- [var composer: String?](mpmediaitem/composer.md)
  The musical composer for the media item.
- [var composerPersistentID: MPMediaEntityPersistentID](mpmediaitem/composerpersistentid.md)
  The persistent identifier for a composer.
- [var dateAdded: Date](mpmediaitem/dateadded.md)
  The date the user adds the media item to the library.
- [var discCount: Int](mpmediaitem/disccount.md)
  The number of discs for the album that contains the media item.
- [var discNumber: Int](mpmediaitem/discnumber.md)
  The disc number of the media item, for a media item that’s part of a multidisc album.
- [var isExplicitItem: Bool](mpmediaitem/isexplicititem.md)
  A Boolean value that indicates whether the media item has explicit (adult) lyrics or language.
- [var genre: String?](mpmediaitem/genre.md)
  The music or film genre of the media item.
- [var genrePersistentID: MPMediaEntityPersistentID](mpmediaitem/genrepersistentid.md)
  The persistent identifier for a genre.
- [var lastPlayedDate: Date?](mpmediaitem/lastplayeddate.md)
  The most recent play date of the media item.
- [var lyrics: String?](mpmediaitem/lyrics.md)
  The lyrics for the media item.
- [var mediaType: MPMediaType](mpmediaitem/mediatype.md)
  The media type of the media item.
- [var persistentID: MPMediaEntityPersistentID](mpmediaitem/persistentid.md)
  The persistent identifier for the media item.
- [var playCount: Int](mpmediaitem/playcount.md)
  The number of times the user plays the media item.
- [var playbackDuration: TimeInterval](mpmediaitem/playbackduration.md)
  The playback duration of the media item.
- [var playbackStoreID: String](mpmediaitem/playbackstoreid.md)
  The ID of a media item from the Apple Music catalog.
- [var podcastPersistentID: MPMediaEntityPersistentID](mpmediaitem/podcastpersistentid.md)
  The persistent identifier for an audio podcast.
- [var podcastTitle: String?](mpmediaitem/podcasttitle.md)
  The title of a podcast, such as , rather than the title of an individual episode of a podcast, such as “Episode 12: Another Cold Day at the Pole.”
- [var hasProtectedAsset: Bool](mpmediaitem/hasprotectedasset.md)
  A Boolean value that indicates whether the media item has a protected asset.
- [var rating: Int](mpmediaitem/rating.md)
  The user-specified rating of the media item.
- [var releaseDate: Date?](mpmediaitem/releasedate.md)
  The date of the media item’s first public release.
- [var skipCount: Int](mpmediaitem/skipcount.md)
  The number of times the user skips playing the media item.
- [var title: String?](mpmediaitem/title.md)
  The title or name of the media item.
- [var userGrouping: String?](mpmediaitem/usergrouping.md)
  Grouping information for the media item.
### Obtaining group properties
- [class func persistentIDProperty(forGroupingType: MPMediaGrouping) -> String](mpmediaitem/persistentidproperty(forgroupingtype:).md)
  Obtains the persistent identifier key for a specified grouping type.
- [class func titleProperty(forGroupingType: MPMediaGrouping) -> String](mpmediaitem/titleproperty(forgroupingtype:).md)
  Obtains the title key for a specified grouping type.
### Media item types and keys
- [struct MPMediaType](mpmediatype.md)
  The properties for defining the type for a media item.
- [General media item property keys](general-media-item-property-keys.md)
  System-defined properties for obtaining the metadata for a media item.
- [User-defined property keys](user-defined-property-keys.md)
  Properties for obtaining user-defined metadata for a media item.

## Relationships

### Inherits From
- [MPMediaEntity](mpmediaentity.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemAnimatedArtwork](mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)*