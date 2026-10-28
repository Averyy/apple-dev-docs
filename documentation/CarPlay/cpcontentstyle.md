# CPContentStyle

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

The types of content style that the vehicle allows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPContentStyle
```

```c
enum CPContentStyle : NSUInteger;
```

## Overview

The vehicle selects the content style according to the ambient light level. Your navigation app can use this value to determine the most appropriate style of map content to draw in its base view. The content style is independent of the user interface style, which controls light and dark mode.

You don’t create instances of `CPContentStyle`. Instead, the session configuration provides the current content style, and it notifies its delegate of any changes. See [`CPSessionConfiguration`](./cpsessionconfiguration.md) for more information.

## Topics

### Creating a Content Style
- [init(rawValue: UInt)](./cpcontentstyle/init%28rawvalue%29.md)
  Creates a content style from a raw value.
### Content Styles
- [static var dark: CPContentStyle](./cpcontentstyle/dark.md)
  The indication from the vehicle to draw the content in a dark style.
- [static var light: CPContentStyle](./cpcontentstyle/light.md)
  The indication from the vehicle to draw the content in a light style.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting the Content Style
- [var contentStyle: CPContentStyle](./cpsessionconfiguration/contentstyle.md)
  The content style that the vehicle selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontentstyle)*