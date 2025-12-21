# splitView(_:shouldCollapseSubview:forDoubleClickOnDividerAt:)

**Framework**: AppKit  
**Kind**: method

Allows a delegate to determine if a subview collapses in response to a double click.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func splitView(_ splitView: NSSplitView, shouldCollapseSubview subview: NSView, forDoubleClickOnDividerAt dividerIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the subview should collapse; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the delegate implements this method, it receives this message once for the subview before a divider when the user double-clicks that divider, and again for the subview after the divider, but only if the delegate returns [`true`](https://developer.apple.com/documentation/Swift/true) when it receives [`splitView(_:canCollapseSubview:)`](nssplitviewdelegate/splitview(_:cancollapsesubview:).md) for the subview in question. When the delegate indicates that both subviews should collapse, the behavior of [`NSSplitView`](nssplitview.md) is undefined.

## Parameters

- `splitView`: The split view that sends the message.
- `subview`: The subview to collapse.
- `dividerIndex`: The index of the divider.

## See Also

- [func splitViewWillResizeSubviews(Notification)](nssplitviewdelegate/splitviewwillresizesubviews(_:).md)
  Notifies the delegate when the split view is about to resize its subviews.
- [func splitViewDidResizeSubviews(Notification)](nssplitviewdelegate/splitviewdidresizesubviews(_:).md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](nssplitviewdelegate/splitview(_:cancollapsesubview:).md)
  Allows the delegate to determine whether the user can collapse and expand the specified subview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:))*