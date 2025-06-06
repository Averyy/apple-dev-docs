# TVColorType

**Framework**: TVMLKit  
**Kind**: enum

Designates how color for an element is to be displayed.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum TVColorType
```

## Topics

### Constants
- [TVColorType.none](tvcolortype/none.md)
  Indicates that there is no color associated with an element.
- [TVColorType.plain](tvcolortype/plain.md)
  Indicates that a single color is to be used with an element.
- [TVColorType.linearGradientTopToBottom](tvcolortype/lineargradienttoptobottom.md)
  Indicates that a color gradient goes from the top to the bottom of an element.
- [TVColorType.linearGradientLeftToRight](tvcolortype/lineargradientlefttoright.md)
  Indicates that a color gradient goes from the left to the right of an element.
### Initializers
- [init?(rawValue: Int)](tvcolortype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var color: UIColor?](tvcolor/color.md)
  A [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) object used to color an element.
- [var colorType: TVColorType](tvcolor/colortype.md)
  The color type for an element.
- [var gradientColors: [UIColor]?](tvcolor/gradientcolors.md)
  An array of colors used to create a gradient for an element.
- [var gradientPoints: [NSNumber]?](tvcolor/gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolortype)*