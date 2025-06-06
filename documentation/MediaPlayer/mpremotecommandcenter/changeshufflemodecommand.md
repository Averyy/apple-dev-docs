# changeShuffleModeCommand

**Framework**: Media Player  
**Kind**: property

The command object for changing the shuffle mode.

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
var changeShuffleModeCommand: MPChangeShuffleModeCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for changing the shuffle mode for the playlist. In your handler, change the shuffle mode to the new value. You can disable the command if your app does not support it.

## See Also

- [var nextTrackCommand: MPRemoteCommand](mpremotecommandcenter/nexttrackcommand.md)
  The command object for selecting the next track.
- [var previousTrackCommand: MPRemoteCommand](mpremotecommandcenter/previoustrackcommand.md)
  The command object for selecting the previous track.
- [var changeRepeatModeCommand: MPChangeRepeatModeCommand](mpremotecommandcenter/changerepeatmodecommand.md)
  The command object for changing the repeat mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/changeshufflemodecommand)*