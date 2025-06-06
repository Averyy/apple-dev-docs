# Transitioning Between Two Scenes

**Framework**: SpriteKit

#### Overview

Typically, you transition to a new scene based on gameplay or user input. For example, if the user presses a button in your main menu scene, you might transition to a new scene to configure the match the player wants to play.

Listing 1 shows how you might implement the event handler in a sprite. The handler first runs an animation on itself to highlight the button (not described here). Then, it creates a transition object and the new scene. Finally, it calls the view to present the new scene. The transition means that this change is animated.

Listing 1. Transitioning to a new scene

When the transition occurs, the scene property is immediately updated to point to the new scene. Then, the animation occurs. Finally, the strong reference to the old scene is removed. If you need to keep the scene around after the transition occurs, your app needs to keep its own strong reference to the old scene.

When organizing your game, it can be helpful to create a diagram that shows all the scenes in a game, the transitions that occur between scenes, and the data that must be passed to the new scene when a transition occurs. Unlike view controllers in iOS, SpriteKit does not provide a built-in mechanism for passing data between scenes. If you need to provide data during a scene transition, you need to implement your own mechanism to configure the new scene. Typically, this means defining custom methods and properties on each scene.

## See Also

- [Configuring Whether Animations Play During the Transition](configuring-whether-animations-play-during-the-transition.md)
- [class func crossFade(withDuration: TimeInterval) -> SKTransition](sktransition/crossfade(withduration:).md)
  Creates a cross fade transition.
- [class func doorsCloseHorizontal(withDuration: TimeInterval) -> SKTransition](sktransition/doorsclosehorizontal(withduration:).md)
  Creates a transition where the new scene appears as a pair of closing horizontal doors.
- [class func doorsCloseVertical(withDuration: TimeInterval) -> SKTransition](sktransition/doorsclosevertical(withduration:).md)
  Creates a transition where the new scene appears as a pair of closing vertical doors.
- [class func doorsOpenHorizontal(withDuration: TimeInterval) -> SKTransition](sktransition/doorsopenhorizontal(withduration:).md)
  Creates a transition where the new scene appears as a pair of opening horizontal doors.
- [class func doorsOpenVertical(withDuration: TimeInterval) -> SKTransition](sktransition/doorsopenvertical(withduration:).md)
  Creates a transition where the new scene appears as a pair of opening vertical doors.
- [class func doorway(withDuration: TimeInterval) -> SKTransition](sktransition/doorway(withduration:).md)
  Creates a transition where the previous scene disappears as a pair of opening doors.
- [class func fade(with: UIColor, duration: TimeInterval) -> SKTransition](sktransition/fade(with:duration:).md)
  Creates a transition that first fades to a constant color and then fades to the new scene.
- [class func fade(withDuration: TimeInterval) -> SKTransition](sktransition/fade(withduration:).md)
  Creates a transition that first fades to black and then fades to the new scene.
- [class func flipHorizontal(withDuration: TimeInterval) -> SKTransition](sktransition/fliphorizontal(withduration:).md)
  Creates a transition where the two scenes are flipped across a horizontal line running through the center of the view.
- [class func flipVertical(withDuration: TimeInterval) -> SKTransition](sktransition/flipvertical(withduration:).md)
  Creates a transition where the two scenes are flipped across a vertical line running through the center of the view.
- [class func moveIn(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/movein(with:duration:).md)
  Creates a transition where the new scene moves in on top of the old scene.
- [class func push(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/push(with:duration:).md)
  Creates a transition where the new scene moves in, pushing the old scene out of the view.
- [class func reveal(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/reveal(with:duration:).md)
  Creates a transition where the old scene moves out of the view, revealing the new scene underneath it.
- [init(ciFilter: CIFilter, duration: TimeInterval)](sktransition/init(cifilter:duration:).md)
  Creates a transition that uses a Core Image filter to perform the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/transitioning-between-two-scenes)*