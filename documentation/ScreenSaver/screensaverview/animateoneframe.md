# animateOneFrame()

**Framework**: Screen Saver  
**Kind**: method

Advances the screen saver’s animation by a single frame.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func animateOneFrame()
```

#### Discussion

The system calls this method each time the timer animating the screen saver fires. The time between calls to this method is always at least [`animationTimeInterval`](screensaverview/animationtimeinterval.md). The system locks focus on your view before it calls this method, so you can use this method to draw content. You can also let [`draw(_:)`](screensaverview/draw(_:).md) perform the drawing, in which case you use this method to call [`setNeedsDisplay(_:)`](https://developer.apple.com/documentation/AppKit/NSView/setNeedsDisplay(_:)) to mark your view as dirty. The default implementation of this method does nothing.

## See Also

- [func startAnimation()](screensaverview/startanimation.md)
  Activates the periodic timer that animates the screen saver.
- [func stopAnimation()](screensaverview/stopanimation.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](screensaverview/isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/animateoneframe())*