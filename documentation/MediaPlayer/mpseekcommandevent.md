# MPSeekCommandEvent

**Framework**: Media Player  
**Kind**: class

An event requesting that the player seek to a new position.

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
class MPSeekCommandEvent
```

## Topics

### Changing the current seek behavior
- [var type: MPSeekCommandEventType](mpseekcommandevent/type.md)
  The type of seek command event.
### Constants
- [enum MPSeekCommandEventType](mpseekcommandeventtype.md)
  Defines the beginning and ending of seek events.

## Relationships

### Inherits From
- [MPRemoteCommandEvent](mpremotecommandevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPChangePlaybackPositionCommand](mpchangeplaybackpositioncommand.md)
  An object that responds to requests to change the current playback position of the playing item.
- [class MPChangePlaybackPositionCommandEvent](mpchangeplaybackpositioncommandevent.md)
  An event requesting a change in the playback position.
- [class MPSkipIntervalCommand](mpskipintervalcommand.md)
  An object that defines the skip intervals for the player.
- [class MPSkipIntervalCommandEvent](mpskipintervalcommandevent.md)
  An event requesting a change in the current skip interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpseekcommandevent)*