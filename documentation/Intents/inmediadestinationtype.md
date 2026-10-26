# INMediaDestinationType

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the different media destination types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INMediaDestinationType
```

```c
enum INMediaDestinationType : NSInteger;
```

## Topics

### Constants
- [INMediaDestinationType.unknown](./inmediadestinationtype/unknown.md)
  A type where the media destination is unknown.
- [INMediaDestinationType.library](./inmediadestinationtype/library.md)
  A type where the media destination is a library.
- [INMediaDestinationType.playlist](./inmediadestinationtype/playlist.md)
  A type where the media destination is a playlist.
### Initializers
- [init?(rawValue: Int)](./inmediadestinationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Describing the Media Destination
- [var playlistName: String?](./inmediadestinationreference/playlistname.md)
  The name of the playlist to which you add the media.
- [var mediaDestinationType: INMediaDestinationType](./inmediadestinationreference/mediadestinationtype.md)
  The destination of the media your app adds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediadestinationtype)*