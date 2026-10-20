# TVColor

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

The color data used by styles.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVColor
```

```objc
@interface TVColor : NSObject
```

## Topics

### Getting Color Properties
- [var color: UIColor?](./tvcolor/color.md)
  A [`UIColor`](../UIKit/uicolor.md) object used to color an element.
- [var colorType: TVColorType](./tvcolor/colortype.md)
  The color type for an element.
- [enum TVColorType](./tvcolortype.md)
  Designates how color for an element is to be displayed.
- [var gradientColors: [UIColor]?](./tvcolor/gradientcolors.md)
  An array of colors used to create a gradient for an element.
- [var gradientPoints: [NSNumber]?](./tvcolor/gradientpoints.md)
  An array of points used to determine gradient color changes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom Styles
- [class TVViewElementStyle](./tvviewelementstyle.md)
  A style applied to a view element.
- [class TVStyleFactory](./tvstylefactory.md)
  An object used to register custom style properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvcolor)*