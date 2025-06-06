# NSWindow.StyleMask

**Framework**: AppKit  
**Kind**: struct

Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.

**Availability**:
- macOS ?+

## Declaration

```swift
struct StyleMask
```

## Topics

### Constants
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
- [static var hudWindow: NSWindow.StyleMask](nswindow/stylemask-swift.struct/hudwindow.md)
  The window is a HUD panel.
### Style Mask Creation
- [init(rawValue: UInt)](nswindow/stylemask-swift.struct/init(rawvalue:).md)
  Creates a style mask using the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var styleMask: NSWindow.StyleMask](nswindow/stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func toggleFullScreen(Any?)](nswindow/togglefullscreen(_:).md)
  Takes the window into or out of fullscreen mode,
- [var worksWhenModal: Bool](nswindow/workswhenmodal.md)
  A Boolean value that indicates whether the window is able to receive keyboard and mouse events even when some other window is being run modally.
- [var alphaValue: CGFloat](nswindow/alphavalue.md)
  The window’s alpha value.
- [var backgroundColor: NSColor!](nswindow/backgroundcolor.md)
  The color of the window’s background.
- [var colorSpace: NSColorSpace?](nswindow/colorspace.md)
  The window’s color space.
- [func setDynamicDepthLimit(Bool)](nswindow/setdynamicdepthlimit(_:).md)
  Sets a Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [var canHide: Bool](nswindow/canhide.md)
  A Boolean value that indicates whether the window can hide when its application becomes hidden.
- [var isOnActiveSpace: Bool](nswindow/isonactivespace.md)
  A Boolean value that indicates whether the window is on the currently active space.
- [var hidesOnDeactivate: Bool](nswindow/hidesondeactivate.md)
  A Boolean value that indicates whether the window is removed from the screen when its application becomes inactive.
- [var collectionBehavior: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.property.md)
  A value that identifies the window’s behavior in window collections.
- [var isOpaque: Bool](nswindow/isopaque.md)
  A Boolean value that indicates whether the window is opaque.
- [var hasShadow: Bool](nswindow/hasshadow.md)
  A Boolean value that indicates whether the window has a shadow.
- [func invalidateShadow()](nswindow/invalidateshadow.md)
  Invalidates the window shadow so that it is recomputed based on the current window shape.
- [func autorecalculatesContentBorderThickness(for: NSRectEdge) -> Bool](nswindow/autorecalculatescontentborderthickness(for:).md)
  Indicates whether the window calculates the thickness of a given border automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct)*