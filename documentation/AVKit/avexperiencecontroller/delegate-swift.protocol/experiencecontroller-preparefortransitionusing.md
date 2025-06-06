# experienceController(_:prepareForTransitionUsing:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the system is preparing for a transition.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
func experienceController(_ controller: AVExperienceController, prepareForTransitionUsing context: AVExperienceController.TransitionContext) async
```

#### Discussion

Implement this method to prepare the app’s state for the [`toExperience`](avexperiencecontroller/transitioncontext/toexperience.md). This may include showing or hiding view controllers, putting the player view controller in the view hierarchy, or any other asynchronous work required for the transition. This is the last chance to update [`configuration`](avexperiencecontroller/configuration-swift.property.md) before the transition begins.

## Parameters

- `controller`: The  .
- `context`: Contains information about the transition.

## See Also

- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangeavailableexperiences:).md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:didchangetransitioncontext:).md)
  Tells the delegate when the transition context changes during a transition.
- [AVExperienceController.TransitionContext](avexperiencecontroller/transitioncontext.md)
  The state of the transition provided to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:))*