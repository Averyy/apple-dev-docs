# AVExperienceController.TransitionContext

**Framework**: AVKit  
**Kind**: struct

The state of the transition provided to the delegate object.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TransitionContext
```

#### Overview

When `AVExperienceController` transitions its `experience` from `fromExperience` to `toExperience`, delegate callbacks provide instances of `TransitionContext` to allow clients to respond as the transition progresses or reverts. The normal `Status` sequence is `.preparing` -> `.transitioning` -> `.completed` Once `.completed`, `AVExperienceController`’s `experience` is now the `toExperience`.

Not all transitions are `.completed`, instead they are `.reversed` back to the `fromExperience`. Reversed transitions can happen after `.preparing` or after `.transitioning`, but it will not happen after `.completed` or before `.preparing`. When a transition is reversed a reason is provided.

## Topics

### Instance Properties
- [let fromExperience: AVExperienceController.Experience](avexperiencecontroller/transitioncontext/fromexperience.md)
  The experience of the `AVExperienceController` before the transition was initiated.
- [let status: AVExperienceController.TransitionContext.Status](avexperiencecontroller/transitioncontext/status-swift.property.md)
  The status of the transition.
- [let toExperience: AVExperienceController.Experience](avexperiencecontroller/transitioncontext/toexperience.md)
  The experience to which the `AVExperienceController` has been requested to transition to.
### Enumerations
- [AVExperienceController.TransitionContext.ReversedReason](avexperiencecontroller/transitioncontext/reversedreason.md)
- [AVExperienceController.TransitionContext.Status](avexperiencecontroller/transitioncontext/status-swift.enum.md)
  Describes the status of a transition.
- [AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transitioncontext/transitionresult.md)
  Describes the result of a transition.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:).md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md)
  Tells the delegate that the system is preparing for a transition.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:).md)
  Tells the delegate when the transition context changes during a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext)*