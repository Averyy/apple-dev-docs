# nextTrackCommand

**Framework**: Media Player  
**Kind**: property

The command object for selecting the next track.

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
var nextTrackCommand: MPRemoteCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for selecting the next track. In your handler, select the media item that follows the current media item. You can disable the command if your app does not support it.

## See Also

- [var previousTrackCommand: MPRemoteCommand](mpremotecommandcenter/previoustrackcommand.md)
  The command object for selecting the previous track.
- [var changeRepeatModeCommand: MPChangeRepeatModeCommand](mpremotecommandcenter/changerepeatmodecommand.md)
  The command object for changing the repeat mode.
- [var changeShuffleModeCommand: MPChangeShuffleModeCommand](mpremotecommandcenter/changeshufflemodecommand.md)
  The command object for changing the shuffle mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/nexttrackcommand)*