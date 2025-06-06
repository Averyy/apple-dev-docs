# moveIn(with:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates a transition where the new scene moves in on top of the old scene.

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
class func moveIn(with direction: SKTransitionDirection, duration sec: TimeInterval) -> SKTransition
```

#### Return Value

A new transition.

## Parameters

- `direction`: The direction of the move. Possible values are described in  .
- `sec`: The duration of the transition.

## See Also

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
- [class func push(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/push(with:duration:).md)
  Creates a transition where the new scene moves in, pushing the old scene out of the view.
- [class func reveal(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/reveal(with:duration:).md)
  Creates a transition where the old scene moves out of the view, revealing the new scene underneath it.
- [init(ciFilter: CIFilter, duration: TimeInterval)](sktransition/init(cifilter:duration:).md)
  Creates a transition that uses a Core Image filter to perform the transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktransition/movein(with:duration:))*