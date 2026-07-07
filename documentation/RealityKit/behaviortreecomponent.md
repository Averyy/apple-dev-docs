# BehaviorTreeComponent

**Framework**: RealityKit  
**Kind**: struct

Manages which behavior tree is active for the component’s entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BehaviorTreeComponent
```

## Topics

### Creating a behavior tree component
- [init(behaviorTree: BehaviorTreeResource?, availableBehaviorTrees: [String : BehaviorTreeResource])](behaviortreecomponent/init(behaviortree:availablebehaviortrees:).md)
### Accessing behavior trees
- [var behaviorTree: BehaviorTreeResource?](behaviortreecomponent/behaviortree.md)
  Accesses the current behavior tree. Note that setting the behavior tree to a tree not in `availableBehaviorTrees` will add a uniquely-named entry for the tree in `availableBehaviorTrees`.
- [var availableBehaviorTrees: [String : BehaviorTreeResource]](behaviortreecomponent/availablebehaviortrees.md)
  All the behavior trees that this component can access.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class BehaviorTreeResource](behaviortreeresource.md)
  An immutable representation of a behavior tree.
- [protocol BehaviorTreeAction](behaviortreeaction.md)
  A protocol that defines an action that a behavior tree action node can use.
- [protocol BehaviorTreeActionHandler](behaviortreeactionhandler.md)
  Behavior Tree-specific event handlers that allow an `ActionResult` to be returned from the handler.
- [enum ActionResult](actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreecomponent)*