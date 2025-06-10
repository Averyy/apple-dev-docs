# viewportBounds(for:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the current viewport, which is the view visible bounds plus the overdraw area.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func viewportBounds(for textViewportLayoutController: NSTextViewportLayoutController) -> CGRect
```

#### Return Value

A [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect).

## Parameters

- `textViewportLayoutController`: The  .

## See Also

- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:).md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:).md)
  The method the framework calls before the text viewport layout controller starts its layout process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/viewportbounds(for:))*