# availableBehaviorTrees

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

All the behavior trees that this component can access.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var availableBehaviorTrees: [String : BehaviorTreeResource] { get set }
```

## See Also

### Accessing behavior trees
- [var behaviorTree: BehaviorTreeResource?](./behaviortree.md)
  Accesses the current behavior tree. Note that setting the behavior tree to a tree not in `availableBehaviorTrees` will add a uniquely-named entry for the tree in `availableBehaviorTrees`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreecomponent/availablebehaviortrees)*