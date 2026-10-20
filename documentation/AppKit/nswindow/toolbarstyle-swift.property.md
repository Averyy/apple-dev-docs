# toolbarStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The style that determines the appearance and location of the toolbar in relation to the title bar.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var toolbarStyle: NSWindow.ToolbarStyle { get set }
```

```objc
@property NSWindowToolbarStyle toolbarStyle;
```

#### Discussion

The default value is [`NSWindow.ToolbarStyle.automatic`](./toolbarstyle-swift.enum/automatic.md).

## See Also

### Managing Title Bars
- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](./standardwindowbutton%28_,for%29.md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](./standardwindowbutton%28_%29.md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var titlebarAppearsTransparent: Bool](./titlebarappearstransparent.md)
  A Boolean value that indicates whether the title bar draws its background.
- [NSWindow.ToolbarStyle](./toolbarstyle-swift.enum.md)
  Styles that determine the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](./titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](./windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/toolbarstyle-swift.property)*