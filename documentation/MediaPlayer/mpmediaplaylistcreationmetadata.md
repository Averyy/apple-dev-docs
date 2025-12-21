# MPMediaPlaylistCreationMetadata

**Framework**: Media Player  
**Kind**: class

A set of attributes for describing a playlist when creating it.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaPlaylistCreationMetadata
```

#### Overview

Use this class when creating a new playlist using the [`getPlaylist(with:creationMetadata:completionHandler:)`](mpmedialibrary/getplaylist(with:creationmetadata:completionhandler:).md) method. The system adds the metadata to the playlist when you create it, however it ignores the metadata if the playlist already exists.

## Topics

### Creating metadata for a playlist
- [init(name: String)](mpmediaplaylistcreationmetadata/init(name:).md)
  Creates a new playlist metadata object with the designated name.
### Metadata for a playlist
- [var authorDisplayName: String!](mpmediaplaylistcreationmetadata/authordisplayname.md)
  App defined display name for the playlist.
- [var descriptionText: String](mpmediaplaylistcreationmetadata/descriptiontext.md)
  The descriptive text for the playlist.
- [var name: String](mpmediaplaylistcreationmetadata/name.md)
  The playlist’s displayed name.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Providing animated artwork for media items](providing-animated-artwork-for-media-items.md)
  Display animated artwork for your app’s media in system views, such as the lock screen, by providing video assets through your now playing info.
- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemAnimatedArtwork](mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata)*