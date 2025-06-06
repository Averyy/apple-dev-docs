# removeTarget(_:)

**Framework**: Media Player  
**Kind**: method

Removes a target from the remote command object.

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
func removeTarget(_ target: Any?)
```

#### Discussion

Call the [`removeTarget(_:)`](mpremotecommand/removetarget(_:).md) method to remove the specified target and all actions associated with the target.

## Parameters

- `target`: The object that currently is a recipient of action messages sent by this object. Specify   to remove all targets.

## See Also

- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](mpremotecommand/addtarget(handler:).md)
  Adds a block to be called when an event is received.
- [func addTarget(Any, action: Selector)](mpremotecommand/addtarget(_:action:).md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any, action: Selector?)](mpremotecommand/removetarget(_:action:).md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/removetarget(_:))*