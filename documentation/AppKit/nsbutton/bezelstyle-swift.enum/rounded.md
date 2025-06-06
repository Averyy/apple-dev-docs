# rounded

**Framework**: AppKit  
**Kind**: property

A rounded rectangle button, designed for text.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static var rounded: NSButton.BezelStyle { get }
```

#### Discussion

Rounded buttons are common within the body of a window or alert. To configure a button as the default button, set the [`keyEquivalent`](nsbutton/keyequivalent.md) property to the carriage return character (`\r`, ASCII `0xd`). The system draws the default button prominently using the accent color to indicate that the user can press the return key to invoke the button’s action.

## See Also

- [static var inline: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/inline.md)
  A button that has a solid round-rectangle border background.
- [static var recessed: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/recessed.md)
  A bezel style appropriate for use in scope bars and title bar accessories, similar to the bookmarks bar in Safari.
- [static var regularSquare: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/regularsquare.md)
  A rectangular button with a two-point border, designed for icons.
- [static var roundedDisclosure: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/roundeddisclosure.md)
  A bezel style for use with a vertically expanding and collapsing disclosure button.
- [static var roundRect: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/roundrect.md)
  A bezel style appropriate for use as an action or auxiliary button in scope bars and title bar accessories.
- [static var texturedRounded: NSButton.BezelStyle](nsbutton/bezelstyle-swift.enum/texturedrounded.md)
  A bezel style appropriate for use in the toolbar or title bar regions of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/rounded)*