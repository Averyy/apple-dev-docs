# addTransition(operation:)

**Framework**: AVKit  
**Kind**: method

Adds a transition to the group, suspending it until all transitions are ready to run together.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func addTransition(operation: sending @escaping @isolated(any) () async -> ChildTransitionResult)
```

#### Discussion

Call [`transition(to:)`](avexperiencecontroller/transition(to:).md) on an [`AVExperienceController`](avexperiencecontroller.md) within the operation closure. The transition suspends until all transitions have been added to the group, then perform together with the others.

[`withTransitionGroup(body:)`](avexperiencecontroller/withtransitiongroup(body:).md) includes the value you return from the closure in the order transitions were added.

```swift
group.addTransition {
    await controller.transition(to: .multiview)
}
```

## Parameters

- `operation`: A closure that performs a transition and returns a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitiongroup/addtransition(operation:))*