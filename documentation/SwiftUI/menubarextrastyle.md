# MenuBarExtraStyle

**Framework**: SwiftUI  
**Kind**: protocol

A specification for the appearance and behavior of a menu bar extra scene.

**Availability**:
- macOS 13.0+

## Declaration

```swift
protocol MenuBarExtraStyle
```

## Topics

### Getting menu bar extra styles
- [static var automatic: AutomaticMenuBarExtraStyle](menubarextrastyle/automatic.md)
  The default menu bar extra style.
- [static var menu: PullDownMenuBarExtraStyle](menubarextrastyle/menu.md)
  A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [static var window: WindowMenuBarExtraStyle](menubarextrastyle/window.md)
  A menu bar extra style that renders its contents in a popover-like window.
### Supporting types
- [struct AutomaticMenuBarExtraStyle](automaticmenubarextrastyle.md)
  The default menu bar extra style. You can also use [`automatic`](menubarextrastyle/automatic.md) to construct this style.
- [struct PullDownMenuBarExtraStyle](pulldownmenubarextrastyle.md)
  A menu bar extra style that renders its contents as a menu that pulls down from the icon in the menu bar.
- [struct WindowMenuBarExtraStyle](windowmenubarextrastyle.md)
  A menu bar extra style that renders its contents in a popover-like window.

## Relationships

### Conforming Types
- [AutomaticMenuBarExtraStyle](automaticmenubarextrastyle.md)
- [PullDownMenuBarExtraStyle](pulldownmenubarextrastyle.md)
- [WindowMenuBarExtraStyle](windowmenubarextrastyle.md)

## See Also

- [struct MenuBarExtra](menubarextra.md)
  A scene that renders itself as a persistent control in the system menu bar.
- [func menuBarExtraStyle<S>(S) -> some Scene](scene/menubarextrastyle(_:).md)
  Sets the style for menu bar extra created by this scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menubarextrastyle)*