# AVExperienceController.TransitionContext.ReversedReason.transitionCancelled

**Framework**: AVKit  
**Kind**: case

A transition in progress has been cancelled.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case transitionCancelled
```

#### Discussion

This can happen due to user interaction or some other system event.

## See Also

- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration.md)
  A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](avexperiencecontroller/transitioncontext/reversedreason/invalidexperience.md)
  A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](avexperiencecontroller/transitioncontext/reversedreason/transitionfailed.md)
  A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress.md)
  A transition was attempted while another transition was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled)*