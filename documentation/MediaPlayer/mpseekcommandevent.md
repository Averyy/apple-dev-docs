# MPSeekCommandEvent

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSeekCommandEvent : MPRemoteCommandEvent
```

## Topics

### Changing the current seek behavior
- [var type: MPSeekCommandEventType](./mpseekcommandevent/type.md)
  The type of seek command event.
### Constants
- [enum MPSeekCommandEventType](./mpseekcommandeventtype.md)
  Defines the beginning and ending of seek events.

## Relationships

### Inherits From
- [MPRemoteCommandEvent](./mpremotecommandevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to track navigation events
- [class MPChangePlaybackPositionCommand](./mpchangeplaybackpositioncommand.md)
  An object that responds to requests to change the current playback position of the playing item.
- [class MPChangePlaybackPositionCommandEvent](./mpchangeplaybackpositioncommandevent.md)
  An event requesting a change in the playback position.
- [class MPSkipIntervalCommand](./mpskipintervalcommand.md)
  An object that defines the skip intervals for the player.
- [class MPSkipIntervalCommandEvent](./mpskipintervalcommandevent.md)
  An event requesting a change in the current skip interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpseekcommandevent)*