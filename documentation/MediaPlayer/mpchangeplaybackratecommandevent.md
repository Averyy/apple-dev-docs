# MPChangePlaybackRateCommandEvent

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

An event requesting a change in the playback rate.

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
class MPChangePlaybackRateCommandEvent
```

```objc
@interface MPChangePlaybackRateCommandEvent : MPRemoteCommandEvent
```

## Topics

### Retrieving the playback rate
- [var playbackRate: Float](./mpchangeplaybackratecommandevent/playbackrate.md)
  The chosen playback rate for the command event.

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

### Responding to changes to media playback mode events
- [class MPChangePlaybackRateCommand](./mpchangeplaybackratecommand.md)
  An object that responds to requests to change the playback rate of the playing item.
- [class MPChangeLanguageOptionCommandEvent](./mpchangelanguageoptioncommandevent.md)
  An event requesting a change in the language option.
- [class MPChangeRepeatModeCommand](./mpchangerepeatmodecommand.md)
  An object that responds to requests to change the current repeat mode used during playback.
- [class MPChangeRepeatModeCommandEvent](./mpchangerepeatmodecommandevent.md)
  An event requesting a change in the repeat mode.
- [class MPChangeShuffleModeCommand](./mpchangeshufflemodecommand.md)
  An object that responds to requests to change the current shuffle mode used during playback.
- [class MPChangeShuffleModeCommandEvent](./mpchangeshufflemodecommandevent.md)
  An event requesting a change in the shuffle mode.
- [enum MPRepeatType](./mprepeattype.md)
  Indicates which items to play repeatedly.
- [enum MPShuffleType](./mpshuffletype.md)
  Indicates which item types to shuffle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommandevent)*