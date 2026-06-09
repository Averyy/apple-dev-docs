# AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration

**Framework**: AVKit  
**Kind**: case

A transition could not be completed because some required configuration was unavailable.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case invalidConfiguration
```

#### Discussion

This can happen if AVPlayerViewController has been freed.

## See Also

- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](avexperiencecontroller/transitioncontext/reversedreason/invalidexperience.md)
  A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled.md)
  A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](avexperiencecontroller/transitioncontext/reversedreason/transitionfailed.md)
  A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress.md)
  A transition was attempted while another transition was in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration)*