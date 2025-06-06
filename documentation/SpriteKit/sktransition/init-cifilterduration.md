# init(ciFilter:duration:)

**Framework**: SpriteKit  
**Kind**: init

Creates a transition that uses a Core Image filter to perform the transition.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(ciFilter filter: CIFilter, duration sec: TimeInterval)
```

#### Return Value

A new transition.

#### Discussion

The filter used to perform the transition must a be filter that requires only two image parameters (`inputImage`, `inputTargetImage`) and generates a single image (`outputImage`). The transition automatically sets the filter’s `inputImage`, `inputTargetImage`, and `inputTime` properties. You must set up any other filter properties before creating the transition.

## Parameters

- `filter`: A Core Image filter.
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
- [class func moveIn(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/movein(with:duration:).md)
  Creates a transition where the new scene moves in on top of the old scene.
- [class func push(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/push(with:duration:).md)
  Creates a transition where the new scene moves in, pushing the old scene out of the view.
- [class func reveal(with: SKTransitionDirection, duration: TimeInterval) -> SKTransition](sktransition/reveal(with:duration:).md)
  Creates a transition where the old scene moves out of the view, revealing the new scene underneath it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktransition/init(cifilter:duration:))*