# UIButton.Configuration.CornerStyle

**Framework**: UIKit  
**Kind**: enum

Settings that determine the appearance of the background corner radius.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
enum CornerStyle
```

#### Overview

Use this property to control how the button uses the [`cornerRadius`](uibackgroundconfiguration-swift.struct/cornerradius.md) property of the button’s [`background`](uibutton/configuration-swift.struct/background.md).

## Topics

### Corner styles
- [UIButton.Configuration.CornerStyle.dynamic](uibutton/configuration-swift.struct/cornerstyle-swift.enum/dynamic.md)
  A style that adjusts the background corner radius for dynamic type.
- [UIButton.Configuration.CornerStyle.fixed](uibutton/configuration-swift.struct/cornerstyle-swift.enum/fixed.md)
  A style that uses the background corner radius without modification.
- [UIButton.Configuration.CornerStyle.capsule](uibutton/configuration-swift.struct/cornerstyle-swift.enum/capsule.md)
  A style that ignores the background corner radius and uses a corner radius that generates a capsule.
- [UIButton.Configuration.CornerStyle.large](uibutton/configuration-swift.struct/cornerstyle-swift.enum/large.md)
  A style that ignores the background corner radius and uses a large system-defined corner radius.
- [UIButton.Configuration.CornerStyle.medium](uibutton/configuration-swift.struct/cornerstyle-swift.enum/medium.md)
  A style that ignores the background corner radius and uses a medium system-defined corner radius.
- [UIButton.Configuration.CornerStyle.small](uibutton/configuration-swift.struct/cornerstyle-swift.enum/small.md)
  A style that ignores the background corner radius and uses a small system-defined corner radius.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var background: UIBackgroundConfiguration](uibutton/configuration-swift.struct/background.md)
  The configuration to customize the button background.
- [var cornerStyle: UIButton.Configuration.CornerStyle](uibutton/configuration-swift.struct/cornerstyle-swift.property.md)
  The button style that controls the display behavior of the background corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.enum)*