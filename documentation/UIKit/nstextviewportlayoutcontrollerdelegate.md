# NSTextViewportLayoutControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

Optional methods that delegates implement to respond to viewport layout changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSTextViewportLayoutControllerDelegate : NSObjectProtocol
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## Topics

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:).md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:).md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerreceivedsetneedslayout(_:).md)
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](nstextviewportlayoutcontrollerdelegate/viewportbounds(for:).md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.
### Storing rendering surfaces
- [func textViewportLayoutController(NSTextViewportLayoutController, cacheRenderingSurface: any NSTextViewportRenderingSurface, for: any NSTextViewportRenderingSurfaceKey)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:).md)
- [func textViewportLayoutController(NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITextView](uitextview.md)

## See Also

- [var delegate: (any NSTextViewportLayoutControllerDelegate)?](nstextviewportlayoutcontroller/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate)*