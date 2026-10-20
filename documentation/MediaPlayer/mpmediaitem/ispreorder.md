# isPreorder

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the media item is a preorder.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var isPreorder: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPreorder) BOOL preorder;
```

## See Also

### Media item properties
- [var albumArtist: String?](./albumartist.md)
  The primary performing artist for an album.
- [var albumArtistPersistentID: MPMediaEntityPersistentID](./albumartistpersistentid.md)
  The persistent identifier for the primary performing artist for an album.
- [var albumPersistentID: MPMediaEntityPersistentID](./albumpersistentid.md)
  The persistent identifier for an album.
- [var albumTitle: String?](./albumtitle.md)
  The title of an album, such as *Live on Mars*, rather than the title of an individual song on the album, such as “Crater Dance.”
- [var albumTrackCount: Int](./albumtrackcount.md)
  The number of tracks for the album that contains the media item.
- [var albumTrackNumber: Int](./albumtracknumber.md)
  The track number of the media item, for a media item that’s part of an album.
- [var artist: String?](./artist.md)
  The performing artists for a media item, which may vary from the primary artist for the album that a media item belongs to.
- [var artistPersistentID: MPMediaEntityPersistentID](./artistpersistentid.md)
  The persistent identifier for an artist.
- [var artwork: MPMediaItemArtwork?](./artwork.md)
  The artwork image for the media item.
- [var assetURL: URL?](./asseturl.md)
  The URL that points to the media item.
- [var beatsPerMinute: Int](./beatsperminute.md)
  The number of musical beats per minute for the media item.
- [var bookmarkTime: TimeInterval](./bookmarktime.md)
  The time of the user’s most recent interaction with the bookmark in the media item.
- [var isCloudItem: Bool](./isclouditem.md)
  A Boolean value that indicates whether the media item is an iCloud Music Library item.
- [var comments: String?](./comments.md)
  Textual information about the media item.
- [var isCompilation: Bool](./iscompilation.md)
  A Boolean value that indicates whether the media item is part of a compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/ispreorder)*