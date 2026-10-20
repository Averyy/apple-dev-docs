# MPMediaPlaylistPropertySeedItems

**Framework**: Media Player  
**Kind**: var  
**Role**: Global Variable

The items seeded to generate the playlist; applies only to Genius playlists.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
let MPMediaPlaylistPropertySeedItems: String
```

```c
extern NSString * const MPMediaPlaylistPropertySeedItems;
```

#### Discussion

Value is an [`NSArray`](../Foundation/nsarray.md) object containing one or more [`MPMediaItem`](./mpmediaitem.md) objects. Value is `nil` for playlists that don’t have the [`genius`](./mpmediaplaylistattribute/genius.md) flag set.

## See Also

### Property keys
- [let MPMediaPlaylistPropertyAuthorDisplayName: String](./mpmediaplaylistpropertyauthordisplayname.md)
  App defined name for the playlist.
- [let MPMediaPlaylistPropertyName: String](./mpmediaplaylistpropertyname.md)
  The name of the playlist.
- [let MPMediaPlaylistPropertyDescriptionText: String](./mpmediaplaylistpropertydescriptiontext.md)
  Descriptive text for the playlist.
- [let MPMediaPlaylistPropertyPersistentID: String](./mpmediaplaylistpropertypersistentid.md)
  The persistent identifier for the playlist.
- [let MPMediaPlaylistPropertyPlaylistAttributes: String](./mpmediaplaylistpropertyplaylistattributes.md)
  The attributes associated with the playlist.
- [let MPMediaPlaylistPropertyCloudGlobalID: String](./mpmediaplaylistpropertycloudglobalid.md)
  The cloud identifier for the playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertyseeditems)*