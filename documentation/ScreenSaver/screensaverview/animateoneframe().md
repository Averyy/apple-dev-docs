# animateOneFrame()

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Instance Method

Advances the screen saver’s animation by a single frame.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func animateOneFrame()
```

```objc
- (void) animateOneFrame;
```

## Discussion

The system calls this method each time the timer animating the screen saver fires. The time between calls to this method is always at least [`animationTimeInterval`](./animationtimeinterval.md). The system locks focus on your view before it calls this method, so you can use this method to draw content. You can also let [`draw(_:)`](./draw%28_%29.md) perform the drawing, in which case you use this method to call [`setNeedsDisplay(_:)`](../../AppKit/nsview/setneedsdisplay%28_%29.md) to mark your view as dirty. The default implementation of this method does nothing.

## See Also

### Animating the screen saver
- [func startAnimation()](./startanimation%28%29.md)
  Activates the periodic timer that animates the screen saver.
- [func stopAnimation()](./stopanimation%28%29.md)
  Deactivates the timer that advances the animation.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value that indicates whether the screen saver is animating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/animateoneframe())*