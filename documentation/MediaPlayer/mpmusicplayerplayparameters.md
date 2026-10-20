# MPMusicPlayerPlayParameters

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

The MusicKit parameters that describe items to play.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class MPMusicPlayerPlayParameters
```

```objc
@interface MPMusicPlayerPlayParameters : NSObject
```

## Topics

### Creating the play parameters
- [init?(dictionary: [String : Any])](./mpmusicplayerplayparameters/init%28dictionary%29.md)
  Returns a new play parameters object using information from MusicKit.
### Accessing the play parameters
- [var dictionary: [String : Any]](./mpmusicplayerplayparameters/dictionary.md)
  The information returned from a MusicKit query and stored in a play parameters object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a new play parameters queue descriptor
- [init(playParametersQueue: [MPMusicPlayerPlayParameters])](./mpmusicplayerplayparametersqueuedescriptor/init%28playparametersqueue%29.md)
  Creates a new queue descriptor using the designated queue of play parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerplayparameters)*