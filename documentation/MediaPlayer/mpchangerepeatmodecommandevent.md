# MPChangeRepeatModeCommandEvent

**Framework**: Media Player  
**Kind**: class

An event requesting a change in the repeat mode.

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
class MPChangeRepeatModeCommandEvent
```

## Topics

### Changing the repeat type
- [var repeatType: MPRepeatType](mpchangerepeatmodecommandevent/repeattype.md)
  The repeat type used when fulfilling the event request.
- [var preservesRepeatMode: Bool](mpchangerepeatmodecommandevent/preservesrepeatmode.md)
  A Boolean value that indicates whether the chosen repeat mode is preserved between playback sessions.

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

- [class MPChangePlaybackRateCommand](mpchangeplaybackratecommand.md)
  An object that responds to requests to change the playback rate of the playing item.
- [class MPChangePlaybackRateCommandEvent](mpchangeplaybackratecommandevent.md)
  An event requesting a change in the playback rate.
- [class MPChangeLanguageOptionCommandEvent](mpchangelanguageoptioncommandevent.md)
  An event requesting a change in the language option.
- [class MPChangeRepeatModeCommand](mpchangerepeatmodecommand.md)
  An object that responds to requests to change the current repeat mode used during playback.
- [class MPChangeShuffleModeCommand](mpchangeshufflemodecommand.md)
  An object that responds to requests to change the current shuffle mode used during playback.
- [class MPChangeShuffleModeCommandEvent](mpchangeshufflemodecommandevent.md)
  An event requesting a change in the shuffle mode.
- [enum MPRepeatType](mprepeattype.md)
  Indicates which items to play repeatedly.
- [enum MPShuffleType](mpshuffletype.md)
  Indicates which item types to shuffle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent)*