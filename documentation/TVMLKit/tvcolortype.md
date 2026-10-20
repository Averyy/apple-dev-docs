# TVColorType

**Framework**: TVMLKit  
**Kind**: enum  
**Role**: Enumeration

Designates how color for an element is to be displayed.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
enum TVColorType
```

```c
enum TVColorType : NSInteger;
```

## Topics

### Constants
- [TVColorType.none](./tvcolortype/none.md)
  Indicates that there is no color associated with an element.
- [TVColorType.plain](./tvcolortype/plain.md)
  Indicates that a single color is to be used with an element.
- [TVColorType.linearGradientTopToBottom](./tvcolortype/lineargradienttoptobottom.md)
  Indicates that a color gradient goes from the top to the bottom of an element.
- [TVColorType.linearGradientLeftToRight](./tvcolortype/lineargradientlefttoright.md)
  Indicates that a color gradient goes from the left to the right of an element.
### Initializers
- [init?(rawValue: Int)](./tvcolortype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Color Properties
- [var color: UIColor?](./tvcolor/color.md)
  A [`UIColor`](../UIKit/uicolor.md) object used to color an element.
- [var colorType: TVColorType](./tvcolor/colortype.md)
  The color type for an element.
- [var gradientColors: [UIColor]?](./tvcolor/gradientcolors.md)
  An array of colors used to create a gradient for an element.
- [var gradientPoints: [NSNumber]?](./tvcolor/gradientpoints.md)
  An array of points used to determine gradient color changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolortype)*