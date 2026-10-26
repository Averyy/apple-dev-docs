# UIButtonConfigurationCornerStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Settings that determine the appearance of the background corner radius.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```c
enum UIButtonConfigurationCornerStyle : NSInteger;
```

#### Overview

Use this property to control how the button uses the [`cornerRadius`](./uibackgroundconfiguration-c.class/cornerradius.md) property of the button’s [`background`](./uibuttonconfiguration/background.md).

## Topics

### Corner styles
- [UIButtonConfigurationCornerStyleDynamic](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstyledynamic.md)
  A style that adjusts the background corner radius for dynamic type.
- [UIButtonConfigurationCornerStyleFixed](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstylefixed.md)
  A style that uses the background corner radius without modification.
- [UIButtonConfigurationCornerStyleCapsule](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstylecapsule.md)
  A style that ignores the background corner radius and uses a corner radius that generates a capsule.
- [UIButtonConfigurationCornerStyleLarge](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstylelarge.md)
  A style that ignores the background corner radius and uses a large system-defined corner radius.
- [UIButtonConfigurationCornerStyleMedium](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstylemedium.md)
  A style that ignores the background corner radius and uses a medium system-defined corner radius.
- [UIButtonConfigurationCornerStyleSmall](./uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstylesmall.md)
  A style that ignores the background corner radius and uses a small system-defined corner radius.

## See Also

### Configuring the button background
- [background](./uibuttonconfiguration/background.md)
  The configuration to customize the button background.
- [cornerStyle](./uibuttonconfiguration/cornerstyle.md)
  The button style that controls the display behavior of the background corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfigurationcornerstyle)*