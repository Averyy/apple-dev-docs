# windowTitlebarLayoutDirection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The direction the window’s title bar lays text out, either left to right or right to left.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection { get }
```

```objc
@property (readonly) NSUserInterfaceLayoutDirection windowTitlebarLayoutDirection;
```

#### Discussion

The layout direction of the window title bar includes the standard window buttons (close, minimize, maximize) and the title for the window. In general, this returns [`NSUserInterfaceLayoutDirection.rightToLeft`](../nsuserinterfacelayoutdirection/righttoleft.md) if the primary system language is right to left. The layout direction may be right to left even in applications that don’t have a right to left language localization. Refer to this value if the application uses [`titlebarAppearsTransparent`](./titlebarappearstransparent.md) and places controls under the title bar.

## See Also

### Managing Title Bars
- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](./standardwindowbutton%28_,for%29.md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](./standardwindowbutton%28_%29.md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var titlebarAppearsTransparent: Bool](./titlebarappearstransparent.md)
  A Boolean value that indicates whether the title bar draws its background.
- [var toolbarStyle: NSWindow.ToolbarStyle](./toolbarstyle-swift.property.md)
  The style that determines the appearance and location of the toolbar in relation to the title bar.
- [NSWindow.ToolbarStyle](./toolbarstyle-swift.enum.md)
  Styles that determine the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](./titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/windowtitlebarlayoutdirection)*