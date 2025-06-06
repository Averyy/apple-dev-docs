# NSButton.BezelStyle

**Framework**: AppKit  
**Kind**: enum

The set of bezel styles to style buttons in your app.

**Availability**:
- macOS ?+

## Declaration

```swift
enum BezelStyle
```

#### Overview

For design guidance on buttons, see [`Human Interface Guidelines > Buttons`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/buttons).

## Topics

### Default
- [NSButton.BezelStyle.automatic](nsbutton/bezelstyle-swift.enum/automatic.md)
  The default button style based on the button’s contents and position within the window.
### Push
- [NSButton.BezelStyle.push](nsbutton/bezelstyle-swift.enum/push.md)
  A standard push style button.
- [NSButton.BezelStyle.flexiblePush](nsbutton/bezelstyle-swift.enum/flexiblepush.md)
  A push button with a flexible height to accommodate longer text labels or an image.
### Disclosure
- [NSButton.BezelStyle.disclosure](nsbutton/bezelstyle-swift.enum/disclosure.md)
  A bezel style button for use with a disclosure triangle.
- [NSButton.BezelStyle.pushDisclosure](nsbutton/bezelstyle-swift.enum/pushdisclosure.md)
  A bezel style push button with a disclosure triangle.
### Toolbar
- [NSButton.BezelStyle.toolbar](nsbutton/bezelstyle-swift.enum/toolbar.md)
  A button style that’s appropriate for a toolbar item.
- [NSButton.BezelStyle.accessoryBar](nsbutton/bezelstyle-swift.enum/accessorybar.md)
  A button style that’s typically used in the context of an accessory toolbar for buttons that narrow the focus of a search or other operation.
- [NSButton.BezelStyle.accessoryBarAction](nsbutton/bezelstyle-swift.enum/accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
### Informational
- [NSButton.BezelStyle.helpButton](nsbutton/bezelstyle-swift.enum/helpbutton.md)
  A round button with a question mark, providing the standard help button look.
- [NSButton.BezelStyle.badge](nsbutton/bezelstyle-swift.enum/badge.md)
  A button style suitable for displaying additional information.
- [NSButton.BezelStyle.circular](nsbutton/bezelstyle-swift.enum/circular.md)
  A round button that can contain either a single character or an icon.
### Other
- [NSButton.BezelStyle.smallSquare](nsbutton/bezelstyle-swift.enum/smallsquare.md)
  A simple square bezel style that can scale to any size.
### Deprecated
- [Deprecated Symbols](bezelstyle-deprecated-symbols.md)
### Initializers
- [init?(rawValue: UInt)](nsbutton/bezelstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSButton.ButtonType](nsbutton/buttontype.md)
  Button types that you can specify using [`setButtonType(_:)`](nsbuttoncell/setbuttontype(_:).md).
- [NSButton.GradientType](nsbutton/gradienttype.md)
  Specify the gradients used by the [`gradientType`](nsbuttoncell/gradienttype.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum)*