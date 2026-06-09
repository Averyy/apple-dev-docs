# AVExperienceController.TransitionContext.ReversedReason.invalidExperience

**Framework**: AVKit  
**Kind**: case

A transition was attempted with an experience that cannot be transitioned to.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case invalidExperience
```

#### Discussion

Possible response is to consult `AVExperienceController.experience` and `AVExperienceController.availableExperiences` to choose a different experience to transition to.

## See Also

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration.md)
  A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled.md)
  A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](avexperiencecontroller/transitioncontext/reversedreason/transitionfailed.md)
  A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress.md)
  A transition was attempted while another transition was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidexperience)*