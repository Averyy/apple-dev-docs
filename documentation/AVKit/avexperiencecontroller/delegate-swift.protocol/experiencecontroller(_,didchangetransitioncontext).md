# experienceController(_:didChangeTransitionContext:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate when the transition context changes during a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func experienceController(_ controller: AVExperienceController, didChangeTransitionContext context: AVExperienceController.TransitionContext)
```

## Discussion

Implement this method to track the transition between experiences.

## Parameters

- `controller`: The experience controller.
- `context`: An structure that contains information about the transition.

## See Also

### Responding to experience changes
- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](./experiencecontroller%28_,didchangeavailableexperiences%29.md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](./experiencecontroller%28_,preparefortransitionusing%29.md)
  Tells the delegate that the system is preparing for a transition.
- [AVExperienceController.TransitionContext](../transitioncontext.md)
  The state of the transition that the system provides to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:))*