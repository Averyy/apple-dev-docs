# textViewportLayoutController(_:configureRenderingSurfaceFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The method the framework calls when the layout controller lays out a text layout fragment in the UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment)
```

```objc
- (void) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController configureRenderingSurfaceForTextLayoutFragment:(NSTextLayoutFragment *) textLayoutFragment;
```

## Discussion

The delegate presents the text layout fragment in the UI, for example, in a sublayer or a subview. Layout information such as `viewportBounds` on `textViewportLayoutController` isn’t up to date at the point of this call.

## Parameters

- `textViewportLayoutController`: The `NSTextViewportLayoutController` associated with this text layout fragment.
- `textLayoutFragment`: An `NSTextLayoutFragment`.

## See Also

### Responding to changes in the viewport
- [func textViewportLayoutControllerDidLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerdidlayout%28_%29.md)
  The method the framework calls when the text viewport layout controller finishes its layout process.
- [func textViewportLayoutControllerWillLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerwilllayout%28_%29.md)
  The method the framework calls before the text viewport layout controller starts its layout process.
- [func textViewportLayoutControllerReceivedSetNeedsLayout(NSTextViewportLayoutController)](./textviewportlayoutcontrollerreceivedsetneedslayout%28_%29.md)
  Triggers relayout of the view.
- [func viewportBounds(for: NSTextViewportLayoutController) -> CGRect](./viewportbounds%28for%29.md)
  Returns the current viewport, which is the view visible bounds plus the overdraw area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:))*