# NSWindow.Level

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The standard window levels in macOS.

**Availability**:
- macOS

## Declaration

```swift
struct Level
```

```c
typedef NSInteger NSWindowLevel;
```

## Discussion

The stacking of levels takes precedence over the stacking of windows within each level. That is, even the bottom window in a level will obscure the top window of the next level down. Levels are listed in order from lowest to highest. These constants are mapped (using `#define` statements) to corresponding elements in [`CGWindowLevelKey`](../../CoreGraphics/cgwindowlevelkey.md).

## Topics

### Constants
- [static var floating: NSWindow.Level](./level-swift.struct/floating.md)
  Useful for floating palettes.
- [static var mainMenu: NSWindow.Level](./level-swift.struct/mainmenu.md)
  Reserved for the application’s main menu.
- [static var modalPanel: NSWindow.Level](./level-swift.struct/modalpanel.md)
  The level for a modal panel.
- [static var normal: NSWindow.Level](./level-swift.struct/normal.md)
  The default level for `NSWindow` objects.
- [static var popUpMenu: NSWindow.Level](./level-swift.struct/popupmenu.md)
  The level for a pop-up menu.
- [static var screenSaver: NSWindow.Level](./level-swift.struct/screensaver.md)
  The level for a screen saver.
- [static var statusBar: NSWindow.Level](./level-swift.struct/statusbar.md)
  The level for a status window.
- [static var submenu: NSWindow.Level](./level-swift.struct/submenu.md)
  Reserved for submenus. Synonymous with `NSTornOffMenuWindowLevel`, which is preferred.
- [static var tornOffMenu: NSWindow.Level](./level-swift.struct/tornoffmenu.md)
  The level for a torn-off menu. Synonymous with `NSSubmenuWindowLevel`.
- [static var dock: NSWindow.Level](./level-swift.struct/dock.md)
  The level for the dock.
### Creating a Window Level
- [init(Int)](./level-swift.struct/init%28_%29.md)
  Creates a window level using the given integer value.
- [init(rawValue: Int)](./level-swift.struct/init%28rawvalue%29.md)
  Creates a window level using the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Window Layers
- [func orderOut(Any?)](./orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](./orderfrontregardless%28%29.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](./order%28_,relativeto%29.md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/level-swift.struct)*