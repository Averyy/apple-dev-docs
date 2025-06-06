# isAnimating

**Framework**: Screen Saver  
**Kind**: property

A Boolean value that indicates whether the screen saver is animating.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var isAnimating: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the screen saver is animating, and [`false`](https://developer.apple.com/documentation/swift/false) when it isn’t.

## See Also

- [func startAnimation()](screensaverview/startanimation.md)
  Activates the periodic timer that animates the screen saver.
- [func animateOneFrame()](screensaverview/animateoneframe.md)
  Advances the screen saver’s animation by a single frame.
- [func stopAnimation()](screensaverview/stopanimation.md)
  Deactivates the timer that advances the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/isanimating)*