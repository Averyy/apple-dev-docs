# MPRemoteCommandHandlerStatus.commandFailed

**Framework**: Media Player  
**Kind**: case  
**Role**: Case

The requested command failed to execute.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case commandFailed
```

```c
MPRemoteCommandHandlerStatusCommandFailed
```

## See Also

### Constants
- [MPRemoteCommandHandlerStatus.success](./success.md)
  The requested command executed successfully.
- [MPRemoteCommandHandlerStatus.noSuchContent](./nosuchcontent.md)
  The requested command couldn’t execute because its required content isn’t available.
- [MPRemoteCommandHandlerStatus.noActionableNowPlayingItem](./noactionablenowplayingitem.md)
  The requested command couldn’t execute because no Now Playing item is available.
- [MPRemoteCommandHandlerStatus.deviceNotFound](./devicenotfound.md)
  The requested command couldn’t execute because a required device isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/commandfailed)*