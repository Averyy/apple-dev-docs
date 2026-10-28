# NSButton.BezelStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The set of bezel styles to style buttons in your app.

**Availability**:
- macOS

## Declaration

```swift
enum BezelStyle
```

```c
enum NSBezelStyle : NSUInteger;
```

## Overview

For design guidance on buttons, see [Human Interface Guidelines > Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

## Topics

### Default
- [NSButton.BezelStyle.automatic](./bezelstyle-swift.enum/automatic.md)
  The default button style based on the button’s contents and position within the window.
### Push
- [NSButton.BezelStyle.push](./bezelstyle-swift.enum/push.md)
  A standard push style button.
- [NSButton.BezelStyle.flexiblePush](./bezelstyle-swift.enum/flexiblepush.md)
  A push button with a flexible height to accommodate longer text labels or an image.
### Disclosure
- [NSButton.BezelStyle.disclosure](./bezelstyle-swift.enum/disclosure.md)
  A bezel style button for use with a disclosure triangle.
- [NSButton.BezelStyle.pushDisclosure](./bezelstyle-swift.enum/pushdisclosure.md)
  A bezel style push button with a disclosure triangle.
### Toolbar
- [NSButton.BezelStyle.toolbar](./bezelstyle-swift.enum/toolbar.md)
  A button style that’s appropriate for a toolbar item.
- [NSButton.BezelStyle.accessoryBar](./bezelstyle-swift.enum/accessorybar.md)
  A button style that’s typically used in the context of an accessory toolbar for buttons that narrow the focus of a search or other operation.
- [NSButton.BezelStyle.accessoryBarAction](./bezelstyle-swift.enum/accessorybaraction.md)
  A button style that you use for extra actions in an accessory toolbar.
### Informational
- [NSButton.BezelStyle.helpButton](./bezelstyle-swift.enum/helpbutton.md)
  A round button with a question mark, providing the standard help button look.
- [NSButton.BezelStyle.badge](./bezelstyle-swift.enum/badge.md)
  A button style suitable for displaying additional information.
- [NSButton.BezelStyle.circular](./bezelstyle-swift.enum/circular.md)
  A round button that can contain either a single character or an icon.
### Other
- [NSButton.BezelStyle.smallSquare](./bezelstyle-swift.enum/smallsquare.md)
  A simple square bezel style that can scale to any size.
### Deprecated
- [Deprecated symbols](../bezelstyle-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Enumeration Cases
- [NSButton.BezelStyle.glass](./bezelstyle-swift.enum/glass.md)
  A bezel style with a glass effect
### Initializers
- [init?(rawValue: UInt)](./bezelstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSButton.ButtonType](./buttontype.md)
  Button types that you can specify using [`setButtonType(_:)`](../nsbuttoncell/setbuttontype%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum)*