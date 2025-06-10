# MPMediaPlaylistAttribute

**Framework**: Media Player  
**Kind**: struct

Attributes define the type of playlist.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct MPMediaPlaylistAttribute
```

#### Overview

Playlist attributes to use as possible values for the [`MPMediaPlaylistPropertyPlaylistAttributes`](mpmediaplaylistpropertyplaylistattributes.md) property.

## Topics

### Constants
- [static var onTheGo: MPMediaPlaylistAttribute](mpmediaplaylistattribute/onthego.md)
  A playlist created on a device rather than synced from the Music app.
- [static var smart: MPMediaPlaylistAttribute](mpmediaplaylistattribute/smart.md)
  A smart playlist includes items that match one or more user-specified rules.
- [static var genius: MPMediaPlaylistAttribute](mpmediaplaylistattribute/genius.md)
  A Genius playlist includes items related to other items in your Music library.
### Initializers
- [init(rawValue: UInt)](mpmediaplaylistattribute/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var authorDisplayName: String?](mpmediaplaylist/authordisplayname.md)
  The display name for the playlist defined in the app.
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
- [var seedItems: [MPMediaItem]?](mpmediaplaylist/seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute)*