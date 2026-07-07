# BehaviorTreeActionHandler

**Framework**: RealityKit  
**Kind**: protocol

Behavior Tree-specific event handlers that allow an `ActionResult` to be returned from the handler.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol BehaviorTreeActionHandler : ActionHandlerProtocol
```

#### Overview

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
- [func actionStartedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionstartedwithresult(event:).md)
- [func actionUpdatedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionupdatedwithresult(event:).md)
- [func actionPausedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionpausedwithresult(event:).md)
- [func actionResumedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionresumedwithresult(event:).md)
### Responding to action completion
- [func actionEndedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionendedwithresult(event:).md)
- [func actionTerminatedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionterminatedwithresult(event:).md)
- [func actionSkippedWithResult(event: Self.EventType) -> ActionResult?](behaviortreeactionhandler/actionskippedwithresult(event:).md)

## Relationships

### Inherits From
- [ActionHandlerProtocol](actionhandlerprotocol.md)

## See Also

- [struct BehaviorTreeComponent](behaviortreecomponent.md)
  Manages which behavior tree is active for the component’s entity.
- [class BehaviorTreeResource](behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeAction](behaviortreeaction.md)
  A protocol that defines an action that a behavior tree action node can use.
- [enum ActionResult](actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeactionhandler)*