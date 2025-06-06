# cornerStyle

**Framework**: UIKit  
**Kind**: property

The button style that controls the display behavior of the background corner radius.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var cornerStyle: UIButton.Configuration.CornerStyle { get set }
```

#### Discussion

This property controls the behavior of the [`cornerRadius`](uibackgroundconfiguration-swift.struct/cornerradius.md) you set on the configuration background. The default corner style is [`UIButton.Configuration.CornerStyle.dynamic`](uibutton/configuration-swift.struct/cornerstyle-swift.enum/dynamic.md).

## See Also

- [var background: UIBackgroundConfiguration](uibutton/configuration-swift.struct/background.md)
  The configuration to customize the button background.
- [UIButton.Configuration.CornerStyle](uibutton/configuration-swift.struct/cornerstyle-swift.enum.md)
  Settings that determine the appearance of the background corner radius.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/cornerstyle-swift.property)*