# experienceController(_:didChangeTransitionContext:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Tells the delegate when the transition context changes during a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func experienceController(_ controller: AVExperienceController, didChangeTransitionContext context: AVExperienceController.TransitionContext)
```

#### Discussion

Implement this method to track the transition between experiences.

## Parameters

- `controller`: The experience controller.
- `context`: An structure that contains information about the transition.

## See Also

- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:).md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md)
  Tells the delegate that the system is preparing for a transition.
- [AVExperienceController.TransitionContext](avexperiencecontroller/transitioncontext.md)
  The state of the transition provided to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:))*