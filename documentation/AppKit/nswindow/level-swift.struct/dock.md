# dock

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The level for the dock.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Deprecated. There is no replacement.

## Declaration

```swift
static var dock: NSWindow.Level { get }
```

```c
static const NSWindowLevel NSDockWindowLevel;
```

## See Also

### Constants
- [static var floating: NSWindow.Level](./floating.md)
  Useful for floating palettes.
- [static var mainMenu: NSWindow.Level](./mainmenu.md)
  Reserved for the application’s main menu.
- [static var modalPanel: NSWindow.Level](./modalpanel.md)
  The level for a modal panel.
- [static var normal: NSWindow.Level](./normal.md)
  The default level for `NSWindow` objects.
- [static var popUpMenu: NSWindow.Level](./popupmenu.md)
  The level for a pop-up menu.
- [static var screenSaver: NSWindow.Level](./screensaver.md)
  The level for a screen saver.
- [static var statusBar: NSWindow.Level](./statusbar.md)
  The level for a status window.
- [static var submenu: NSWindow.Level](./submenu.md)
  Reserved for submenus. Synonymous with `NSTornOffMenuWindowLevel`, which is preferred.
- [static var tornOffMenu: NSWindow.Level](./tornoffmenu.md)
  The level for a torn-off menu. Synonymous with `NSSubmenuWindowLevel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/level-swift.struct/dock)*