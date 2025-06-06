# minimumTrackingAdjustment

**Framework**: UIKit  
**Kind**: property

The smallest amount of space, in points, to maintain between characters.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var minimumTrackingAdjustment: CGFloat { get set }
```

#### Discussion

Changing the value of this property tells the renderer that it can change the tracking to a value no smaller than the indicated amount. For example, a value of `-0.5` indicates that characters can be tracked closer together by up to half a point. A value of 0 indicates that the standard spacing is used. A typical range of values for this property would be `-0.5` to `0.0`. The default value of this property is `0.0`.

## See Also

- [var actualTrackingAdjustment: CGFloat](nsstringdrawingcontext/actualtrackingadjustment.md)
  The actual tracking value that the system applied during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/minimumtrackingadjustment)*