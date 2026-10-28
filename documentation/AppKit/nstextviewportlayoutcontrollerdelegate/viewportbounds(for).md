# viewportBounds(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the current viewport, which is the view visible bounds plus the overdraw area.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func viewportBounds(for textViewportLayoutController: NSTextViewportLayoutController) -> CGRect
```

```objc
- (CGRect) viewportBoundsForTextViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController;
```

## Return Value

A [`CGRect`](../../CoreFoundation/cgrect.md).

## Parameters

- `textViewportLayoutController`: The [`NSTextViewportLayoutController`](../nstextviewportlayoutcontroller.md).

## See Also

### Responding to changes in the viewport
- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](./textviewportlayoutcontroller%28_,configurerenderingsurfacefor%29.md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerdidlayout%28_%29.md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerwilllayout%28_%29.md)
  The method the framework calls before the text viewport layout controller starts its layout process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/viewportbounds(for:))*