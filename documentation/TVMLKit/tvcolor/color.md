# color

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

A [`UIColor`](../../UIKit/uicolor.md) object used to color an element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var color: UIColor? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIColor * color;
```

## Discussion

Only available when [`colorType`](./colortype.md) is set to [`TVColorType.plain`](../tvcolortype/plain.md).

## See Also

### Getting Color Properties
- [var colorType: TVColorType](./colortype.md)
  The color type for an element.
- [enum TVColorType](../tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientColors: [UIColor]?](./gradientcolors.md)
  An array of colors used to create a gradient for an element.
- [var gradientPoints: [NSNumber]?](./gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/color)*