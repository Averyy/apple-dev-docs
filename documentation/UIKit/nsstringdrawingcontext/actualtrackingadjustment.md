# actualTrackingAdjustment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The actual tracking value that the system applied during drawing.

**Availability**:
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var actualTrackingAdjustment: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat actualTrackingAdjustment;
```

## Discussion

If you specified a custom value in the [`minimumTrackingAdjustment`](./minimumtrackingadjustment.md) property, when drawing is complete, this property contains the actual tracking value that was used.

## See Also

### Accessing the scale factors
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.
- [var actualScaleFactor: CGFloat](./actualscalefactor.md)
  The actual scale factor that the system applied to the font during drawing.
- [var minimumTrackingAdjustment: CGFloat](./minimumtrackingadjustment.md)
  The smallest amount of space, in points, to maintain between characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualtrackingadjustment)*