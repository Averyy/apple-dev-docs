# MPMediaItemPropertyAlbumTrackCount

**Framework**: Media Player  
**Kind**: var

The number of tracks for the album that contains the media item.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPMediaItemPropertyAlbumTrackCount: String
```

#### Discussion

This value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object that represents an [`NSUInteger`](https://developer.apple.com/documentation/ObjectiveC/NSUInteger) data type. For an audio streaming app, the system provides a default value of `1` for this property.

## See Also

- [let MPMediaItemPropertyPlaybackDuration: String](mpmediaitempropertyplaybackduration.md)
  The playback duration of the media item.
- [let MPMediaItemPropertyAlbumTrackNumber: String](mpmediaitempropertyalbumtracknumber.md)
  The track number of the media item, for a media item that is part of an album.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyalbumtrackcount)*