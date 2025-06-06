# addTarget(handler:)

**Framework**: Media Player  
**Kind**: method

Adds a block to be called when an event is received.

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
func addTarget(handler: @escaping (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any
```

#### Return Value

An opaque object associated with the designated handler.

#### Discussion

Call the [`addTarget(handler:)`](mpremotecommand/addtarget(handler:).md) method to add a block to be called. Remove the handler by calling the [`removeTarget(_:)`](mpremotecommand/removetarget(_:).md) method, passing in the object returned by this method.

## Parameters

- `handler`: A block object to handle the  .

## See Also

- [func addTarget(Any, action: Selector)](mpremotecommand/addtarget(_:action:).md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](mpremotecommand/removetarget(_:).md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](mpremotecommand/removetarget(_:action:).md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/addtarget(handler:))*