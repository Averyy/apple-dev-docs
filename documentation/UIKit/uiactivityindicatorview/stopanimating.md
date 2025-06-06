# stopAnimating()

**Framework**: UIKit  
**Kind**: method

Stops the animation of the progress indicator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func stopAnimating()
```

#### Discussion

Call this method to stop the animation of the progress indicator started with a call to [`startAnimating()`](uiactivityindicatorview/startanimating().md). When animating is stopped, the indicator is hidden, unless [`hidesWhenStopped`](uiactivityindicatorview/hideswhenstopped.md) is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func startAnimating()](uiactivityindicatorview/startanimating.md)
  Starts the animation of the progress indicator.
- [var isAnimating: Bool](uiactivityindicatorview/isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.
- [var hidesWhenStopped: Bool](uiactivityindicatorview/hideswhenstopped.md)
  A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/stopanimating())*