# General media item property keys

**Framework**: Media Player

System-defined properties for obtaining the metadata for a media item.

#### Overview

Obtain metadata for a media item by calling the [`value(forProperty:)`](mpmediaentity/value(forproperty:).md) method with these property keys. You can use the filterable property keys to build media property predicates, which [`MPMediaPropertyPredicate`](mpmediapropertypredicate.md) describes.

## Topics

### Property keys
- [let MPMediaItemPropertyPlaybackDuration: String](mpmediaitempropertyplaybackduration.md)
  The playback duration of the media item.
- [let MPMediaItemPropertyAlbumTrackNumber: String](mpmediaitempropertyalbumtracknumber.md)
  The track number of the media item, for a media item that is part of an album.
- [let MPMediaItemPropertyAlbumTrackCount: String](mpmediaitempropertyalbumtrackcount.md)
  The number of tracks for the album that contains the media item.
- [let MPMediaItemPropertyDiscNumber: String](mpmediaitempropertydiscnumber.md)
  The disc number of the media item, for a media item that is part of a multidisc album.
- [let MPMediaItemPropertyDiscCount: String](mpmediaitempropertydisccount.md)
  The number of discs for the album that contains the media item.
- [let MPMediaItemPropertyArtwork: String](mpmediaitempropertyartwork.md)
  The artwork image for the media item.
- [let MPMediaItemPropertyLyrics: String](mpmediaitempropertylyrics.md)
  The lyrics for the media item.
- [let MPMediaItemPropertyReleaseDate: String](mpmediaitempropertyreleasedate.md)
  The date of the media item’s first public release.
- [let MPMediaItemPropertyBeatsPerMinute: String](mpmediaitempropertybeatsperminute.md)
  The number of musical beats per minute for the media item.
- [let MPMediaItemPropertyComments: String](mpmediaitempropertycomments.md)
  Textual information about the media item.
- [let MPMediaItemPropertyAssetURL: String](mpmediaitempropertyasseturl.md)
  A URL that points to the media item.
- [let MPMediaItemPropertyIsExplicit: String](mpmediaitempropertyisexplicit.md)
  A Boolean value that indicates whether the media item contains explicit (adult) lyrics or language.
- [let MPMediaItemPropertyIsPreorder: String](mpmediaitempropertyispreorder.md)
  A Boolean value that indicates whether the media item is a preorder.
- [let MPMediaItemPropertyPlaybackStoreID: String](mpmediaitempropertyplaybackstoreid.md)
  The identifier for enqueueing store tracks.
### Filterable property keys
- [let MPMediaItemPropertyAlbumArtist: String](mpmediaitempropertyalbumartist.md)
  The primary performing artist for an album.
- [let MPMediaItemPropertyAlbumArtistPersistentID: String](mpmediaitempropertyalbumartistpersistentid.md)
  The persistent identifier for an album artist.
- [let MPMediaItemPropertyAlbumPersistentID: String](mpmediaitempropertyalbumpersistentid.md)
  The key for the persistent identifier for an album.
- [let MPMediaItemPropertyAlbumTitle: String](mpmediaitempropertyalbumtitle.md)
  The title of an album.
- [let MPMediaItemPropertyArtist: String](mpmediaitempropertyartist.md)
  The performing artists for a media item — which may vary from the primary artist for the album that a media item belongs to.
- [let MPMediaItemPropertyArtistPersistentID: String](mpmediaitempropertyartistpersistentid.md)
  The key for the persistent identifier for an artist.
- [let MPMediaItemPropertyComposer: String](mpmediaitempropertycomposer.md)
  The musical composer for the media item.
- [let MPMediaItemPropertyComposerPersistentID: String](mpmediaitempropertycomposerpersistentid.md)
  The persistent identifier for a composer.
- [let MPMediaItemPropertyGenre: String](mpmediaitempropertygenre.md)
  The music or film genre of the media item.
- [let MPMediaItemPropertyGenrePersistentID: String](mpmediaitempropertygenrepersistentid.md)
  The persistent identifier for a genre.
- [let MPMediaItemPropertyHasProtectedAsset: String](mpmediaitempropertyhasprotectedasset.md)
  A Boolean value that indicates the media item has DRM protection so it can’t play through a standard playback API.
- [let MPMediaItemPropertyIsCompilation: String](mpmediaitempropertyiscompilation.md)
  A Boolean value that indicates whether the media item is part of a compilation.
- [let MPMediaItemPropertyIsCloudItem: String](mpmediaitempropertyisclouditem.md)
  A Boolean value that indicates whether the media item is an iCloud item.
- [let MPMediaItemPropertyMediaType: String](mpmediaitempropertymediatype.md)
  The media type of the media item.
- [let MPMediaItemPropertyPersistentID: String](mpmediaitempropertypersistentid.md)
  The key for the persistent identifier for the media item.
- [let MPMediaItemPropertyPlayCount: String](mpmediaitempropertyplaycount.md)
  The number of times the user plays the media item.
- [let MPMediaItemPropertyPodcastPersistentID: String](mpmediaitempropertypodcastpersistentid.md)
  The persistent identifier for an audio podcast.
- [let MPMediaItemPropertyPodcastTitle: String](mpmediaitempropertypodcasttitle.md)
  The title of a podcast.
- [let MPMediaItemPropertyTitle: String](mpmediaitempropertytitle.md)
  The title or name of the media item.

## See Also

- [struct MPMediaType](mpmediatype.md)
  The properties for defining the type for a media item.
- [User-defined property keys](user-defined-property-keys.md)
  Properties for obtaining user-defined metadata for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/general-media-item-property-keys)*