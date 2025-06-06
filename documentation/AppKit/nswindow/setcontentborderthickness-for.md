# setContentBorderThickness(_:for:)

**Framework**: AppKit  
**Kind**: method

Specifies the thickness of a given border of the window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setContentBorderThickness(_ thickness: CGFloat, for edge: NSRectEdge)
```

#### Discussion

In a nontextured window calling `setContentBorderThickness:forEdge:` passing `NSMaxYEdge` will raise an exception (in a nontextured window, it’s only valid to set the content border thickness of the bottom edge). It is only valid to set the content border thickness of the top edge in a textured window.

Typically, if you call `setContentBorderThickness:forEdge:`, you should also call `setAutorecalculatesContentBorderThickness:NO forEdge:`.

The `contentBorder` does not include the title bar or toolbar, so a textured window that just wants the gradient in the title bar and toolbar should have a `thickness` of `0` for `NSMaxYEdge`.

## Parameters

- `thickness`: The thickness for  , in points.
- `edge`: The border whose thickness to set:

## See Also

- [var styleMask: NSWindow.StyleMask](nswindow/stylemask-swift.property.md)
  Flags that describe the window’s current style, such as if it’s resizable or in full-screen mode.
- [NSWindow.StyleMask](nswindow/stylemask-swift.struct.md)
  Constants that specify the style of a window, and that you can combine with the C bitwise OR operator.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setcontentborderthickness(_:for:))*