# AVExperienceController.TransitionContext.Status

**Framework**: AVKit  
**Kind**: enum

Describes the status of a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum Status
```

#### Overview

Transitions go through a sequence of `Status`s as they progress.

## Topics

### Enumeration Cases
- [case finished(result: AVExperienceController.TransitionContext.TransitionResult)](avexperiencecontroller/transitioncontext/status-swift.enum/finished(result:).md)
  Transition finished. Perform cleanup based on result.
- [AVExperienceController.TransitionContext.Status.preparing](avexperiencecontroller/transitioncontext/status-swift.enum/preparing.md)
  The transition is preparing for `toExperience`.
- [AVExperienceController.TransitionContext.Status.transitioning](avexperiencecontroller/transitioncontext/status-swift.enum/transitioning.md)
  The transition is in progress.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/status-swift.enum)*