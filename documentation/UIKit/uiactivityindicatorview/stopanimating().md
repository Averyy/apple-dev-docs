# stopAnimating()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Stops the animation of the progress indicator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func stopAnimating()
```

```objc
- (void) stopAnimating;
```

## Discussion

Call this method to stop the animation of the progress indicator started with a call to [`startAnimating()`](./startanimating%28%29.md). When animating is stopped, the indicator is hidden, unless [`hidesWhenStopped`](./hideswhenstopped.md) is [`false`](../../Swift/false.md).

## See Also

### Managing an activity indicator
- [func startAnimating()](./startanimating%28%29.md)
  Starts the animation of the progress indicator.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.
- [var hidesWhenStopped: Bool](./hideswhenstopped.md)
  A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/stopanimating())*