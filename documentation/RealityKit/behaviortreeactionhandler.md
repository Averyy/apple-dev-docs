# BehaviorTreeActionHandler

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

Behavior Tree-specific event handlers that allow an `ActionResult` to be returned from the handler.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol BehaviorTreeActionHandler : ActionHandlerProtocol
```

## Overview

Behavior trees send Started, Updated and Ended events. Optionally subscribe directly to any of these events in order to override default event handling in cases when conforming a new, custom event handler type.

Example:

```swift
struct MyAction: BehaviorTreeAction, Codable {
    // ...
}

struct MyActionHandler: BehaviorTreeActionHandler {
    typealias ActionType = MyAction

    //... add some optional state data here.

   // Action updated event handler.
   public mutating func actionUpdatedWithResult(event: EventType) -> ActionResult? {
       // ... handle the 'updated' event.

       // Return the action result.
       return .success
   }
}

// The handler must be registered in order to receive events:
MyActionHandler.register { event in
    return MyActionHandler()
}
```

## Topics

### Responding to action progress
- [func actionStartedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionstartedwithresult%28event%29.md)
- [func actionUpdatedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionupdatedwithresult%28event%29.md)
- [func actionPausedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionpausedwithresult%28event%29.md)
- [func actionResumedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionresumedwithresult%28event%29.md)
### Responding to action completion
- [func actionEndedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionendedwithresult%28event%29.md)
- [func actionTerminatedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionterminatedwithresult%28event%29.md)
- [func actionSkippedWithResult(event: Self.EventType) -> ActionResult?](./behaviortreeactionhandler/actionskippedwithresult%28event%29.md)

## Relationships

### Inherits From
- [ActionHandlerProtocol](./actionhandlerprotocol.md)

## See Also

### Behavior trees
- [struct BehaviorTreeComponent](./behaviortreecomponent.md)
  Manages which behavior tree is active for the component’s entity.
- [class BehaviorTreeResource](./behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeAction](./behaviortreeaction.md)
  A protocol that defines an action that a behavior tree action node can use.
- [enum ActionResult](./actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeactionhandler)*