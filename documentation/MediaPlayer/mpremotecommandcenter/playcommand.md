# playCommand

**Framework**: Media Player  
**Kind**: property

The command object for starting playback of the current item.

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
var playCommand: MPRemoteCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for pausing the currently playing track. In your handler, play the current item from the point at which the track was paused, or from the beginning if the item was not paused. You can disable the command if your app does not support it.

## See Also

- [var pauseCommand: MPRemoteCommand](mpremotecommandcenter/pausecommand.md)
  The command object for pausing playback of the current item.
- [var stopCommand: MPRemoteCommand](mpremotecommandcenter/stopcommand.md)
  The command object for stopping playback of the current item.
- [var togglePlayPauseCommand: MPRemoteCommand](mpremotecommandcenter/toggleplaypausecommand.md)
  The command object for toggling between playing and pausing the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/playcommand)*