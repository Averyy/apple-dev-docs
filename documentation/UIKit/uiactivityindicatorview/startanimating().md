# startAnimating()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Starts the animation of the progress indicator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func startAnimating()
```

```objc
- (void) startAnimating;
```

#### Discussion

When the progress indicator is animated, the gear spins to indicate indeterminate progress. The indicator is animated until [`stopAnimating()`](./stopanimating%28%29.md) is called.

## See Also

### Managing an activity indicator
- [func stopAnimating()](./stopanimating%28%29.md)
  Stops the animation of the progress indicator.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.
- [var hidesWhenStopped: Bool](./hideswhenstopped.md)
  A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/startanimating())*