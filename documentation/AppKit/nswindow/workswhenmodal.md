# worksWhenModal

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is able to receive keyboard and mouse events even when some other window is being run modally.

**Availability**:
- macOS

## Declaration

```swift
var worksWhenModal: Bool { get }
```

```objc
@property (readonly) BOOL worksWhenModal;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window is able to receive keyboard and mouse events even when some other window is being run modally; otherwise, [`false`](../../Swift/false.md). By default, the `NSWindow` value of this property is [`false`](../../Swift/false.md). Only subclasses of `NSPanel` should override this default.

## See Also

### Related Documentation
- [var worksWhenModal: Bool](../nspanel/workswhenmodal.md)
  A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.
### Configuring the Window’s Appearance
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [NSWindow.StyleMask](./stylemask-swift.struct.md)
  Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.
- [func toggleFullScreen(Any?)](./togglefullscreen%28_%29.md)
  Takes the window into or out of fullscreen mode,
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/workswhenmodal)*