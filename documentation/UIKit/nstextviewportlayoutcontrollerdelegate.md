# NSTextViewportLayoutControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSTextViewportLayoutControllerDelegate <NSObject>
```

## Mentions

- [Managing viewport layout and attachment reuse in text views](./managing-viewport-layout-and-attachment-reuse-in-a-text-view-subclass.md)

## Topics

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_,configurerenderingsurfacefor%29.md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout%28_%29.md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout%28_%29.md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerreceivedsetneedslayout%28_%29.md)
  Triggers relayout of the view.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./nstextviewportlayoutcontrollerdelegate/viewportbounds%28for%29.md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.
### Storing rendering surfaces
- [func textViewportLayoutController(NSTextViewportLayoutController, cacheRenderingSurface: any NSTextViewportRenderingSurface, for: any NSTextViewportRenderingSurfaceKey)](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_,cacherenderingsurface,for%29.md)
  Asks the delegate to cache a rendering surface for later retrieval.
- [func textViewportLayoutController(NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_,retrievecachedrenderingsurfacefor%29.md)
  Asks the delegate to return a previously cached rendering surface.
### Instance Methods
- [- textViewportLayoutController:renderingSurfaceForTextLayoutFragment:](./nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller_renderingsurfacefortextlayoutfragment_.md)
  Returns a rendering surface for the specified text layout fragment.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UITextView](./uitextview.md)

## See Also

### Responding to changes in viewport layout
- [var delegate: (any NSTextViewportLayoutControllerDelegate)?](./nstextviewportlayoutcontroller/delegate.md)
  The delegate for the text layout manager object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate)*