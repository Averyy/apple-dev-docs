# AVExperienceController.Delegate

**Framework**: AVKit  
**Kind**: protocol

A protocol that defines the methods to implement to respond to experience changes.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol Delegate : AnyObject
```

#### Overview

Use this delegate to be informed of transitions and to update applications state based on these changes.

## Topics

### Responding to experience changes
- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:).md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:).md)
  Tells the delegate that the system is preparing for a transition.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:).md)
  Tells the delegate when the transition context changes during a transition.
- [AVExperienceController.TransitionContext](avexperiencecontroller/transitioncontext.md)
  The state of the transition provided to the delegate object.

## See Also

- [var delegate: (any AVExperienceController.Delegate)?](avexperiencecontroller/delegate-swift.property.md)
  A delegate object for the experience controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol)*