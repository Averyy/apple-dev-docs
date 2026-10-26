# INAddMediaMediaDestinationUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Reasons describing why the destination is not supported.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INAddMediaMediaDestinationUnsupportedReason
```

```c
enum INAddMediaMediaDestinationUnsupportedReason : NSInteger;
```

## Topics

### Reasons
- [INAddMediaMediaDestinationUnsupportedReason.playlistNameNotFound](./inaddmediamediadestinationunsupportedreason/playlistnamenotfound.md)
  The app was unable to find a playlist with that name.
- [INAddMediaMediaDestinationUnsupportedReason.playlistNotEditable](./inaddmediamediadestinationunsupportedreason/playlistnoteditable.md)
  The user can’t modify the destination playlist.
### Initializers
- [init?(rawValue: Int)](./inaddmediamediadestinationunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result
- [init(mediaDestinationResolutionResult: INMediaDestinationResolutionResult)](./inaddmediamediadestinationresolutionresult/init%28mediadestinationresolutionresult%29.md)
  Creates an object whose resolution involves successfully adding a media item to a particular destination.
- [class func unsupported(forReason: INAddMediaMediaDestinationUnsupportedReason) -> Self](./inaddmediamediadestinationresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the media destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediadestinationunsupportedreason)*