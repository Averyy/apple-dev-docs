# NSWindow.StyleMask

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.

**Availability**:
- macOS

## Declaration

```swift
struct StyleMask
```

```c
enum NSWindowStyleMask : NSUInteger;
```

## Topics

### Constants
- [static var borderless: NSWindow.StyleMask](./stylemask-swift.struct/borderless.md)
  The window displays none of the usual peripheral elements.
- [static var titled: NSWindow.StyleMask](./stylemask-swift.struct/titled.md)
  The window displays a title bar.
- [static var closable: NSWindow.StyleMask](./stylemask-swift.struct/closable.md)
  The window displays a close button.
- [static var miniaturizable: NSWindow.StyleMask](./stylemask-swift.struct/miniaturizable.md)
  The window displays a minimize button.
- [static var resizable: NSWindow.StyleMask](./stylemask-swift.struct/resizable.md)
  The window can be resized by the user.
- [static var unifiedTitleAndToolbar: NSWindow.StyleMask](./stylemask-swift.struct/unifiedtitleandtoolbar.md)
  This constant has no effect, because all windows that include a toolbar use the unified style.
- [static var fullScreen: NSWindow.StyleMask](./stylemask-swift.struct/fullscreen.md)
  The window can appear full screen. A fullscreen window does not draw its title bar, and may have special handling for its toolbar. (This mask is automatically toggled when [`toggleFullScreen(_:)`](./togglefullscreen%28_%29.md) is called.)
- [static var fullSizeContentView: NSWindow.StyleMask](./stylemask-swift.struct/fullsizecontentview.md)
  When set, the window’s [`contentView`](./contentview.md) consumes the full size of the window. Although you can combine this constant with other window style masks, it is respected only for windows with a title bar. Note that using this mask opts in to layer-backing. Use the [`contentLayoutRect`](./contentlayoutrect.md) or the [`contentLayoutGuide`](./contentlayoutguide.md) to lay out views underneath the title bar–toolbar area.
- [static var utilityWindow: NSWindow.StyleMask](./stylemask-swift.struct/utilitywindow.md)
  The window is a panel or a subclass of [`NSPanel`](../nspanel.md).
- [static var docModalWindow: NSWindow.StyleMask](./stylemask-swift.struct/docmodalwindow.md)
  The window is a document-modal panel (or  a subclass of [`NSPanel`](../nspanel.md)).
- [static var nonactivatingPanel: NSWindow.StyleMask](./stylemask-swift.struct/nonactivatingpanel.md)
  The window is a panel or a subclass of [`NSPanel`](../nspanel.md) that does not activate the owning app.
- [static var hudWindow: NSWindow.StyleMask](./stylemask-swift.struct/hudwindow.md)
  The window is a HUD panel.
### Style Mask Creation
- [init(rawValue: UInt)](./stylemask-swift.struct/init%28rawvalue%29.md)
  Creates a style mask using the given raw value.
### Deprecated
- [Deprecated symbols](../stylemask-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring the Window’s Appearance
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [func toggleFullScreen(Any?)](./togglefullscreen%28_%29.md)
  Takes the window into or out of fullscreen mode,
- [var worksWhenModal: Bool](./workswhenmodal.md)
  A Boolean value that indicates whether the window is able to receive keyboard and mouse events even when some other window is being run modally.
- [var alphaValue: CGFloat](./alphavalue.md)
  The window’s alpha value.
- [var backgroundColor: NSColor!](./backgroundcolor.md)
  The color of the window’s background.
- [var colorSpace: NSColorSpace?](./colorspace.md)
  The window’s color space.
- [func setDynamicDepthLimit(Bool)](./setdynamicdepthlimit%28_%29.md)
  Sets a Boolean value that indicates whether the window’s depth limit can change to match the depth of the screen it’s on.
- [var canHide: Bool](./canhide.md)
  A Boolean value that indicates whether the window can hide when its application becomes hidden.
- [var isOnActiveSpace: Bool](./isonactivespace.md)
  A Boolean value that indicates whether the window is on the currently active space.
- [var hidesOnDeactivate: Bool](./hidesondeactivate.md)
  A Boolean value that indicates whether the window is removed from the screen when its application becomes inactive.
- [var collectionBehavior: NSWindow.CollectionBehavior](./collectionbehavior-swift.property.md)
  A value that identifies the window’s behavior in window collections.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates whether the window is opaque.
- [var hasShadow: Bool](./hasshadow.md)
  A Boolean value that indicates whether the window has a shadow.
- [func invalidateShadow()](./invalidateshadow%28%29.md)
  Invalidates the window shadow so that it is recomputed based on the current window shape.
- [func autorecalculatesContentBorderThickness(for: NSRectEdge) -> Bool](./autorecalculatescontentborderthickness%28for%29.md)
  Indicates whether the window calculates the thickness of a given border automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct)*