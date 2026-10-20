# playlistAttributes

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The attributes associated with the playlist.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var playlistAttributes: MPMediaPlaylistAttribute { get }
```

```objc
@property (nonatomic, readonly) MPMediaPlaylistAttribute playlistAttributes;
```

## See Also

### Retrieving information about a playlist
- [var authorDisplayName: String?](./authordisplayname.md)
  The display name for the playlist defined in the app.
- [var descriptionText: String?](./descriptiontext.md)
  User supplied text that describes the playlist.
- [var name: String?](./name.md)
  The name of the playlist.
- [var persistentID: MPMediaEntityPersistentID](./persistentid.md)
  The persistent identifier for the playlist.
- [var cloudGlobalID: String?](./cloudglobalid.md)
  The cloud identifier for the playlist.
- [struct MPMediaPlaylistAttribute](../mpmediaplaylistattribute.md)
  Attributes define the type of playlist.
- [var seedItems: [MPMediaItem]?](./seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/playlistattributes)*