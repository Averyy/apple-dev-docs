# splitView(_:shouldAdjustSizeOfSubview:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to specify whether to resize the subview.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, shouldAdjustSizeOfSubview view: NSView) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView shouldAdjustSizeOfSubview:(NSView *) view;
```

#### Return Value

If [`adjustSubviews()`](../nssplitview/adjustsubviews%28%29.md) can change the size of the subview, [`true`](../../Swift/true.md); otherwise, [`false`](../../Swift/false.md). By returning [`false`](../../Swift/false.md), you lock the size of the split view `subview` while the split view resizes.

#### Discussion

> ❗ **Important**:  If your split view uses Auto Layout to size its subviews, don’t implement this method.

Regardless of the value that this method returns, [`adjustSubviews()`](../nssplitview/adjustsubviews%28%29.md) may change the origin of the subview. Nonresizable subviews may resize to prevent an invalid subview layout.

If a split view has no delegate, or if its delegate doesn’t respond to this message, the split view behaves as if this method returns [`true`](../../Swift/true.md).

## Parameters

- `splitView`: The split view that sends the message.
- `view`: The subview to resize.

## See Also

### Adjusting Subviews Manually
- [func splitView(NSSplitView, constrainMinCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](./splitview%28_,constrainmincoordinate,ofsubviewat%29.md)
  Allows the delegate to constrain the minimum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, constrainMaxCoordinate: CGFloat, ofSubviewAt: Int) -> CGFloat](./splitview%28_,constrainmaxcoordinate,ofsubviewat%29.md)
  Allows the delegate to constrain the maximum coordinate limit of a divider when the user drags it.
- [func splitView(NSSplitView, resizeSubviewsWithOldSize: NSSize)](./splitview%28_,resizesubviewswitholdsize%29.md)
  Allows the delegate to specify custom sizing behavior for the subviews of the split view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:shouldadjustsizeofsubview:))*