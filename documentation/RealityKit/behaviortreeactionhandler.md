# BehaviorTreeActionHandler

**Framework**: RealityKit  
**Kind**: protocol

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
- [class BehaviorTreeResource](behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeAction](behaviortreeaction.md)
- [enum ActionResult](actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeactionhandler)*