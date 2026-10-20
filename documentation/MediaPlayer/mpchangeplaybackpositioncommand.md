# MPChangePlaybackPositionCommand

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

An object that responds to requests to change the current playback position of the playing item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPChangePlaybackPositionCommand
```

```objc
@interface MPChangePlaybackPositionCommand : MPRemoteCommand
```

## Relationships

### Inherits From
- [MPRemoteCommand](./mpremotecommand.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to track navigation events
- [class MPChangePlaybackPositionCommandEvent](./mpchangeplaybackpositioncommandevent.md)
  An event requesting a change in the playback position.
- [class MPSeekCommandEvent](./mpseekcommandevent.md)
  An event requesting that the player seek to a new position.
- [class MPSkipIntervalCommand](./mpskipintervalcommand.md)
  An object that defines the skip intervals for the player.
- [class MPSkipIntervalCommandEvent](./mpskipintervalcommandevent.md)
  An event requesting a change in the current skip interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommand)*