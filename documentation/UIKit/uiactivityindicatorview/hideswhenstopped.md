# hidesWhenStopped

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that controls whether the activity indicator is hidden when the animation is stopped.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var hidesWhenStopped: Bool { get set }
```

```objc
@property (nonatomic) BOOL hidesWhenStopped;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md) (the default), the receiver sets its [`isHidden`](../uiview/ishidden.md) property (`UIView`) to [`true`](../../Swift/true.md) when receiver is not animating. If the [`hidesWhenStopped`](./hideswhenstopped.md) property is [`false`](../../Swift/false.md), the receiver is not hidden when animation stops. You stop an animating progress indicator with the [`stopAnimating()`](./stopanimating%28%29.md) method.

## See Also

### Managing an activity indicator
- [func startAnimating()](./startanimating%28%29.md)
  Starts the animation of the progress indicator.
- [func stopAnimating()](./stopanimating%28%29.md)
  Stops the animation of the progress indicator.
- [var isAnimating: Bool](./isanimating.md)
  A Boolean value indicating whether the activity indicator is currently running its animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/hideswhenstopped)*