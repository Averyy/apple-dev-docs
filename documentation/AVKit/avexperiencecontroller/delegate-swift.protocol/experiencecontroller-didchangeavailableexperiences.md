# experienceController(_:didChangeAvailableExperiences:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Tells the delegate when the available experiences change.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func experienceController(_ controller: AVExperienceController, didChangeAvailableExperiences availableExperiences: AVExperienceController.Experiences)
```

#### Discussion

Use this callback to hide or show interface elements based on which experiences are possible.

## Parameters

- `controller`: The experience controller.
- `availableExperiences`: The current value of  .

## See Also

- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md)
  Tells the delegate that the system is preparing for a transition.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:).md)
  Tells the delegate when the transition context changes during a transition.
- [AVExperienceController.TransitionContext](avexperiencecontroller/transitioncontext.md)
  The state of the transition provided to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:))*