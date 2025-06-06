# togglePlayPauseCommand

**Framework**: Media Player  
**Kind**: property

The command object for toggling between playing and pausing the current item.

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
var togglePlayPauseCommand: MPRemoteCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for toggling between playing and pausing the current track. In your handler, perform the appropriate task based on the current state of the media item. If the item is currently playing, pause it. If it is paused, resume playing it. You can disable the command if your app does not support it.

## See Also

- [var pauseCommand: MPRemoteCommand](mpremotecommandcenter/pausecommand.md)
  The command object for pausing playback of the current item.
- [var playCommand: MPRemoteCommand](mpremotecommandcenter/playcommand.md)
  The command object for starting playback of the current item.
- [var stopCommand: MPRemoteCommand](mpremotecommandcenter/stopcommand.md)
  The command object for stopping playback of the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/toggleplaypausecommand)*