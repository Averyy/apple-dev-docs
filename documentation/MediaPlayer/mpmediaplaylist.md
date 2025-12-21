# MPMediaPlaylist

**Framework**: Media Player  
**Kind**: class

A playable collection of related media items.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaPlaylist
```

#### Overview

Each playlist has a name, a set of attributes, and a unique identifier that persists across application launches.

Users configure playlists using iTunes or by creating a playlist on the device. Playlists are read-only to your iOS app. To obtain playlists, configure a media query that’s grouped by playlist. Each returned media item collection is a media playlist. The following code snippet illustrates this by logging playlist and song names to the Xcode debugger console:

[`MPMediaPropertyPredicate`](mpmediapropertypredicate.md) and [`MPMediaQuery`](mpmediaquery.md) describe the API for building a media query. [`MPMediaEntity`](mpmediaentity.md) describes the methods for querying media playlist property values.

## Topics

### Adding media items to a playlist
- [func addItem(withProductID: String, completionHandler: (((any Error)?) -> Void)?)](mpmediaplaylist/additem(withproductid:completionhandler:).md)
  Adds the item associated with the product identifier to the end of the playlist.
- [func add([MPMediaItem], completionHandler: (((any Error)?) -> Void)?)](mpmediaplaylist/add(_:completionhandler:).md)
  Adds an array of media items to the end of the playlist.
### Retrieving information about a playlist
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
- [struct MPMediaPlaylistAttribute](mpmediaplaylistattribute.md)
  Attributes define the type of playlist.
- [var seedItems: [MPMediaItem]?](mpmediaplaylist/seeditems.md)
  The items seeded to generate the playlist; applies only to Genius playlists.
### Property keys
- [Playlist property keys](playlist-property-keys.md)
  Keys that contain information about a playlist.

## Relationships

### Inherits From
- [MPMediaItemCollection](mpmediaitemcollection.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist)*