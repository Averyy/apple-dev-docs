# AVExperienceController.TransitionContext.ReversedReason

**Framework**: AVKit  
**Kind**: enum

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
enum ReversedReason
```

## Topics

### Reasons
- [AVExperienceController.TransitionContext.ReversedReason.invalidConfiguration](avexperiencecontroller/transitioncontext/reversedreason/invalidconfiguration.md)
  A transition could not be completed because some required configuration was unavailable.
- [AVExperienceController.TransitionContext.ReversedReason.invalidExperience](avexperiencecontroller/transitioncontext/reversedreason/invalidexperience.md)
  A transition was attempted with an experience that cannot be transitioned to.
- [AVExperienceController.TransitionContext.ReversedReason.transitionCancelled](avexperiencecontroller/transitioncontext/reversedreason/transitioncancelled.md)
  A transition in progress has been cancelled.
- [AVExperienceController.TransitionContext.ReversedReason.transitionFailed](avexperiencecontroller/transitioncontext/reversedreason/transitionfailed.md)
  A transition has failed.
- [AVExperienceController.TransitionContext.ReversedReason.transitionInProgress](avexperiencecontroller/transitioncontext/reversedreason/transitioninprogress.md)
  A transition was attempted while another transition was in progress.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AVExperienceController.TransitionContext.Status](avexperiencecontroller/transitioncontext/status-swift.enum.md)
  Describes the status of a transition.
- [AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transitioncontext/transitionresult.md)
  Describes the result of a transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason)*