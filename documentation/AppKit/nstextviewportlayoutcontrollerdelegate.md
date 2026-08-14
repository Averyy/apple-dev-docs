# NSTextViewportLayoutControllerDelegate

**Framework**: AppKit  
**Kind**: protocol

Optional methods that delegates implement to respond to viewport layout changes.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol NSTextViewportLayoutControllerDelegate : NSObjectProtocol
```

## Topics

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:).md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:).md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](nstextviewportlayoutcontrollerdelegate/viewportbounds(for:).md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.
### Instance Methods
- [func textViewportLayoutController(NSTextViewportLayoutController, cacheRenderingSurface: any NSTextViewportRenderingSurface, for: any NSTextViewportRenderingSurfaceKey)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:).md)
  Asks the delegate to cache a rendering surface for later retrieval.
- [func textViewportLayoutController(NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:).md)
  Asks the delegate to return a previously cached rendering surface.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerreceivedsetneedslayout(_:).md)
  Triggers relayout of the view.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
### Conforming Types
- [NSTextView](nstextview.md)

## See Also

- [var delegate: (any NSTextViewportLayoutControllerDelegate)?](nstextviewportlayoutcontroller/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate)*