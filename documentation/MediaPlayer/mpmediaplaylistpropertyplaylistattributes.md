# MPMediaPlaylistPropertyPlaylistAttributes

**Framework**: Media Player  
**Kind**: var

The attributes associated with the playlist.

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
let MPMediaPlaylistPropertyPlaylistAttributes: String
```

#### Discussion

Value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing an [`NSInteger`](https://developer.apple.com/documentation/ObjectiveC/NSInteger) data type. Fields in the `NSInteger` identify the attributes of the playlist. A playlist may have any combination of attributes described in [`MPMediaPlaylistAttribute`](mpmediaplaylistattribute.md). Can be used to build a media property predicate as described in [`MPMediaQuery`](mpmediaquery.md).

## See Also

- [let MPMediaPlaylistPropertyAuthorDisplayName: String](mpmediaplaylistpropertyauthordisplayname.md)
  App defined name for the playlist.
- [let MPMediaPlaylistPropertyName: String](mpmediaplaylistpropertyname.md)
  The name of the playlist.
- [let MPMediaPlaylistPropertyDescriptionText: String](mpmediaplaylistpropertydescriptiontext.md)
  Descriptive text for the playlist.
- [let MPMediaPlaylistPropertyPersistentID: String](mpmediaplaylistpropertypersistentid.md)
  The persistent identifier for the playlist.
- [let MPMediaPlaylistPropertyCloudGlobalID: String](mpmediaplaylistpropertycloudglobalid.md)
  The cloud identifier for the playlist.
- [let MPMediaPlaylistPropertySeedItems: String](mpmediaplaylistpropertyseeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertyplaylistattributes)*