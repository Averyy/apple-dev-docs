# BehaviorTreeAction

**Framework**: RealityKit  
**Kind**: protocol

A protocol that defines an action that a behavior tree action node can use.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol BehaviorTreeAction : EntityAction
```

#### Overview

Conform to this protocol as:

```swift
struct CustomBehaviorTreeAction: BehaviorTreeAction, Codable {

    public var isReversible: Bool { false }
    public var isAdditive: Bool { false }
    public var animatedValueType: (any AnimatableData.Type)? { nil }

    // Add your action-specific properties, functions and subscriptions here.
}
```

## Topics

### Subscribing to events
- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> ActionResult)](behaviortreeaction/subscribe(to:_:)-9mrvx.md)
  Subscribes to a serializable action event and returns a `ActionResult`.
- [static func subscribe(to: ActionEventType, (ActionEvent<Self>) -> Void)](behaviortreeaction/subscribe(to:_:)-3p0pj.md)
  Shadows the `EntityAction.subscribe(to:_:)` overload that takes a `-> Void` closure.
### Type Methods
- [static subscribe(to:_:)](behaviortreeaction/subscribe(to:_:).md)
  Subscribes to a serializable action event and returns a `ActionResult`.

## Relationships

### Inherits From
- [EntityAction](entityaction.md)

## See Also

- [struct BehaviorTreeComponent](behaviortreecomponent.md)
  Manages which behavior tree is active for the component’s entity.
- [class BehaviorTreeResource](behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeActionHandler](behaviortreeactionhandler.md)
  Behavior Tree-specific event handlers that allow an `ActionResult` to be returned from the handler.
- [enum ActionResult](actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeaction)*