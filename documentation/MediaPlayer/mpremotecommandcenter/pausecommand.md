# pauseCommand

**Framework**: Media Player  
**Kind**: property

The command object for pausing playback of the current item.

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
var pauseCommand: MPRemoteCommand { get }
```

#### Discussion

Use the object in this property to register your app’s handler for pausing the currently playing track. In your handler, pause playback of the current item but maintain the current play position. You can disable the command if your app does not support it.

## See Also

- [var playCommand: MPRemoteCommand](mpremotecommandcenter/playcommand.md)
  The command object for starting playback of the current item.
- [var stopCommand: MPRemoteCommand](mpremotecommandcenter/stopcommand.md)
  The command object for stopping playback of the current item.
- [var togglePlayPauseCommand: MPRemoteCommand](mpremotecommandcenter/toggleplaypausecommand.md)
  The command object for toggling between playing and pausing the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/pausecommand)*