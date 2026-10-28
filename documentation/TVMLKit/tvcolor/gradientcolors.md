# gradientColors

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

An array of colors used to create a gradient for an element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var gradientColors: [UIColor]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<UIColor *> * gradientColors;
```

## Discussion

This property is only available when [`colorType`](./colortype.md) is set to [`TVColorType.linearGradientTopToBottom`](../tvcolortype/lineargradienttoptobottom.md) or [`TVColorType.linearGradientLeftToRight`](../tvcolortype/lineargradientlefttoright.md).

## See Also

### Getting Color Properties
- [var color: UIColor?](./color.md)
  A [`UIColor`](../../UIKit/uicolor.md) object used to color an element.
- [var colorType: TVColorType](./colortype.md)
  The color type for an element.
- [enum TVColorType](../tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientPoints: [NSNumber]?](./gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor/gradientcolors)*