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
- visionOS

## Declaration

```swift
var cornerStyle: UIButton.Configuration.CornerStyle { get set }
```

#### Discussion

This property controls the behavior of the [`cornerRadius`](../../uibackgroundconfiguration-swift.struct/cornerradius.md) you set on the configuration background. The default corner style is [`UIButton.Configuration.CornerStyle.dynamic`](./cornerstyle-swift.enum/dynamic.md).

## See Also

### Configuring the button background
- [var background: UIBackgroundConfiguration](./background.md)
  The configuration to customize the button background.
- [UIButton.Configuration.CornerStyle](./cornerstyle-swift.enum.md)
  Settings that determine the appearance of the background corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.property)*