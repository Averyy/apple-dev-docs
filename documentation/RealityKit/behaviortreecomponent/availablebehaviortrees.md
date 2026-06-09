# availableBehaviorTrees

**Framework**: RealityKit  
**Kind**: property

All the behavior trees that this component can access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var availableBehaviorTrees: [String : BehaviorTreeResource] { get set }
```

## See Also

- [var behaviorTree: BehaviorTreeResource?](behaviortreecomponent/behaviortree.md)
  Accesses the current behavior tree. Note that setting the behavior tree to a tree not in `availableBehaviorTrees` will add a uniquely-named entry for the tree in `availableBehaviorTrees`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreecomponent/availablebehaviortrees)*