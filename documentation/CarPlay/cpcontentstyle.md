# CPContentStyle

**Framework**: CarPlay  
**Kind**: struct

The types of content style that the vehicle allows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPContentStyle
```

#### Overview

The vehicle selects the content style according to the ambient light level. Your navigation app can use this value to determine the most appropriate style of map content to draw in its base view. The content style is independent of the user interface style, which controls light and dark mode.

You don’t create instances of `CPContentStyle`. Instead, the session configuration provides the current content style, and it notifies its delegate of any changes. See [`CPSessionConfiguration`](cpsessionconfiguration.md) for more information.

## Topics

### Creating a Content Style
- [init(rawValue: UInt)](cpcontentstyle/init(rawvalue:).md)
  Creates a content style from a raw value.
### Content Styles
- [static var dark: CPContentStyle](cpcontentstyle/dark.md)
  The indication from the vehicle to draw the content in a dark style.
- [static var light: CPContentStyle](cpcontentstyle/light.md)
  The indication from the vehicle to draw the content in a light style.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var contentStyle: CPContentStyle](cpsessionconfiguration/contentstyle.md)
  The content style that the vehicle selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontentstyle)*