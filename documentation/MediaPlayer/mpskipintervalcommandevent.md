# MPSkipIntervalCommandEvent

**Framework**: Media Player  
**Kind**: class

An event requesting a change in the current skip interval.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPSkipIntervalCommandEvent
```

## Topics

### Retrieving the skip interval
- [var interval: TimeInterval](mpskipintervalcommandevent/interval.md)
  The chosen interval, in seconds, for the skip command event.

## Relationships

### Inherits From
- [MPRemoteCommandEvent](mpremotecommandevent.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MPChangePlaybackPositionCommand](mpchangeplaybackpositioncommand.md)
  An object that responds to requests to change the current playback position of the playing item.
- [class MPChangePlaybackPositionCommandEvent](mpchangeplaybackpositioncommandevent.md)
  An event requesting a change in the playback position.
- [class MPSeekCommandEvent](mpseekcommandevent.md)
  An event requesting that the player seek to a new position.
- [class MPSkipIntervalCommand](mpskipintervalcommand.md)
  An object that defines the skip intervals for the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent)*