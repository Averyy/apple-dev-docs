# withTransitionGroup(body:)

**Framework**: AVKit  
**Kind**: method

Coordinates multiple experience transitions to perform together as a single visual transition.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
nonisolated(nonsending) static func withTransitionGroup<ChildTransitionResult>(body: @_lifetime(0: copy 0) (inout AVExperienceController.TransitionGroup<ChildTransitionResult>) async -> Void) async -> [ChildTransitionResult] where ChildTransitionResult : Sendable
```

#### Return Value

An array of transition results in the order transitions were added.

#### Discussion

Use this method when you need to transition multiple [`AVExperienceController`](avexperiencecontroller.md) instances simultaneously, creating a smooth, coordinated animation.

All transitions prepare concurrently, then perform together once preparation completes. Individual transitions may succeed or fail independently — the group continues with successful transitions and collects results for all.

```swift
let results = await AVExperienceController.withTransitionGroup { group in
    for controller in controllers {
        group.addTransition {
            await controller.transition(to: .multiview)
        }
    }
}

// Check which transitions succeeded
for (index, result) in results.enumerated() {
    if case .reversed(let reason) = result {
        print("Controller \(index) failed: \(reason)")
    }
}
```

## Parameters

- `body`: A closure that adds transitions to the group using `addTransition(operation:)`.

## See Also

- [AVExperienceController.TransitionGroup](avexperiencecontroller/transitiongroup.md)
  A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition.
- [func transition(to: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transition(to:).md)
  Transitions the video to a different experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/withtransitiongroup(body:))*