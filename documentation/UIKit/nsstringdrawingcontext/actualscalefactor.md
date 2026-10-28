# actualScaleFactor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The actual scale factor that the system applied to the font during drawing.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actualScaleFactor: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat actualScaleFactor;
```

## Discussion

If you specified a custom value in the [`minimumScaleFactor`](./minimumscalefactor.md) property, when drawing is complete, this property contains the actual scale factor value that was used to draw the string.

## See Also

### Accessing the scale factors
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.
- [var minimumTrackingAdjustment: CGFloat](./minimumtrackingadjustment.md)
  The smallest amount of space, in points, to maintain between characters.
- [var actualTrackingAdjustment: CGFloat](./actualtrackingadjustment.md)
  The actual tracking value that the system applied during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualscalefactor)*