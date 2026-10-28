# appearanceSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object that the window inherits its appearance from.

**Availability**:
- macOS 10.14+

## Declaration

```swift
weak var appearanceSource: (any NSAppearanceCustomization)! { get set }
```

```objc
@property (weak, null_resettable) NSObject<NSAppearanceCustomization> * appearanceSource;
```

## Discussion

The default value of this property is [`NSApp`](../nsapp.md). The window uses key-value observing to monitor the source’s [`effectiveAppearance`](../nsappearancecustomization/effectiveappearance.md) for changes. Typically, you use this property for child windows shown from a parent window or specific view.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/appearancesource)*