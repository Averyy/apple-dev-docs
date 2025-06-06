# addTarget(_:action:)

**Framework**: Media Player  
**Kind**: method

Adds a target object to be called when an event is received.

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
func addTarget(_ target: Any, action: Selector)
```

#### Discussion

Call the [`addTarget(_:action:)`](mpremotecommand/addtarget(_:action:).md) method multiple times to specify multiple target-action pairs. If a specific target-action pair has already been added, the request is ignored. You can add multiple actions for a single target by calling this method multiple times using the same target, but different actions.

The command object does not keep a strong reference to the target; you should remove the target before the target is deallocated.

## Parameters

- `target`: The object to receive action messages sent by the receiver when the represented remote command is triggered. The value must not be  .
- `action`: The method to be called must have the following signature:

## See Also

- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](mpremotecommand/addtarget(handler:).md)
  Adds a block to be called when an event is received.
- [func removeTarget(Any?)](mpremotecommand/removetarget(_:).md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](mpremotecommand/removetarget(_:action:).md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/addtarget(_:action:))*