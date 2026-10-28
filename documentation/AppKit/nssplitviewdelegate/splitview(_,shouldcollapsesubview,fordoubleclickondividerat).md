# splitView(_:shouldCollapseSubview:forDoubleClickOnDividerAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows a delegate to determine if a subview collapses in response to a double click.

**Availability**:
- macOS 10.5+ - Deprecated in 10.15

> **Deprecated**: NSSplitView no longer supports collapsing sections via double-click. This delegate method is never called.

## Declaration

```swift
optional func splitView(_ splitView: NSSplitView, shouldCollapseSubview subview: NSView, forDoubleClickOnDividerAt dividerIndex: Int) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView shouldCollapseSubview:(NSView *) subview forDoubleClickOnDividerAtIndex:(NSInteger) dividerIndex;
```

## Return Value

[`true`](../../Swift/true.md) if the subview should collapse; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the delegate implements this method, it receives this message once for the subview before a divider when the user double-clicks that divider, and again for the subview after the divider, but only if the delegate returns [`true`](../../Swift/true.md) when it receives [`splitView(_:canCollapseSubview:)`](./splitview%28_,cancollapsesubview%29.md) for the subview in question. When the delegate indicates that both subviews should collapse, the behavior of [`NSSplitView`](../nssplitview.md) is undefined.

## Parameters

- `splitView`: The split view that sends the message.
- `subview`: The subview to collapse.
- `dividerIndex`: The index of the divider.

## See Also

### Managing Subviews
- [func splitViewWillResizeSubviews(Notification)](./splitviewwillresizesubviews%28_%29.md)
  Notifies the delegate when the split view is about to resize its subviews.
- [func splitViewDidResizeSubviews(Notification)](./splitviewdidresizesubviews%28_%29.md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](./splitview%28_,cancollapsesubview%29.md)
  Allows the delegate to determine whether the user can collapse and expand the specified subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:))*