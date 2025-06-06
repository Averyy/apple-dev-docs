# MPChangePlaybackPositionCommandEvent

**Framework**: Media Player  
**Kind**: class

An event requesting a change in the playback position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPChangePlaybackPositionCommandEvent
```

## Topics

### Retrieving the position time
- [var positionTime: TimeInterval](mpchangeplaybackpositioncommandevent/positiontime.md)
  The playback position used when setting the current time of the player.

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
- [class MPSeekCommandEvent](mpseekcommandevent.md)
  An event requesting that the player seek to a new position.
- [class MPSkipIntervalCommand](mpskipintervalcommand.md)
  An object that defines the skip intervals for the player.
- [class MPSkipIntervalCommandEvent](mpskipintervalcommandevent.md)
  An event requesting a change in the current skip interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommandevent)*