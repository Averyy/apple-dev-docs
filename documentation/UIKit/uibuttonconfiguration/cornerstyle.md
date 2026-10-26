# cornerStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The button style that controls the display behavior of the background corner radius.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationCornerStyle cornerStyle;
```

#### Discussion

This property controls the behavior of the [`cornerRadius`](../uibackgroundconfiguration-c.class/cornerradius.md) you set on the configuration background. The default corner style is [`UIButtonConfigurationCornerStyleDynamic`](../uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstyledynamic.md).

## See Also

### Configuring the button background
- [background](./background.md)
  The configuration to customize the button background.
- [UIButtonConfigurationCornerStyle](../uibuttonconfigurationcornerstyle.md)
  Settings that determine the appearance of the background corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/cornerstyle)*