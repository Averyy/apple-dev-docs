# INMediaItem

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes a piece of media content, such as a song, TV show, artist, or podcast playlist.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INMediaItem
```

```objc
@interface INMediaItem : NSObject
```

## Topics

### Creating a Media Item
- [convenience init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?)](./inmediaitem/init%28identifier,title,type,artwork%29.md)
  Creates a media item with an identifier, title, type, and artwork.
- [init(identifier: String?, title: String?, type: INMediaItemType, artwork: INImage?, artist: String?)](./inmediaitem/init%28identifier,title,type,artwork,artist%29.md)
  Creates a media item with an identifier, title, type, artwork, and artist.
### Describing the Media Item
- [var artwork: INImage?](./inmediaitem/artwork.md)
  Artwork for the media item.
- [var identifier: String?](./inmediaitem/identifier.md)
  The value your app uses to identify the media item.
- [var title: String?](./inmediaitem/title.md)
  The media item title.
- [var artist: String?](./inmediaitem/artist.md)
  The artist associated with the media item.
- [var type: INMediaItemType](./inmediaitem/type.md)
  The media item type.
- [enum INMediaItemType](./inmediaitemtype.md)
  The type of content the media item describes.
### Initializers
- [init?(coder: NSCoder)](./inmediaitem/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Data Objects
- [class INMediaSearch](./inmediasearch.md)
  An object that describes a media type to search for, such as a station name, song name, or album name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitem)*