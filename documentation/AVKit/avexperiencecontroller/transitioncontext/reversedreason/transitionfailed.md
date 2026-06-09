# AVExperienceController.TransitionContext.ReversedReason.transitionFailed

**Framework**: AVKit  
**Kind**: case

A transition has failed.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case transitionFailed
```

#### Discussion

This could fail due to changes in the system state after a transition is prepared.

## See Also

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration.md)
  A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](avexperiencecontroller/transitioncontext/reversedreason/invalidexperience.md)
  A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled.md)
  A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress.md)
  A transition was attempted while another transition was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitionfailed)*