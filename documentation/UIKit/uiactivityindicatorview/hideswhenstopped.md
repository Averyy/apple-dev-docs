# hidesWhenStopped

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var hidesWhenStopped: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) (the default), the receiver sets its [`isHidden`](uiview/ishidden.md) property (`UIView`) to [`true`](https://developer.apple.com/documentation/Swift/true) when receiver is not animating. If the [`hidesWhenStopped`](uiactivityindicatorview/hideswhenstopped.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), the receiver is not hidden when animation stops. You stop an animating progress indicator with the [`stopAnimating()`](uiactivityindicatorview/stopanimating().md) method.

## See Also

- [func startAnimating()](uiactivityindicatorview/startanimating.md)
  Starts the animation of the progress indicator.
- [func stopAnimating()](uiactivityindicatorview/stopanimating.md)
  Stops the animation of the progress indicator.
- [var isAnimating: Bool](uiactivityindicatorview/isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/hideswhenstopped)*