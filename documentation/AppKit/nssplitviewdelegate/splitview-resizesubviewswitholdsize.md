# splitView(_:resizeSubviewsWithOldSize:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to specify custom sizing behavior for the subviews of the split view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, resizeSubviewsWithOldSize oldSize: NSSize)
```

#### Discussion

> ❗ **Important**:  If your split view uses Auto Layout to size its subviews, don’t implement this method.

If the delegate implements this method, it receives this message after the split view resizes.

Resize the subviews so that the sum of the sizes of the subviews plus the sum of the thickness of the dividers equals the size of the new frame of the [`NSSplitView`](nssplitview.md). You can get the thickness of a divider through the [`dividerThickness`](nssplitview/dividerthickness.md) method.

If you implement this delegate method to resize subviews on your own, the [`NSSplitView`](nssplitview.md) doesn’t perform any error checking for you. However, you can invoke [`adjustSubviews()`](nssplitview/adjustsubviews().md) to perform the default sizing behavior.

## Parameters

- `splitView`: The split view that sends the message.
- `oldSize`: The size of the split view before the user resizes it.

## See Also

- [func splitView(NSSplitView, constrainMinCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](nssplitviewdelegate/splitview(_:constrainmincoordinate:ofsubviewat:).md)
  Allows the delegate to constrain the minimum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, constrainMaxCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](nssplitviewdelegate/splitview(_:constrainmaxcoordinate:ofsubviewat:).md)
  Allows the delegate to constrain the maximum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, shouldAdjustSizeOfSubview: NSView) -> Bool](nssplitviewdelegate/splitview(_:shouldadjustsizeofsubview:).md)
  Allows the delegate to specify whether to resize the subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:resizesubviewswitholdsize:))*