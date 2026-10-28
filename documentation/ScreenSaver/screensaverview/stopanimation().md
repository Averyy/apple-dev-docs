# stopAnimation()

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Instance Method

Deactivates the timer that advances the animation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func stopAnimation()
```

```objc
- (void) stopAnimation;
```

## Discussion

The system calls this method when it’s time for you to stop animating your screen saver’s content. The system calls this method only once at the end of animations. Use this method to unload expensive resources or to reset your screen saver to a known state. If you override this method, you must call the inherited implementation at some point.

## See Also

### Animating the screen saver
- [func startAnimation()](./startanimation%28%29.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](./animateoneframe%28%29.md)
  Advances the screen saver’s animation by a single frame.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/stopanimation())*