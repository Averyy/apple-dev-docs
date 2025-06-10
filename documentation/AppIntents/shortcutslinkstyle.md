# ShortcutsLinkStyle

**Framework**: App Intents  
**Kind**: struct

The styles to apply to buttons you use to open your app’s page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct ShortcutsLinkStyle
```

#### Overview

Specify a [`ShortcutsLinkStyle`](shortcutslinkstyle.md) value when you add a [`ShortcutsUIButton`](shortcutsuibutton.md) or [`ShortcutsLink`](shortcutslink.md) type to your interface. For the [`ShortcutsLink`](shortcutslink.md) type, specify the style using the [`shortcutsLinkStyle(_:)`](shortcutslink/shortcutslinkstyle(_:).md) modifier.

## Topics

### Getting the styles
- [static let automatic: ShortcutsLinkStyle](shortcutslinkstyle/automatic.md)
  The default button style, based on the current color scheme.
- [static let automaticOutline: ShortcutsLinkStyle](shortcutslinkstyle/automaticoutline.md)
  The default button style with an outline, based on the current color scheme.
- [static let dark: ShortcutsLinkStyle](shortcutslinkstyle/dark.md)
  A button style that applies a dark background with light text.
- [static let darkOutline: ShortcutsLinkStyle](shortcutslinkstyle/darkoutline.md)
  A button style that applies a dark background with light text along with a light outline.
- [static let light: ShortcutsLinkStyle](shortcutslinkstyle/light.md)
  A button style that applies a light background with dark text.
- [static let lightOutline: ShortcutsLinkStyle](shortcutslinkstyle/lightoutline.md)
  A button style that applies a light background with dark text along with a dark outline.

## See Also

- [class ShortcutsUIButton](shortcutsuibutton.md)
  A button that opens the current app’s page in the Shortcuts app.
- [struct ShortcutsLink](shortcutslink.md)
  A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslinkstyle)*