# transition(to:)

**Framework**: AVKit  
**Kind**: method

Transitions the video to a different experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor final func transition(to toExperience: AVExperienceController.Experience) async -> AVExperienceController.TransitionContext.TransitionResult
```

#### Return Value

A transition result.

#### Discussion

Call this method to transition to a different experience such as [`AVExperienceController.Experience.expanded`](avexperiencecontroller/experience-swift.enum/expanded.md). When you initiate a transition, the system calls the experience controller’s delegate methods so your app can respond to experience changes.

You determine the success of a transition by evaluating the [`AVExperienceController.TransitionContext.TransitionResult`](avexperiencecontroller/transitioncontext/transitionresult.md) this method returns. A transition result of [`AVExperienceController.TransitionContext.TransitionResult.completed`](avexperiencecontroller/transitioncontext/transitionresult/completed.md) indicates a successful transition, in which case the system updates the [`experience`](avexperiencecontroller/experience-swift.property.md) property to the new experience. A transition result of [`AVExperienceController.TransitionContext.TransitionResult.reversed(reason:)`](avexperiencecontroller/transitioncontext/transitionresult/reversed(reason:).md) indicates a failed transition. Evaluate the the result’s [`AVExperienceController.TransitionContext.ReversedReason`](avexperiencecontroller/transitioncontext/reversedreason.md) to determine why the transition failed. A failure that occurs before the transition begins results in the system not invoking any delegate callback methods. If the failure happens after the callback to  [`experienceController(_:prepareForTransitionUsing:)`](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md) occurs, the transition context changes to [`AVExperienceController.TransitionContext.Status.finished(result:)`](avexperiencecontroller/transitioncontext/status-swift.enum/finished(result:).md).

## Parameters

- `toExperience`: The experience to transition to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transition(to:))*