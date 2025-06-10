# textViewportLayoutControllerDidLayout(_:)

**Framework**: AppKit  
**Kind**: method

The method the framework calls when the text viewport layout controller finishes its layout process.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func textViewportLayoutControllerDidLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

#### Discussion

Layout information on `textViewportLayoutController` is up-to-date at the point of this call.

## Parameters

- `textViewportLayoutController`: The  .

## See Also

- [func textViewportLayoutController(NSTextViewportLayoutController, configureRenderingSurfaceFor: NSTextLayoutFragment)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:).md)
  The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:).md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](nstextviewportlayoutcontrollerdelegate/viewportbounds(for:).md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:))*