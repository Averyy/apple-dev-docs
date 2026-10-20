# experienceController(_:prepareForTransitionUsing:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method  
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

Implement this method to prepare the app’s state for the [`toExperience`](../transitioncontext/toexperience.md). This may include showing or hiding view controllers, putting the player view controller in the view hierarchy, or any other asynchronous work required for the transition. This is the last chance to update [`configuration`](../configuration-swift.property.md) before the transition begins.

## Parameters

- `controller`: The `AVExperienceController`.
- `context`: Contains information about the transition.

## See Also

### Responding to experience changes
- [func experienceController(AVExperienceController, didChangeAvailableExperiences: AVExperienceController.Experiences)](./experiencecontroller%28_,didchangeavailableexperiences%29.md)
  Tells the delegate when the available experiences change.
- [func experienceController(AVExperienceController, didChangeTransitionContext: AVExperienceController.TransitionContext)](./experiencecontroller%28_,didchangetransitioncontext%29.md)
  Tells the delegate when the transition context changes during a transition.
- [AVExperienceController.TransitionContext](../transitioncontext.md)
  The state of the transition that the system provides to the delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.protocol/experiencecontroller(_:preparefortransitionusing:))*