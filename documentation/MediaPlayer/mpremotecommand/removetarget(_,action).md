# removeTarget(_:action:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Removes a target and action from a remote command object.

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
func removeTarget(_ target: Any, action: Selector?)
```

```objc
- (void) removeTarget:(id) target action:(SEL) action;
```

## Discussion

Call the [`removeTarget(_:action:)`](./removetarget%28_,action%29.md) method to remove the specified target-action pair. Passing `nil` for `target` matches all targets and passing `NULL` for `action` matches all actions.

## Parameters

- `target`: The object that currently is a recipient of action messages sent by this object. Specify `nil` to remove all targets.
- `action`: A selector identifying a method on the target. Specify `NULL` to remove all actions.

## See Also

### Handling events
- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](./addtarget%28handler%29.md)
  Adds a block to be called when an event is received.
- [func addTarget(Any, action: Selector)](./addtarget%28_,action%29.md)
  Adds a target object to be called when an event is received.
- [func removeTarget(Any?)](./removetarget%28_%29.md)
  Removes a target from the remote command object.
- [enum MPRemoteCommandHandlerStatus](../mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/removetarget(_:action:))*