# MPMediaPlaylistPropertyPersistentID

**Framework**: Media Player  
**Kind**: var

The persistent identifier for the playlist.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
let MPMediaPlaylistPropertyPersistentID: String
```

#### Discussion

Value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a `UInt64_t` (unsigned long long). Can be used to build a media property predicate as described in [`MPMediaQuery`](mpmediaquery.md).

## See Also

- [let MPMediaPlaylistPropertyAuthorDisplayName: String](mpmediaplaylistpropertyauthordisplayname.md)
  App defined name for the playlist.
- [let MPMediaPlaylistPropertyName: String](mpmediaplaylistpropertyname.md)
  The name of the playlist.
- [let MPMediaPlaylistPropertyDescriptionText: String](mpmediaplaylistpropertydescriptiontext.md)
  Descriptive text for the playlist.
- [let MPMediaPlaylistPropertyPlaylistAttributes: String](mpmediaplaylistpropertyplaylistattributes.md)
  The attributes associated with the playlist.
- [let MPMediaPlaylistPropertyCloudGlobalID: String](mpmediaplaylistpropertycloudglobalid.md)
  The cloud identifier for the playlist.
- [let MPMediaPlaylistPropertySeedItems: String](mpmediaplaylistpropertyseeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertypersistentid)*