# persistentID

**Framework**: Media Player  
**Kind**: property

The persistent identifier for the playlist.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var persistentID: MPMediaEntityPersistentID { get }
```

## See Also

- [var authorDisplayName: String?](mpmediaplaylist/authordisplayname.md)
  The display name for the playlist defined in the app.
- [var descriptionText: String?](mpmediaplaylist/descriptiontext.md)
  User supplied text that describes the playlist.
- [var name: String?](mpmediaplaylist/name.md)
  The name of the playlist.
- [var cloudGlobalID: String?](mpmediaplaylist/cloudglobalid.md)
  The cloud identifier for the playlist.
- [var playlistAttributes: MPMediaPlaylistAttribute](mpmediaplaylist/playlistattributes.md)
  The attributes associated with the playlist.
- [struct MPMediaPlaylistAttribute](mpmediaplaylistattribute.md)
  Attributes define the type of playlist.
- [var seedItems: [MPMediaItem]?](mpmediaplaylist/seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/persistentid)*