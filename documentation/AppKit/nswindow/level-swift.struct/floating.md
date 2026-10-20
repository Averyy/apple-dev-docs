# floating

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Useful for floating palettes.

**Availability**:
- macOS

## Declaration

```swift
static var floating: NSWindow.Level { get }
```

```c
static const NSWindowLevel NSFloatingWindowLevel;
```

## See Also

### Constants
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
- [static var dock: NSWindow.Level](./dock.md)
  The level for the dock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/level-swift.struct/floating)*