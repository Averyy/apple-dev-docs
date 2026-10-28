# gradientPoints

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

An array of points used to determine gradient color changes.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var gradientPoints: [NSNumber]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSNumber *> * gradientPoints;
```

## Discussion

This property is only available when [`colorType`](./colortype.md) is set to [`TVColorType.linearGradientTopToBottom`](../tvcolortype/lineargradienttoptobottom.md) or [`TVColorType.linearGradientLeftToRight`](../tvcolortype/lineargradientlefttoright.md). The points defined in the array determine when a color change occurs using the colors in the [`gradientColors`](./gradientcolors.md) property.

## See Also

### Getting Color Properties
- [var color: UIColor?](./color.md)
  A [`UIColor`](../../UIKit/uicolor.md) object used to color an element.
- [var colorType: TVColorType](./colortype.md)
  The color type for an element.
- [enum TVColorType](../tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientColors: [UIColor]?](./gradientcolors.md)
  An array of colors used to create a gradient for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/gradientpoints)*