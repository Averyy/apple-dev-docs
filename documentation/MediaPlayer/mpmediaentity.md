# MPMediaEntity

**Framework**: Media Player  
**Kind**: class

The abstract superclass for media items, media item collections, and media playlist instances.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMediaEntity
```

#### Overview

This is the superclass for [`MPMediaItem`](mpmediaitem.md) and [`MPMediaItemCollection`](mpmediaitemcollection.md) instances, and in turn for [`MPMediaPlaylist`](mpmediaplaylist.md) instances.

## Topics

### Working with media properties
- [class func canFilter(byProperty: String) -> Bool](mpmediaentity/canfilter(byproperty:).md)
  Indicates whether you can use the media property key that you specify to construct a media property predicate.
- [func enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](mpmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the given item properties.
- [var persistentID: MPMediaEntityPersistentID](mpmediaentity/persistentid.md)
  The persistent identifier for a media entity.
- [subscript(Any) -> Any?](mpmediaentity/subscript(_:).md)
  Returns the object specified by the key.
- [func value(forProperty: String) -> Any?](mpmediaentity/value(forproperty:).md)
  Retrieves the value for a specified media property key.
- [typealias MPMediaEntityPersistentID](mpmediaentitypersistentid.md)
  Defines the type for storing a persistent identifier to a particular entity.
### Media entity property keys
- [Media entity property keys](media-entity-property-keys.md)
  The property keys used to retrieve metadata for media entities.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MPMediaItem](mpmediaitem.md)
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

- [class MPMediaItem](mpmediaitem.md)
  A collection of properties that represents a single item in the media library.
- [class MPMediaItemArtwork](mpmediaitemartwork.md)
  A graphical image, such as music album cover art, associated with a media item.
- [class MPMediaItemCollection](mpmediaitemcollection.md)
  A sorted set of media items from the media library.
- [class MPMediaPlaylist](mpmediaplaylist.md)
  A playable collection of related media items.
- [class MPMediaPlaylistCreationMetadata](mpmediaplaylistcreationmetadata.md)
  A set of attributes for describing a playlist when creating it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)*