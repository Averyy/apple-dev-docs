# hudWindow

**Framework**: AppKit  
**Kind**: property

The window is a HUD panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var hudWindow: NSWindow.StyleMask { get }
```

## See Also

- [static var borderless: NSWindow.StyleMask](nswindow/stylemask-swift.struct/borderless.md)
  The window displays none of the usual peripheral elements. Useful only for display or caching purposes. A window that uses `NSWindowStyleMaskBorderless` can’t become key or main, unless the value of [`canBecomeKey`](nswindow/canbecomekey.md) or [`canBecomeMain`](nswindow/canbecomemain.md) is [`true`](https://developer.apple.com/documentation/swift/true). Note that you can set a window’s or panel’s style mask to `NSWindowStyleMaskBorderless` in Interface Builder by deselecting Title Bar in the Appearance section of the Attributes inspector.
- [static var titled: NSWindow.StyleMask](nswindow/stylemask-swift.struct/titled.md)
  The window displays a title bar.
- [static var closable: NSWindow.StyleMask](nswindow/stylemask-swift.struct/closable.md)
  The window displays a close button.
- [static var miniaturizable: NSWindow.StyleMask](nswindow/stylemask-swift.struct/miniaturizable.md)
  The window displays a minimize button.
- [static var resizable: NSWindow.StyleMask](nswindow/stylemask-swift.struct/resizable.md)
  The window can be resized by the user.
- [static var texturedBackground: NSWindow.StyleMask](nswindow/stylemask-swift.struct/texturedbackground.md)
  The window uses a textured background that darkens when the window is key or main and lightens when it is inactive, and may have a second gradient in the section below the window content.
- [static var unifiedTitleAndToolbar: NSWindow.StyleMask](nswindow/stylemask-swift.struct/unifiedtitleandtoolbar.md)
  This constant has no effect, because all windows that include a toolbar use the unified style.
- [static var fullScreen: NSWindow.StyleMask](nswindow/stylemask-swift.struct/fullscreen.md)
  The window can appear full screen. A fullscreen window does not draw its title bar, and may have special handling for its toolbar. (This mask is automatically toggled when [`toggleFullScreen(_:)`](nswindow/togglefullscreen(_:).md) is called.)
- [static var fullSizeContentView: NSWindow.StyleMask](nswindow/stylemask-swift.struct/fullsizecontentview.md)
  When set, the window’s [`contentView`](nswindow/contentview.md) consumes the full size of the window. Although you can combine this constant with other window style masks, it is respected only for windows with a title bar. Note that using this mask opts in to layer-backing. Use the [`contentLayoutRect`](nswindow/contentlayoutrect.md) or the [`contentLayoutGuide`](nswindow/contentlayoutguide.md) to lay out views underneath the title bar–toolbar area.
- [static var utilityWindow: NSWindow.StyleMask](nswindow/stylemask-swift.struct/utilitywindow.md)
  The window is a panel or a subclass of [`NSPanel`](nspanel.md).
- [static var docModalWindow: NSWindow.StyleMask](nswindow/stylemask-swift.struct/docmodalwindow.md)
  The window is a document-modal panel (or  a subclass of [`NSPanel`](nspanel.md)).
- [static var nonactivatingPanel: NSWindow.StyleMask](nswindow/stylemask-swift.struct/nonactivatingpanel.md)
  The window is a panel or a subclass of [`NSPanel`](nspanel.md) that does not activate the owning app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow)*