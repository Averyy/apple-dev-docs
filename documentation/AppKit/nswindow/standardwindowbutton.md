# standardWindowButton(_:)

**Framework**: AppKit  
**Kind**: method

Returns the window button of a given window button kind in the window’s view hierarchy.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func standardWindowButton(_ b: NSWindow.ButtonType) -> NSButton?
```

#### Return Value

Window button in the window’s view hierarchy of the type identified by `b`; `nil` when such button is not in the window’s view hierarchy.

## Parameters

- `b`: The type of standard window button to return.

## See Also

- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](nswindow/standardwindowbutton(_:for:).md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [var showsToolbarButton: Bool](nswindow/showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.
- [var titlebarAppearsTransparent: Bool](nswindow/titlebarappearstransparent.md)
  A Boolean value that indicates whether the title bar draws its background.
- [var toolbarStyle: NSWindow.ToolbarStyle](nswindow/toolbarstyle-swift.property.md)
  The style that determines the appearance and location of the toolbar in relation to the title bar.
- [NSWindow.ToolbarStyle](nswindow/toolbarstyle-swift.enum.md)
  Styles that determine the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](nswindow/titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](nswindow/windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/standardwindowbutton(_:))*