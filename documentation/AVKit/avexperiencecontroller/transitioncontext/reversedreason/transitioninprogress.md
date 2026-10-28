# AVExperienceController.TransitionContext.ReversedReason.transitionInProgress

**Framework**: AVKit  
**Kind**: case  
**Role**: Case

A transition was attempted while another transition was in progress.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case transitionInProgress
```

## Discussion

Possible response is to try again after the transition completes.

## See Also

### Reasons
- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](./invalidconfiguration.md)
  A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](./invalidexperience.md)
  A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](./transitioncancelled.md)
  A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](./transitionfailed.md)
  A transition has failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress)*