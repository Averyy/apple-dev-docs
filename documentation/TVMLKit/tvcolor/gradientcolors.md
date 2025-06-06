# gradientColors

**Framework**: TVMLKit  
**Kind**: property

An array of colors used to create a gradient for an element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var gradientColors: [UIColor]? { get }
```

#### Discussion

This property is only available when [`colorType`](tvcolor/colortype.md) is set to [`TVColorType.linearGradientTopToBottom`](tvcolortype/lineargradienttoptobottom.md) or [`TVColorType.linearGradientLeftToRight`](tvcolortype/lineargradientlefttoright.md).

## See Also

- [var color: UIColor?](tvcolor/color.md)
  A [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object used to color an element.
- [var colorType: TVColorType](tvcolor/colortype.md)
  The color type for an element.
- [enum TVColorType](tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientPoints: [NSNumber]?](tvcolor/gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/gradientcolors)*