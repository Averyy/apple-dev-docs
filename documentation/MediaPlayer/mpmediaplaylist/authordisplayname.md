# authorDisplayName

**Framework**: Media Player  
**Kind**: property

The display name for the playlist defined in the app.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var authorDisplayName: String? { get }
```

#### Discussion

The system requires this property for 3rd party apps. Defaults to the app display name when not defined.

## See Also

- [var descriptionText: String?](mpmediaplaylist/descriptiontext.md)
  User supplied text that describes the playlist.
- [var name: String?](mpmediaplaylist/name.md)
  The name of the playlist.
- [var persistentID: MPMediaEntityPersistentID](mpmediaplaylist/persistentid.md)
  The persistent identifier for the playlist.
- [var cloudGlobalID: String?](mpmediaplaylist/cloudglobalid.md)
  The cloud identifier for the playlist.
- [var playlistAttributes: MPMediaPlaylistAttribute](mpmediaplaylist/playlistattributes.md)
  The attributes associated with the playlist.
- [struct MPMediaPlaylistAttribute](mpmediaplaylistattribute.md)
  Attributes define the type of playlist.
- [var seedItems: [MPMediaItem]?](mpmediaplaylist/seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/authordisplayname)*