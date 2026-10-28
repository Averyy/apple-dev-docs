# AVExperienceController.Delegate

**Framework**: AVKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods to implement to respond to experience changes.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol Delegate : AnyObject
```

## Overview

Use this delegate to be aware of transitions and to update an app’s state based on those changes.

## Topics

### Responding to experience changes
- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](./delegate-swift.protocol/experiencecontroller%28_,didchangeavailableexperiences%29.md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, prepareForTransitionUsing: AVExperienceController.TransitionContext) async](./delegate-swift.protocol/experiencecontroller%28_,preparefortransitionusing%29.md)
  Tells the delegate that the system is preparing for a transition.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](./delegate-swift.protocol/experiencecontroller%28_,didchangetransitioncontext%29.md)
  Tells the delegate when the transition context changes during a transition.
- [AVExperienceController.TransitionContext](./transitioncontext.md)
  The state of the transition that the system provides to the delegate object.

## See Also

### Configuring a delegate
- [var delegate: (any AVExperienceController.Delegate)?](./delegate-swift.property.md)
  A delegate object for the experience controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol)*