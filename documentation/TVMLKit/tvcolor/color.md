# color

**Framework**: TVMLKit  
**Kind**: property

A [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object used to color an element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var color: UIColor? { get }
```

#### Discussion

Only available when [`colorType`](tvcolor/colortype.md) is set to [`TVColorType.plain`](tvcolortype/plain.md).

## See Also

- [var colorType: TVColorType](tvcolor/colortype.md)
  The color type for an element.
- [enum TVColorType](tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientColors: [UIColor]?](tvcolor/gradientcolors.md)
  An array of colors used to create a gradient for an element.
- [var gradientPoints: [NSNumber]?](tvcolor/gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/color)*