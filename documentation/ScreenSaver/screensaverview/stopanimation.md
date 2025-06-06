# stopAnimation()

**Framework**: Screen Saver  
**Kind**: method

Deactivates the timer that advances the animation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func stopAnimation()
```

#### Discussion

The system calls this method when it’s time for you to stop animating your screen saver’s content. The system calls this method only once at the end of animations. Use this method to unload expensive resources or to reset your screen saver to a known state. If you override this method, you must call the inherited implementation at some point.

## See Also

- [func startAnimation()](screensaverview/startanimation.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](screensaverview/animateoneframe.md)
  Advances the screen saver’s animation by a single frame.
- [var isAnimating: Bool](screensaverview/isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/stopanimation())*