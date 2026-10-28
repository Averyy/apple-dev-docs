# AVExperienceController.TransitionContext.TransitionResult

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Describes the result of a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@preconcurrency
enum TransitionResult
```

## Overview

A transition can successfully complete to the `toExperience` or reverse back to the `fromExperience`.

## Topics

### Results
- [AVExperienceController.TransitionContext.TransitionResult.completed](./transitionresult/completed.md)
- [case reversed(reason: AVExperienceController.TransitionContext.ReversedReason)](./transitionresult/reversed%28reason%29.md)

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Understanding transition results
- [AVExperienceController.TransitionContext.Status](./status-swift.enum.md)
  Describes the status of a transition.
- [AVExperienceController.TransitionContext.ReversedReason](./reversedreason.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/transitionresult)*