# ActionResult

**Framework**: RealityKit  
**Kind**: enum

Status values that an action can report back to the animation system.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ActionResult
```

#### Overview

Use these values within action event handlers to communicate the state of your action logic back to the animation system.

## Topics

### Getting the action result
- [ActionResult.success](actionresult/success.md)
  The action completed successfully.
- [ActionResult.running](actionresult/running.md)
  The action is currently running.
- [ActionResult.failure](actionresult/failure.md)
  The action has failed.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct BehaviorTreeComponent](behaviortreecomponent.md)
  Manages which behavior tree is active for the component’s entity.
- [class BehaviorTreeResource](behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeAction](behaviortreeaction.md)
  A protocol that defines an action that a behavior tree action node can use.
- [protocol BehaviorTreeActionHandler](behaviortreeactionhandler.md)
  Behavior Tree-specific event handlers that allow an `ActionResult` to be returned from the handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionresult)*