# minimumScaleFactor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The scale factor that determines the smallest font size to use during drawing.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var minimumScaleFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumScaleFactor;
```

## Discussion

A value of `0.0` corresponds to a scale factor of `1.0`. Any value greater than `0.0` is multiplied by the font point size to get the smallest font size that is permissible to use. For example, 0.5 indicates a font that is half the size of the actual font, 0.75 is three-quarters of the font size, and so on. Typically, you specify a value between 0.0 and 1.0 to indicate how much the font can be shrunk during drawing.

The default value of this property is `0.0`.

## See Also

### Accessing the scale factors
- [var actualScaleFactor: CGFloat](./actualscalefactor.md)
  The actual scale factor that the system applied to the font during drawing.
- [var minimumTrackingAdjustment: CGFloat](./minimumtrackingadjustment.md)
  The smallest amount of space, in points, to maintain between characters.
- [var actualTrackingAdjustment: CGFloat](./actualtrackingadjustment.md)
  The actual tracking value that the system applied during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/minimumscalefactor)*