# addTarget(_:action:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addTarget:(id) target action:(SEL) action;
```

## Discussion

Call the [`addTarget(_:action:)`](./addtarget%28_,action%29.md) method multiple times to specify multiple target-action pairs. If a specific target-action pair has already been added, the request is ignored. You can add multiple actions for a single target by calling this method multiple times using the same target, but different actions.

The command object does not keep a strong reference to the target; you should remove the target before the target is deallocated.

## Parameters

- `target`: The object to receive action messages sent by the receiver when the represented remote command is triggered. The value must not be `nil`.
- `action`: A selector identifying the method on the target to be called. The value must not be `NULL`.

  The method to be called must have the following signature:

  ```objc
  - (MPRemoteCommandHandlerStatus) handleCommand: (MPRemoteCommandEvent*) event;
  ```

## See Also

### Handling events
- [func addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](./addtarget%28handler%29.md)
  Adds a block to be called when an event is received.
- [func removeTarget(Any?)](./removetarget%28_%29.md)
  Removes a target from the remote command object.
- [func removeTarget(Any, action: Selector?)](./removetarget%28_,action%29.md)
  Removes a target and action from a remote command object.
- [enum MPRemoteCommandHandlerStatus](../mpremotecommandhandlerstatus.md)
  Constants indicating the status of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/addtarget(_:action:))*