# AVExperienceController.TransitionContext.Status

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Describes the status of a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
enum Status
```

## Overview

Transitions go through a sequence of `Status`s as they progress.

## Topics

### Statuses
- [AVExperienceController.TransitionContext.Status.preparing](./status-swift.enum/preparing.md)
  The transition is preparing for `toExperience`.
- [AVExperienceController.TransitionContext.Status.transitioning](./status-swift.enum/transitioning.md)
  The transition is in progress.
- [case finished(result: AVExperienceController.TransitionContext.TransitionResult)](./status-swift.enum/finished%28result%29.md)
  Transition finished. Perform cleanup based on result.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Understanding transition results
- [AVExperienceController.TransitionContext.TransitionResult](./transitionresult.md)
  Describes the result of a transition.
- [AVExperienceController.TransitionContext.ReversedReason](./reversedreason.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum)*