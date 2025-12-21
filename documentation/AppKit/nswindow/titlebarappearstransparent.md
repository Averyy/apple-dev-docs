# titlebarAppearsTransparent

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the title bar draws its background.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var titlebarAppearsTransparent: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the title bar does not draw its background, which allows all content underneath it to show through. It only makes sense to set this property to [`true`](https://developer.apple.com/documentation/Swift/true) when [`NSFullSizeContentViewWindowMask`](nsfullsizecontentviewwindowmask.md) is also set.

## See Also

- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](nswindow/standardwindowbutton(_:for:).md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](nswindow/standardwindowbutton(_:).md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var showsToolbarButton: Bool](nswindow/showstoolbarbutton.md)
  A Boolean value that indicates whether the toolbar control button is currently displayed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlebarappearstransparent)*