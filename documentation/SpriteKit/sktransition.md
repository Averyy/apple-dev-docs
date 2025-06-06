# SKTransition

**Framework**: SpriteKit  
**Kind**: class

An object used to perform an animated transition to a new scene.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class SKTransition
```

#### Overview

Scenes are the basic building blocks of games. Typically, you design self-contained scenes for the parts of your game, and then transition between these scenes as necessary. For example, you might create different scene classes to represent any or all of the following concepts:

- A loading scene to display while other content is loaded
- A main menu scene to choose what kind of game the user wants to play
- A scene to configure the details of the specific kind of game the user chose
- A scene that provides the gameplay
- A scene displayed when gameplay ends

When you present a new scene in a view that is already presenting a scene, you have the option of using a transition to animate the change from the old scene to the new scene. Using a transition provides continuity so that the scene change is not quite so abrupt.

## Topics

### Creating Transitions
- [Transitioning Between Two Scenes](transitioning-between-two-scenes.md)
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
### Pausing
- [var pausesIncomingScene: Bool](sktransition/pausesincomingscene.md)
  A Boolean value that determines whether the incoming scene is paused during the transition.
- [var pausesOutgoingScene: Bool](sktransition/pausesoutgoingscene.md)
  A Boolean value that determines whether the outgoing scene is paused during the transition.
### Constants
- [enum SKTransitionDirection](sktransitiondirection.md)
  For some transitions, the direction in which the transition is performed.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var scene: SKScene?](skview/scene.md)
  The scene currently presented by this view.
- [func presentScene(SKScene?)](skview/presentscene(_:).md)
  Presents a scene.
- [func presentScene(SKScene, transition: SKTransition)](skview/presentscene(_:transition:).md)
  Transitions from the current scene to a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktransition)*