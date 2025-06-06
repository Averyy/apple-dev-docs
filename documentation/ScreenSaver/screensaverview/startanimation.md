# startAnimation()

**Framework**: Screen Saver  
**Kind**: method

Activates the periodic timer that animates the screen saver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func startAnimation()
```

#### Discussion

The system calls this method when it’s time for you to start animating your screen saver’s content. The system calls this method only once at the start of animations. Use this method to set up any initial state information you require or to allocate expensive resources. If you override this method, you must call the inherited implementation at some point.

## See Also

- [func animateOneFrame()](screensaverview/animateoneframe.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](screensaverview/stopanimation.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](screensaverview/isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/startanimation())*