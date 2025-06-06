# MPRemoteCommandHandlerStatus.deviceNotFound

**Framework**: Media Player  
**Kind**: case

The requested command couldn’t execute because a required device isn’t available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case deviceNotFound
```

#### Discussion

Commands that require a device to perform their action should return this status when the device is unavailable. For example, you’d return this status if your command requires headphones, but none are available.

## See Also

- [MPRemoteCommandHandlerStatus.success](mpremotecommandhandlerstatus/success.md)
  The requested command executed successfully.
- [MPRemoteCommandHandlerStatus.noSuchContent](mpremotecommandhandlerstatus/nosuchcontent.md)
  The requested command couldn’t execute because its required content isn’t available.
- [MPRemoteCommandHandlerStatus.noActionableNowPlayingItem](mpremotecommandhandlerstatus/noactionablenowplayingitem.md)
  The requested command couldn’t execute because no Now Playing item is available.
- [MPRemoteCommandHandlerStatus.commandFailed](mpremotecommandhandlerstatus/commandfailed.md)
  The requested command failed to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/devicenotfound)*