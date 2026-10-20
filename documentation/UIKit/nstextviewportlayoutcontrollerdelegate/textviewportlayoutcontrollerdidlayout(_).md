# textViewportLayoutControllerDidLayout(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

The method the framework calls when the text viewport layout controller finishes its layout process.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textViewportLayoutControllerDidLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

```objc
- (void) textViewportLayoutControllerDidLayout:(NSTextViewportLayoutController *) textViewportLayoutController;
```

#### Discussion

Layout information on `textViewportLayoutController` is up-to-date at the point of this call.

## Parameters

- `textViewportLayoutController`: The [`NSTextViewportLayoutController`](../nstextviewportlayoutcontroller.md).

## See Also

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](./textviewportlayoutcontroller%28_,configurerenderingsurfacefor%29.md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerwilllayout%28_%29.md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerreceivedsetneedslayout%28_%29.md)
  Triggers relayout of the view.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./viewportbounds%28for%29.md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:))*