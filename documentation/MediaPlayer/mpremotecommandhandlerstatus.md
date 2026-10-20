# MPRemoteCommandHandlerStatus

**Framework**: Media Player  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of a command.

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
enum MPRemoteCommandHandlerStatus
```

```c
enum MPRemoteCommandHandlerStatus : NSInteger;
```

## Topics

### Constants
- [MPRemoteCommandHandlerStatus.success](./mpremotecommandhandlerstatus/success.md)
  The requested command executed successfully.
- [MPRemoteCommandHandlerStatus.noSuchContent](./mpremotecommandhandlerstatus/nosuchcontent.md)
  The requested command couldn’t execute because its required content isn’t available.
- [MPRemoteCommandHandlerStatus.noActionableNowPlayingItem](./mpremotecommandhandlerstatus/noactionablenowplayingitem.md)
  The requested command couldn’t execute because no Now Playing item is available.
- [MPRemoteCommandHandlerStatus.deviceNotFound](./mpremotecommandhandlerstatus/devicenotfound.md)
  The requested command couldn’t execute because a required device isn’t available.
- [MPRemoteCommandHandlerStatus.commandFailed](./mpremotecommandhandlerstatus/commandfailed.md)
  The requested command failed to execute.
### Initializers
- [init?(rawValue: Int)](./mpremotecommandhandlerstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling events
- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](./mpremotecommand/addtarget%28handler%29.md)
  Adds a block to be called when an event is received.
- [func addTarget(Any, action: Selector)](./mpremotecommand/addtarget%28_,action%29.md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](./mpremotecommand/removetarget%28_%29.md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](./mpremotecommand/removetarget%28_,action%29.md)
  Removes a target and action from a remote command object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus)*