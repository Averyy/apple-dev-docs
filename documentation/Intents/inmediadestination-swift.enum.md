# INMediaDestination

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

An object that describes the destination for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 14.0+
- watchOS 6.0+

## Declaration

```swift
enum INMediaDestination
```

## Topics

### Specifying the Destination
- [INMediaDestination.library](./inmediadestination-swift.enum/library.md)
  The library destination.
- [INMediaDestination.playlist(_:)](./inmediadestination-swift.enum/playlist%28_%29.md)
  The destination playlist.
### Getting the Playlist Name
- [var playlistName: String?](./inmediadestination-swift.enum/playlistname.md)
  The name of the destination playlist.
### Using Reference Types
- [class INMediaDestinationReference](./inmediadestinationreference.md)
  An object that describes the destination for a media item.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [ReferenceConvertible](../Foundation/referenceconvertible.md)

## See Also

### Accessing the Media
- [var mediaItems: [INMediaItem]?](./inaddmediaintent/mediaitems.md)
  The media content to add.
- [var mediaSearch: INMediaSearch?](./inaddmediaintent/mediasearch.md)
  The location to search for the media item to add.
- [var mediaDestination: INMediaDestination?](./inaddmediaintent/mediadestination.md)
  The location for the media to add.
- [class INMediaDestinationReference](./inmediadestinationreference.md)
  An object that describes the destination for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestination-swift.enum)*