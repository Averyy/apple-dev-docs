# AVExperienceController.TransitionContext

**Framework**: AVKit  
**Kind**: struct  
**Role**: Structure

The state of the transition that the system provides to the delegate object.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
struct TransitionContext
```

## Overview

When `AVExperienceController` transitions its `experience` from `fromExperience` to `toExperience`, delegate callbacks provide instances of `TransitionContext` to allow clients to respond as the transition progresses or reverts. The normal `Status` sequence is `.preparing` -> `.transitioning` -> `.completed` Once `.completed`, `AVExperienceController`’s `experience` is now the `toExperience`.

Not all transitions are `.completed`, instead they are `.reversed` back to the `fromExperience`. Reversed transitions can happen after `.preparing` or after `.transitioning`, but it will not happen after `.completed` or before `.preparing`. When a transition is reversed a reason is provided.

## Topics

### Inspecting the transition
- [let fromExperience: AVExperienceController.Experience](./transitioncontext/fromexperience.md)
  The experience of the `AVExperienceController` before the transition was initiated.
- [let toExperience: AVExperienceController.Experience](./transitioncontext/toexperience.md)
  The experience to which the `AVExperienceController` has been requested to transition to.
- [let status: AVExperienceController.TransitionContext.Status](./transitioncontext/status-swift.property.md)
  The status of the transition.
### Understanding transition results
- [AVExperienceController.TransitionContext.Status](./transitioncontext/status-swift.enum.md)
  Describes the status of a transition.
- [AVExperienceController.TransitionContext.TransitionResult](./transitioncontext/transitionresult.md)
  Describes the result of a transition.
- [AVExperienceController.TransitionContext.ReversedReason](./transitioncontext/reversedreason.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to experience changes
- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](./delegate-swift.protocol/experiencecontroller%28_,didchangeavailableexperiences%29.md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](./delegate-swift.protocol/experiencecontroller%28_,preparefortransitionusing%29.md)
  Tells the delegate that the system is preparing for a transition.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](./delegate-swift.protocol/experiencecontroller%28_,didchangetransitioncontext%29.md)
  Tells the delegate when the transition context changes during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext)*