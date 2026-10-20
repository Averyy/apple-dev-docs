# textViewportLayoutControllerWillLayout(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The method the framework calls before the text viewport layout controller starts its layout process.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textViewportLayoutControllerWillLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

```objc
- (void) textViewportLayoutControllerWillLayout:(NSTextViewportLayoutController *) textViewportLayoutController;
```

## Parameters

- `textViewportLayoutController`: The [`NSTextViewportLayoutController`](../nstextviewportlayoutcontroller.md).

## See Also

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](./textviewportlayoutcontroller%28_,configurerenderingsurfacefor%29.md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerdidlayout%28_%29.md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./viewportbounds%28for%29.md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:))*