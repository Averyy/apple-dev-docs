# transition(to:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Transitions the video to a different experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor final func transition(to toExperience: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult
```

## Return Value

A transition result.

## Discussion

Call this method to transition to a different experience such as [`AVExperienceController.Experience.expanded`](./experience-swift.enum/expanded.md). When you initiate a transition, the system calls the experience controller’s delegate methods so your app can respond to experience changes.

You determine the success of a transition by evaluating the [`AVExperienceController.TransitionContext.TransitionResult`](./transitioncontext/transitionresult.md) this method returns. A transition result of [`AVExperienceController.TransitionContext.TransitionResult.completed`](./transitioncontext/transitionresult/completed.md) indicates a successful transition, in which case the system updates the [`experience`](./experience-swift.property.md) property to the new experience. A transition result of [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](./transitioncontext/transitionresult/reversed%28reason%29.md) indicates a failed transition. Evaluate the result’s [`AVExperienceController.TransitionContext.ReversedReason`](./transitioncontext/reversedreason.md) to determine why the transition failed. A failure that occurs before the transition begins results in the system not invoking any delegate callback methods. If the failure happens after the callback to  [`experienceController(_:prepareForTransitionUsing:)`](./delegate-swift.protocol/experiencecontroller%28_,preparefortransitionusing%29.md) occurs, the transition context changes to [`AVExperienceController.TransitionContext.Status.finished(result:)`](./transitioncontext/status-swift.enum/finished%28result%29.md).

## Parameters

- `toExperience`: The experience to transition to.

## See Also

### Transitioning experiences
- [AVExperienceController.TransitionGroup](./transitiongroup.md)
  A group of experience transitions that prepare concurrently and run simultaneously as a single visual transition.
- [static func withTransitionGroup<ChildTransitionResult>(body: (inout AVExperienceController.TransitionGroup<ChildTransitionResult>) async -> Void) async -> [ChildTransitionResult]](./withtransitiongroup%28body%29.md)
  Coordinates multiple experience transitions to perform together as a single visual transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transition(to:))*