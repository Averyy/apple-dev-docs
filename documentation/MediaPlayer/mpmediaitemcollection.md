# MPMediaItemCollection

**Framework**: Media Player  
**Kind**: class

A sorted set of media items from the media library.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MPMediaItemCollection
```

#### Overview

Typically, you use this class by requesting an array of [`collections`](mpmediaquery/collections.md) from a media query by way of its collections property. [`MPMediaQuery`](mpmediaquery.md) describes media queries.

The grouping type for the media query determines the arrangement of the media items you obtain. You also use the media query [`collections`](mpmediaquery/collections.md) property to obtain synced playlists, as described in [`MPMediaPlaylist`](mpmediaplaylist.md).

A media item collection can have a wide range of metadata associated with it. You access this metadata using the [`value(forProperty:)`](mpmediaentity/value(forproperty:).md) method along with the property keys described in this document. You can also access metadata in a batch fashion using the [`enumerateValues(forProperties:using:)`](mpmediaentity/enumeratevalues(forproperties:using:).md) method. In some cases, this is more efficient. [`MPMediaEntity`](mpmediaentity.md) defines and describes both of these methods.

## Topics

### Creating a media item collection
- [init(items: [MPMediaItem])](mpmediaitemcollection/init(items:).md)
  Initializes a media item collection with an array of media items.
### Using a media item collection
- [var items: [MPMediaItem]](mpmediaitemcollection/items.md)
  The media items in a media item collection.
- [var representativeItem: MPMediaItem?](mpmediaitemcollection/representativeitem.md)
  A media item whose properties are representative of the other media items in a collection.
- [var count: Int](mpmediaitemcollection/count.md)
  The number of media items in a collection.
- [var mediaTypes: MPMediaType](mpmediaitemcollection/mediatypes.md)
  The types of the media items in a collection.

## Relationships

### Inherits From
- [MPMediaEntity](mpmediaentity.md)
### Inherited By
- [MPMediaPlaylist](mpmediaplaylist.md)
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

- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)*