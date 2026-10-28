# inline

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A button that has a solid round-rectangle border background.

**Availability**:
- macOS 10.7+ - Deprecated in 27.0 (renamed: NSButton.BezelStyle.badge)

## Declaration

```swift
static var inline: NSButton.BezelStyle { get }
```

```c
NSBezelStyleInline
```

## Discussion

Common uses of this button style include:

- An inline button in a table view, such as a stop progress button in a download panel
- An “unread” indicator in an outline view

Use text for an unread indicator and a template image for other buttons.

## See Also

### Deprecated properties
- [static var recessed: NSButton.BezelStyle](./recessed.md)
  A bezel style appropriate for use in scope bars and title bar accessories, similar to the bookmarks bar in Safari.
- [static var regularSquare: NSButton.BezelStyle](./regularsquare.md)
  A rectangular button with a two-point border, designed for icons.
- [static var rounded: NSButton.BezelStyle](./rounded.md)
  A rounded rectangle button, designed for text.
- [static var roundedDisclosure: NSButton.BezelStyle](./roundeddisclosure.md)
  A bezel style for use with a vertically expanding and collapsing disclosure button.
- [static var roundRect: NSButton.BezelStyle](./roundrect.md)
  A bezel style appropriate for use as an action or auxiliary button in scope bars and title bar accessories.
- [static var texturedRounded: NSButton.BezelStyle](./texturedrounded.md)
  A bezel style appropriate for use in the toolbar or title bar regions of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/inline)*