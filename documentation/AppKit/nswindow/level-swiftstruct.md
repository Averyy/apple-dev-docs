# NSWindow.Level

**Framework**: AppKit  
**Kind**: struct

The standard window levels in macOS.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Level
```

#### Discussion

The stacking of levels takes precedence over the stacking of windows within each level. That is, even the bottom window in a level will obscure the top window of the next level down. Levels are listed in order from lowest to highest. These constants are mapped (using `#define` statements) to corresponding elements in [`CGWindowLevelKey`](https://developer.apple.com/documentation/CoreGraphics/CGWindowLevelKey).

## Topics

### Constants
- [static let dock: NSWindow.Level](nswindow/level-swift.struct/dock.md)
  The level for the dock.
- [static let floating: NSWindow.Level](nswindow/level-swift.struct/floating.md)
  Useful for floating palettes.
- [static let mainMenu: NSWindow.Level](nswindow/level-swift.struct/mainmenu.md)
  Reserved for the application’s main menu.
- [static let modalPanel: NSWindow.Level](nswindow/level-swift.struct/modalpanel.md)
  The level for a modal panel.
- [static let normal: NSWindow.Level](nswindow/level-swift.struct/normal.md)
  The default level for `NSWindow` objects.
- [static let popUpMenu: NSWindow.Level](nswindow/level-swift.struct/popupmenu.md)
  The level for a pop-up menu.
- [static let screenSaver: NSWindow.Level](nswindow/level-swift.struct/screensaver.md)
  The level for a screen saver.
- [static let statusBar: NSWindow.Level](nswindow/level-swift.struct/statusbar.md)
  The level for a status window.
- [static let submenu: NSWindow.Level](nswindow/level-swift.struct/submenu.md)
  Reserved for submenus. Synonymous with `NSTornOffMenuWindowLevel`, which is preferred.
- [static let tornOffMenu: NSWindow.Level](nswindow/level-swift.struct/tornoffmenu.md)
  The level for a torn-off menu. Synonymous with `NSSubmenuWindowLevel`.
### Creating a Window Level
- [init(Int)](nswindow/level-swift.struct/init(_:).md)
  Creates a window level using the given integer value.
- [init(rawValue: Int)](nswindow/level-swift.struct/init(rawvalue:).md)
  Creates a window level using the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](nswindow/orderback(_:).md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](nswindow/orderfront(_:).md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](nswindow/orderfrontregardless.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](nswindow/order(_:relativeto:).md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](nswindow/level-swift.property.md)
  The window level of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/level-swift.struct)*