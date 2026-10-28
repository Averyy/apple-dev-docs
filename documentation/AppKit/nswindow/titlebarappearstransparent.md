# titlebarAppearsTransparent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the title bar draws its background.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var titlebarAppearsTransparent: Bool { get set }
```

```objc
@property BOOL titlebarAppearsTransparent;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the title bar does not draw its background, which allows all content underneath it to show through. It only makes sense to set this property to [`true`](../../Swift/true.md) when [`NSFullSizeContentViewWindowMask`](../nsfullsizecontentviewwindowmask.md) is also set.

## See Also

### Managing Title Bars
- [class func standardWindowButton(NSWindow.ButtonType, for: NSWindow.StyleMask) -> NSButton?](./standardwindowbutton%28_,for%29.md)
  Returns a new instance of a given standard window button, sized appropriately for a given window style.
- [func standardWindowButton(NSWindow.ButtonType) -> NSButton?](./standardwindowbutton%28_%29.md)
  Returns the window button of a given window button kind in the window’s view hierarchy.
- [var toolbarStyle: NSWindow.ToolbarStyle](./toolbarstyle-swift.property.md)
  The style that determines the appearance and location of the toolbar in relation to the title bar.
- [NSWindow.ToolbarStyle](./toolbarstyle-swift.enum.md)
  Styles that determine the appearance and location of the toolbar in relation to the title bar.
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](./titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](./windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlebarappearstransparent)*