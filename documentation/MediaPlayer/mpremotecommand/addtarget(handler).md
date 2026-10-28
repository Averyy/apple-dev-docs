# addTarget(handler:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) addTargetWithHandler:(MPRemoteCommandHandlerStatus (^)(MPRemoteCommandEvent *event)) handler;
```

## Return Value

An opaque object associated with the designated handler.

## Discussion

Call the [`addTarget(handler:)`](./addtarget%28handler%29.md) method to add a block to be called. Remove the handler by calling the [`removeTarget(_:)`](./removetarget%28_%29.md) method, passing in the object returned by this method.

## Parameters

- `handler`: A block object to handle the [`MPRemoteCommandEvent`](../mpremotecommandevent.md).

## See Also

### Handling events
- [func addTarget(Any, action: Selector)](./addtarget%28_,action%29.md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](./removetarget%28_%29.md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](./removetarget%28_,action%29.md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](../mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/addtarget(handler:))*