# MPChangeRepeatModeCommand

**Framework**: Media Player  
**Kind**: class

An object that responds to requests to change the current repeat mode used during playback.

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
class MPChangeRepeatModeCommand
```

## Topics

### Retrieving the current repeat option
- [var currentRepeatType: MPRepeatType](mpchangerepeatmodecommand/currentrepeattype.md)
  The current repeat option for a media item.

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

- [class MPChangePlaybackRateCommand](mpchangeplaybackratecommand.md)
  An object that responds to requests to change the playback rate of the playing item.
- [class MPChangePlaybackRateCommandEvent](mpchangeplaybackratecommandevent.md)
  An event requesting a change in the playback rate.
- [class MPChangeLanguageOptionCommandEvent](mpchangelanguageoptioncommandevent.md)
  An event requesting a change in the language option.
- [class MPChangeRepeatModeCommandEvent](mpchangerepeatmodecommandevent.md)
  An event requesting a change in the repeat mode.
- [class MPChangeShuffleModeCommand](mpchangeshufflemodecommand.md)
  An object that responds to requests to change the current shuffle mode used during playback.
- [class MPChangeShuffleModeCommandEvent](mpchangeshufflemodecommandevent.md)
  An event requesting a change in the shuffle mode.
- [enum MPRepeatType](mprepeattype.md)
  Indicates which items to play repeatedly.
- [enum MPShuffleType](mpshuffletype.md)
  Indicates which item types to shuffle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand)*