# isAnimating

**Framework**: Screen Saver  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the screen saver is animating.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isAnimating: Bool { get }
```

```objc
@property (atomic, readonly, getter=isAnimating) BOOL animating;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the screen saver is animating, and [`false`](../../Swift/false.md) when it isn’t.

## See Also

### Animating the screen saver
- [func startAnimation()](./startanimation%28%29.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](./animateoneframe%28%29.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](./stopanimation%28%29.md)
  Deactivates the timer that advances the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/isanimating)*