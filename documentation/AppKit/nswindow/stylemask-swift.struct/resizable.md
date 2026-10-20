# resizable

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window can be resized by the user.

**Availability**:
- macOS

## Declaration

```swift
static var resizable: NSWindow.StyleMask { get }
```

```c
NSWindowStyleMaskResizable
```

## See Also

### Constants
- [static var borderless: NSWindow.StyleMask](./borderless.md)
  The window displays none of the usual peripheral elements.
- [static var titled: NSWindow.StyleMask](./titled.md)
  The window displays a title bar.
- [static var closable: NSWindow.StyleMask](./closable.md)
  The window displays a close button.
- [static var miniaturizable: NSWindow.StyleMask](./miniaturizable.md)
  The window displays a minimize button.
- [static var unifiedTitleAndToolbar: NSWindow.StyleMask](./unifiedtitleandtoolbar.md)
  This constant has no effect, because all windows that include a toolbar use the unified style.
- [static var fullScreen: NSWindow.StyleMask](./fullscreen.md)
  The window can appear full screen. A fullscreen window does not draw its title bar, and may have special handling for its toolbar. (This mask is automatically toggled when [`toggleFullScreen(_:)`](../togglefullscreen%28_%29.md) is called.)
- [static var fullSizeContentView: NSWindow.StyleMask](./fullsizecontentview.md)
  When set, the window’s [`contentView`](../contentview.md) consumes the full size of the window. Although you can combine this constant with other window style masks, it is respected only for windows with a title bar. Note that using this mask opts in to layer-backing. Use the [`contentLayoutRect`](../contentlayoutrect.md) or the [`contentLayoutGuide`](../contentlayoutguide.md) to lay out views underneath the title bar–toolbar area.
- [static var utilityWindow: NSWindow.StyleMask](./utilitywindow.md)
  The window is a panel or a subclass of [`NSPanel`](../../nspanel.md).
- [static var docModalWindow: NSWindow.StyleMask](./docmodalwindow.md)
  The window is a document-modal panel (or  a subclass of [`NSPanel`](../../nspanel.md)).
- [static var nonactivatingPanel: NSWindow.StyleMask](./nonactivatingpanel.md)
  The window is a panel or a subclass of [`NSPanel`](../../nspanel.md) that does not activate the owning app.
- [static var hudWindow: NSWindow.StyleMask](./hudwindow.md)
  The window is a HUD panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/resizable)*