# gradientPoints

**Framework**: TVMLKit  
**Kind**: property

An array of points used to determine gradient color changes.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var gradientPoints: [NSNumber]? { get }
```

#### Discussion

This property is only available when [`colorType`](tvcolor/colortype.md) is set to [`TVColorType.linearGradientTopToBottom`](tvcolortype/lineargradienttoptobottom.md) or [`TVColorType.linearGradientLeftToRight`](tvcolortype/lineargradientlefttoright.md). The points defined in the array determine when a color change occurs using the colors in the [`gradientColors`](tvcolor/gradientcolors.md) property.

## See Also

- [var color: UIColor?](tvcolor/color.md)
  A [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object used to color an element.
- [var colorType: TVColorType](tvcolor/colortype.md)
  The color type for an element.
- [enum TVColorType](tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientColors: [UIColor]?](tvcolor/gradientcolors.md)
  An array of colors used to create a gradient for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/gradientpoints)*