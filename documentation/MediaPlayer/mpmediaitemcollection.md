# MPMediaItemCollection

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPMediaItemCollection : MPMediaEntity
```

#### Overview

Typically, you use this class by requesting an array of [`collections`](./mpmediaquery/collections.md) from a media query by way of its collections property. [`MPMediaQuery`](./mpmediaquery.md) describes media queries.

The grouping type for the media query determines the arrangement of the media items you obtain. You also use the media query [`collections`](./mpmediaquery/collections.md) property to obtain synced playlists, as described in [`MPMediaPlaylist`](./mpmediaplaylist.md).

A media item collection can have a wide range of metadata associated with it. You access this metadata using the [`value(forProperty:)`](./mpmediaentity/value%28forproperty%29.md) method along with the property keys described in this document. You can also access metadata in a batch fashion using the [`enumerateValues(forProperties:using:)`](./mpmediaentity/enumeratevalues%28forproperties,using%29.md) method. In some cases, this is more efficient. [`MPMediaEntity`](./mpmediaentity.md) defines and describes both of these methods.

## Topics

### Creating a media item collection
- [init(items: [MPMediaItem])](./mpmediaitemcollection/init%28items%29.md)
  Initializes a media item collection with an array of media items.
- [+ collectionWithItems:](./mpmediaitemcollection/collectionwithitems_.md)
  Creates a media item collection by copying an array of media items.
### Using a media item collection
- [var items: [MPMediaItem]](./mpmediaitemcollection/items.md)
  The media items in a media item collection.
- [var representativeItem: MPMediaItem?](./mpmediaitemcollection/representativeitem.md)
  A media item whose properties are representative of the other media items in a collection.
- [var count: Int](./mpmediaitemcollection/count.md)
  The number of media items in a collection.
- [var mediaTypes: MPMediaType](./mpmediaitemcollection/mediatypes.md)
  The types of the media items in a collection.

## Relationships

### Inherits From
- [MPMediaEntity](./mpmediaentity.md)
### Inherited By
- [MPMediaPlaylist](./mpmediaplaylist.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Media items and playlists
- [Providing animated artwork for media items](./providing-animated-artwork-for-media-items.md)
  Display animated artwork for your app’s media in system views, such as the lock screen, by providing video assets through your now playing info.
- [class MPMediaItem](./mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](./mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemAnimatedArtwork](./mpmediaitemanimatedartwork.md)
  An animated image, such as an animated music album cover art, for a media item.
- [class MPMediaPlaylist](./mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](./mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.
- [class MPMediaEntity](./mpmediaentity.md)
  The abstract superclass for media items, media item collections, and media playlist instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)*