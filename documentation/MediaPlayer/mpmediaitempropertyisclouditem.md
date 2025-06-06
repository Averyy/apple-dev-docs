# MPMediaItemPropertyIsCloudItem

**Framework**: Media Player  
**Kind**: var

A Boolean value that indicates whether the media item is an iCloud item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPMediaItemPropertyIsCloudItem: String
```

#### Discussion

A media item is an iCloud item if it’s available in the iCloud Music Library, or if it’s part of the Apple Music subscription service and isn’t already on the device. This value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that represents a `BOOL` data type.

## See Also

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
- [let MPMediaItemPropertyMediaType: String](mpmediaitempropertymediatype.md)
  The media type of the media item.
- [let MPMediaItemPropertyPersistentID: String](mpmediaitempropertypersistentid.md)
  The key for the persistent identifier for the media item.
- [let MPMediaItemPropertyPlayCount: String](mpmediaitempropertyplaycount.md)
  The number of times the user plays the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyisclouditem)*