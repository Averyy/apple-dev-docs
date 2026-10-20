# NSWindow.ToolbarStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Styles that determine the appearance and location of the toolbar in relation to the title bar.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ToolbarStyle
```

```c
enum NSWindowToolbarStyle : NSInteger;
```

## Topics

### Styles
- [NSWindow.ToolbarStyle.automatic](./toolbarstyle-swift.enum/automatic.md)
  A style indicating that the system determines the toolbar’s appearance and location.
- [NSWindow.ToolbarStyle.expanded](./toolbarstyle-swift.enum/expanded.md)
  A style indicating that the toolbar appears below the window title.
- [NSWindow.ToolbarStyle.preference](./toolbarstyle-swift.enum/preference.md)
  A style indicating that the toolbar appears below the window title with toolbar items centered in the toolbar.
- [NSWindow.ToolbarStyle.unified](./toolbarstyle-swift.enum/unified.md)
  A style indicating that the toolbar appears next to the window title.
- [NSWindow.ToolbarStyle.unifiedCompact](./toolbarstyle-swift.enum/unifiedcompact.md)
  A style indicating that the toolbar appears next to the window title and with reduced margins to allow more focus on the window’s contents.
### Initializers
- [init?(rawValue: Int)](./toolbarstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var titlebarSeparatorStyle: NSTitlebarSeparatorStyle](./titlebarseparatorstyle.md)
  The type of separator that the app displays between the title bar and content of a window.
- [enum NSTitlebarSeparatorStyle](../nstitlebarseparatorstyle.md)
  Styles that determine the type of separator displayed between the title bar and content of a window.
- [var windowTitlebarLayoutDirection: NSUserInterfaceLayoutDirection](./windowtitlebarlayoutdirection.md)
  The direction the window’s title bar lays text out, either left to right or right to left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/toolbarstyle-swift.enum)*