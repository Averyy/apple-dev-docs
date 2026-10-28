# usesThreadedAnimation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the progress indicator implements animation in a separate thread.

**Availability**:
- macOS

## Declaration

```swift
var usesThreadedAnimation: Bool { get set }
```

```objc
@property BOOL usesThreadedAnimation;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), animation of the progress indicator occurs in a separate thread.

If the app becomes multithreaded as a result of an invocation of this method, the app’s performance could become noticeably slower.

## See Also

### Animating the progress indicator
- [func startAnimation(Any?)](./startanimation%28_%29.md)
  Starts the animation of an indeterminate progress indicator.
- [func stopAnimation(Any?)](./stopanimation%28_%29.md)
  Stops the animation of an indeterminate progress indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprogressindicator/usesthreadedanimation)*