# AVExperienceController.TransitionContext.Status

**Framework**: AVKit  
**Kind**: enum

Describes the status of a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
enum Status
```

#### Overview

Transitions go through a sequence of `Status`s as they progress.

## Topics

### Statuses
- [AVExperienceController.TransitionContext.Status.preparing](avexperiencecontroller/transitioncontext/status-swift.enum/preparing.md)
  The transition is preparing for `toExperience`.
- [AVExperienceController.TransitionContext.Status.transitioning](avexperiencecontroller/transitioncontext/status-swift.enum/transitioning.md)
  The transition is in progress.
- [case finished(result: AVExperienceController.TransitionContext.TransitionResult)](avexperiencecontroller/transitioncontext/status-swift.enum/finished(result:).md)
  Transition finished. Perform cleanup based on result.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [AVExperienceController.TransitionContext.TransitionResult](avexperiencecontroller/transitioncontext/transitionresult.md)
  Describes the result of a transition.
- [AVExperienceController.TransitionContext.ReversedReason](avexperiencecontroller/transitioncontext/reversedreason.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum)*