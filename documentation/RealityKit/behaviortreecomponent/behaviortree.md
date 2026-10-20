# behaviorTree

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

Accesses the current behavior tree. Note that setting the behavior tree to a tree not in `availableBehaviorTrees` will add a uniquely-named entry for the tree in `availableBehaviorTrees`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var behaviorTree: BehaviorTreeResource? { get set }
```

## See Also

### Accessing behavior trees
- [var availableBehaviorTrees: [String : BehaviorTreeResource]](./availablebehaviortrees.md)
  All the behavior trees that this component can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreecomponent/behaviortree)*