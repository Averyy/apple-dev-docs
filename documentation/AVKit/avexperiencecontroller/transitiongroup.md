# AVExperienceController.TransitionGroup

**Framework**: AVKit  
**Kind**: struct

A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TransitionGroup<ChildTransitionResult> where ChildTransitionResult : Sendable
```

#### Overview

Use [`withTransitionGroup(body:)`](avexperiencecontroller/withtransitiongroup(body:).md) to create a transition group. Add transitions using [`addTransition(operation:)`](avexperiencecontroller/transitiongroup/addtransition(operation:).md), and they perform together once all have been added and prepared.

Transitions in a group prepare concurrently, then perform their animations simultaneously, creating a single cohesive visual transition. Each transition completes with its own result, allowing you to handle individual successes and failures.

#### Handle Failures

Individual transitions may fail during preparation or execution without affecting other transitions in the group.

## Topics

### Adding transitions
- [func addTransition(operation: sending () async -> ChildTransitionResult)](avexperiencecontroller/transitiongroup/addtransition(operation:).md)
  Adds a transition to the group, suspending it until all transitions are ready to run together.

## See Also

- [static func withTransitionGroup<ChildTransitionResult>(body: (inout AVExperienceController.TransitionGroup<ChildTransitionResult>) async -> Void) async -> [ChildTransitionResult]](avexperiencecontroller/withtransitiongroup(body:).md)
  Coordinates multiple experience transitions to perform together as a single visual transition.
- [func transition(to: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transition(to:).md)
  Transitions the video to a different experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitiongroup)*