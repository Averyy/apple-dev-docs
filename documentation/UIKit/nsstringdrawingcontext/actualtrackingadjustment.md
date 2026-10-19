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

- [var minimumScaleFactor: CGFloat](nsstringdrawingcontext/minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.
- [var actualScaleFactor: CGFloat](nsstringdrawingcontext/actualscalefactor.md)
  The actual scale factor that the system applied to the font during drawing.
- [var minimumTrackingAdjustment: CGFloat](nsstringdrawingcontext/minimumtrackingadjustment.md)
  The smallest amount of space, in points, to maintain between characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment)*