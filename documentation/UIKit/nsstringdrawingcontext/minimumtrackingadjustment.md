# minimumTrackingAdjustment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The smallest amount of space, in points, to maintain between characters.

**Availability**:
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var minimumTrackingAdjustment: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumTrackingAdjustment;
```

## Discussion

Changing the value of this property tells the renderer that it can change the tracking to a value no smaller than the indicated amount. For example, a value of `-0.5` indicates that characters can be tracked closer together by up to half a point. A value of 0 indicates that the standard spacing is used. A typical range of values for this property would be `-0.5` to `0.0`. The default value of this property is `0.0`.

## See Also

### Accessing the scale factors
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.
- [var actualScaleFactor: CGFloat](./actualscalefactor.md)
  The actual scale factor that the system applied to the font during drawing.
- [var actualTrackingAdjustment: CGFloat](./actualtrackingadjustment.md)
  The actual tracking value that the system applied during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/minimumtrackingadjustment)*