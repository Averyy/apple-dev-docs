# MPSkipIntervalCommand

**Framework**: Media Player  
**Kind**: class

An object that defines the skip intervals for the player.

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
class MPSkipIntervalCommand
```

#### Overview

You use a skip interval to move the playback of a media item, forward or backward, the indicated number of seconds. For example, a forward skip interval of 30 seconds at 2 minutes and 30 seconds into a song would immediately jump to 3 minutes into the song and continue playing. The skipped content isn’t played.

## Topics

### Retrieving skip intervals
- [var preferredIntervals: [NSNumber]](mpskipintervalcommand/preferredintervals.md)
  The available skip intervals, in seconds, for a media item.

## Relationships

### Inherits From
- [MPRemoteCommand](mpremotecommand.md)
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
- [class MPSeekCommandEvent](mpseekcommandevent.md)
  An event requesting that the player seek to a new position.
- [class MPSkipIntervalCommandEvent](mpskipintervalcommandevent.md)
  An event requesting a change in the current skip interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand)*