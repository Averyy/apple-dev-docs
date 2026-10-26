# INMediaDestinationReference

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes the destination for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INMediaDestinationReference
```

```objc
@interface INMediaDestination : NSObject
```

## Topics

### Creating a Media Destination Object
- [class func library() -> Self](./inmediadestinationreference/library%28%29.md)
  Creates a new library destination for the media item.
- [class func playlistDestination(withName: String) -> Self](./inmediadestinationreference/playlistdestination%28withname%29.md)
  Creates a new playlist destination for the media item.
### Describing the Media Destination
- [var playlistName: String?](./inmediadestinationreference/playlistname.md)
  The name of the playlist to which you add the media.
- [var mediaDestinationType: INMediaDestinationType](./inmediadestinationreference/mediadestinationtype.md)
  The destination of the media your app adds.
- [enum INMediaDestinationType](./inmediadestinationtype.md)
  Constants that describe the different media destination types.
### Initializers
- [init?(coder: NSCoder)](./inmediadestinationreference/init%28coder%29.md)

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

### Accessing the Media
- [var mediaItems: [INMediaItem]?](./inaddmediaintent/mediaitems.md)
  The media content to add.
- [var mediaSearch: INMediaSearch?](./inaddmediaintent/mediasearch.md)
  The location to search for the media item to add.
- [var mediaDestination: INMediaDestination?](./inaddmediaintent/mediadestination.md)
  The location for the media to add.
- [enum INMediaDestination](./inmediadestination-swift.enum.md)
  An object that describes the destination for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationreference)*