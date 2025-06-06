# actualTrackingAdjustment

**Framework**: UIKit  
**Kind**: property

The actual tracking value that the system applied during drawing.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var actualTrackingAdjustment: CGFloat { get }
```

#### Discussion

If you specified a custom value in the [`minimumTrackingAdjustment`](nsstringdrawingcontext/minimumtrackingadjustment.md) property, when drawing is complete, this property contains the actual tracking value that was used.

## See Also

- [var minimumTrackingAdjustment: CGFloat](nsstringdrawingcontext/minimumtrackingadjustment.md)
  The smallest amount of space, in points, to maintain between characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment)*