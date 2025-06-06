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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/transitioncontext/reversedreason/invalidexperience)*