# NSWindow.ToolbarStyle

**Framework**: AppKit  
**Kind**: enum

Styles that determine the appearance and location of the toolbar in relation to the title bar.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ToolbarStyle
```

## Topics

### Styles
- [NSWindow.ToolbarStyle.automatic](nswindow/toolbarstyle-swift.enum/automatic.md)
  A style indicating that the system determines the toolbar’s appearance and location.
- [NSWindow.ToolbarStyle.expanded](nswindow/toolbarstyle-swift.enum/expanded.md)
  A style indicating that the toolbar appears below the window title.
- [NSWindow.ToolbarStyle.preference](nswindow/toolbarstyle-swift.enum/preference.md)
  A style indicating that the toolbar appears below the window title with toolbar items centered in the toolbar.
- [NSWindow.ToolbarStyle.unified](nswindow/toolbarstyle-swift.enum/unified.md)
  A style indicating that the toolbar appears next to the window title.
- [NSWindow.ToolbarStyle.unifiedCompact](nswindow/toolbarstyle-swift.enum/unifiedcompact.md)
  A style indicating that the toolbar appears next to the window title and with reduced margins to allow more focus on the window’s contents.
### Initializers
- [init?(rawValue: Int)](nswindow/toolbarstyle-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](nswindow/standardwindowbutton(_:for:).md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](nswindow/standardwindowbutton(_:).md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var showsToolbarButton: Bool](nswindow/showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.
- [var titlebarAppearsTransparent: Bool](nswindow/titlebarappearstransparent.md)
  A Boolean value that indicates whether the title bar draws its background.
- [var toolbarStyle: NSWindow.ToolbarStyle](nswindow/toolbarstyle-swift.property.md)
  The style that determines the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](nswindow/titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](nswindow/windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/toolbarstyle-swift.enum)*