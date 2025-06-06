# timingFunction

**Framework**: AppKit  
**Kind**: property

The timing function used for all animations within this animation proxy group.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var timingFunction: CAMediaTimingFunction? { get set }
```

#### Discussion

The NSAnimationContext timing function is analogous to the CATransaction [`setAnimationTimingFunction(_:)`](https://developer.apple.com/documentation/QuartzCore/CATransaction/setAnimationTimingFunction(_:)) method.

Animations initiated through the “animator” proxy syntax, that do not have an explicitly specified timing functions, will inherit the enclosing `NSAnimationContext` instance’s [`timingFunction`](nsanimationcontext/timingfunction.md) if it is not `nil` (which is the default).

As with the existing [`duration`](nsanimationcontext/duration.md) property, changing a timing function causes the same change in the underlying CATransaction instance’s [`animationTimingFunction()`](https://developer.apple.com/documentation/QuartzCore/CATransaction/animationTimingFunction()).

Also as with the [`duration`](nsanimationcontext/duration.md) property, you may change the timingFunction any number of times within a given NSAnimationContext [`beginGrouping()`](nsanimationcontext/begingrouping().md) and [`endGrouping()`](nsanimationcontext/endgrouping().md) block. Changes to the `timingFunction` will apply to any animations that are subsequently initiated in that NSAnimationContext grouping, until the `timingFunction` is possibly changed again.

## See Also

- [var duration: TimeInterval](nsanimationcontext/duration.md)
  The duration used by animations created as a result of setting new values for an animatable property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext/timingfunction)*