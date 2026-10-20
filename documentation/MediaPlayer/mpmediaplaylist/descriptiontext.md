# descriptionText

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

User supplied text that describes the playlist.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var descriptionText: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * descriptionText;
```

## See Also

### Retrieving information about a playlist
- [var authorDisplayName: String?](./authordisplayname.md)
  The display name for the playlist defined in the app.
- [var name: String?](./name.md)
  The name of the playlist.
- [var persistentID: MPMediaEntityPersistentID](./persistentid.md)
  The persistent identifier for the playlist.
- [var cloudGlobalID: String?](./cloudglobalid.md)
  The cloud identifier for the playlist.
- [var playlistAttributes: MPMediaPlaylistAttribute](./playlistattributes.md)
  The attributes associated with the playlist.
- [struct MPMediaPlaylistAttribute](../mpmediaplaylistattribute.md)
  Attributes define the type of playlist.
- [var seedItems: [MPMediaItem]?](./seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/descriptiontext)*