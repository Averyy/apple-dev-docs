# startAnimation()

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Instance Method

Activates the periodic timer that animates the screen saver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func startAnimation()
```

```objc
- (void) startAnimation;
```

#### Discussion

The system calls this method when it’s time for you to start animating your screen saver’s content. The system calls this method only once at the start of animations. Use this method to set up any initial state information you require or to allocate expensive resources. If you override this method, you must call the inherited implementation at some point.

## See Also

### Animating the screen saver
- [func animateOneFrame()](./animateoneframe%28%29.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](./stopanimation%28%29.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/startanimation())*