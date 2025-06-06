# effect

**Framework**: AppKit  
**Kind**: property

An effect to apply to the animation.

**Availability**:
- macOS ?+

## Declaration

```swift
static let effect: NSViewAnimation.Key
```

#### Discussion

Takes a string constant specifying fade-in or fade-out effects for the target: `NSViewAnimationFadeInEffect` and `NSViewAnimationFadeOutEffect`. If the target is a view and the effect is to fade out, the view is hidden at the end. If the effect is to fade in an initially hidden view and the end frame is non-empty, the view is unhidden at the end. If the target is a window, the window is ordered in or out as appropriate to the effect. This property is optional.

## See Also

- [static let endFrame: NSViewAnimation.Key](nsviewanimation/key/endframe.md)
  The size and location of the window or view at the end of the animation.
- [static let startFrame: NSViewAnimation.Key](nsviewanimation/key/startframe.md)
  The size and location of the window or view at the start of the animation.
- [static let target: NSViewAnimation.Key](nsviewanimation/key/target.md)
  The target of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewanimation/key/effect)*