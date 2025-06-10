# MPRepeatType

**Framework**: Media Player  
**Kind**: enum

Indicates which items to play repeatedly.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MPRepeatType
```

## Topics

### Repeat types
- [MPRepeatType.off](mprepeattype/off.md)
  Nothing is repeated during playback.
- [MPRepeatType.one](mprepeattype/one.md)
  A single item is repeated indefinitely.
- [MPRepeatType.all](mprepeattype/all.md)
  The current container or playlist is repeated indefinitely.
### Initializers
- [init?(rawValue: Int)](mprepeattype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MPChangePlaybackRateCommand](mpchangeplaybackratecommand.md)
  An object that responds to requests to change the playback rate of the playing item.
- [class MPChangePlaybackRateCommandEvent](mpchangeplaybackratecommandevent.md)
  An event requesting a change in the playback rate.
- [class MPChangeLanguageOptionCommandEvent](mpchangelanguageoptioncommandevent.md)
  An event requesting a change in the language option.
- [class MPChangeRepeatModeCommand](mpchangerepeatmodecommand.md)
  An object that responds to requests to change the current repeat mode used during playback.
- [class MPChangeRepeatModeCommandEvent](mpchangerepeatmodecommandevent.md)
  An event requesting a change in the repeat mode.
- [class MPChangeShuffleModeCommand](mpchangeshufflemodecommand.md)
  An object that responds to requests to change the current shuffle mode used during playback.
- [class MPChangeShuffleModeCommandEvent](mpchangeshufflemodecommandevent.md)
  An event requesting a change in the shuffle mode.
- [enum MPShuffleType](mpshuffletype.md)
  Indicates which item types to shuffle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mprepeattype)*