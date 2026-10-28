# setAutorecalculatesContentBorderThickness(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies whether the window calculates the thickness of a given border automatically.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setAutorecalculatesContentBorderThickness(_ flag: Bool, for edge: NSRectEdge)
```

```objc
- (void) setAutorecalculatesContentBorderThickness:(BOOL) flag forEdge:(NSRectEdge) edge;
```

## Discussion

Turning off a border’s auto-recalculation status sets its border thickness to `0.0`.

In a nontextured window calling `setAutorecalculatesContentBorderThickness:forEdge:` passing `NSMaxYEdge` will raise an exception (in a nontextured window, it’s only valid to set the content border thickness of the bottom edge). It is only valid to set the content border thickness of the top edge in a textured window.

Typically, if you call `setContentBorderThickness:forEdge:`, you should also call `setAutorecalculatesContentBorderThickness:NO forEdge:`.

## Parameters

- `flag`: If [`true`](../../Swift/true.md), the window calculates the thickness of the edge automatically; if [`false`](../../Swift/false.md), it does not.
- `edge`: The border to set auto-recalculation on or off:

  - `NSMaxYEdge`: Top border.
  - `NSMinYEdge`: Bottom border.

## See Also

### Configuring the Window’s Appearance
- [var styleMask: NSWindow.StyleMask](./stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [NSWindow.StyleMask](./stylemask-swift.struct.md)
  Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setautorecalculatescontentborderthickness(_:for:))*