# behaviorTree

**Framework**: RealityKit  
**Kind**: property

Accesses the current behavior tree. Note that setting the behavior tree to a tree not in `availableBehaviorTrees` will add a uniquely-named entry for the tree in `availableBehaviorTrees`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var behaviorTree: BehaviorTreeResource? { get set }
```

## See Also

- [var availableBehaviorTrees: [String : BehaviorTreeResource]](behaviortreecomponent/availablebehaviortrees.md)
  All the behavior trees that this component can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreecomponent/behaviortree)*