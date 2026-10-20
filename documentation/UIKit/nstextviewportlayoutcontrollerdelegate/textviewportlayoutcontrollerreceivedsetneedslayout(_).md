# textViewportLayoutControllerReceivedSetNeedsLayout(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Triggers relayout of the view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textViewportLayoutControllerReceivedSetNeedsLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

```objc
- (void) textViewportLayoutControllerReceivedSetNeedsLayout:(NSTextViewportLayoutController *) textViewportLayoutController;
```

## Parameters

- `textViewportLayoutController`: The viewport layout controller requesting a relayout.

## See Also

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](./textviewportlayoutcontroller%28_,configurerenderingsurfacefor%29.md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerdidlayout%28_%29.md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerwilllayout%28_%29.md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./viewportbounds%28for%29.md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerreceivedsetneedslayout(_:))*