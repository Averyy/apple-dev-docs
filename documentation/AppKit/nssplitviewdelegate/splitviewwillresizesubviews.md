# splitViewWillResizeSubviews(_:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate when the split view is about to resize its subviews.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func splitViewWillResizeSubviews(_ notification: Notification)
```

#### Discussion

If the delegate implements this method, the system automatically registers it to receive this notification.

The default notification center invokes this method before the split view resizes two of its subviews in response to the repositioning of a divider.

## Parameters

- `notification`: A notification named  , which posts before a change to the size of some or all subviews of a split view.

## See Also

- [func splitViewDidResizeSubviews(Notification)](nssplitviewdelegate/splitviewdidresizesubviews(_:).md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](nssplitviewdelegate/splitview(_:cancollapsesubview:).md)
  Allows the delegate to determine whether the user can collapse and expand the specified subview.
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](nssplitviewdelegate/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:).md)
  Allows a delegate to determine if a subview collapses in response to a double click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitviewwillresizesubviews(_:))*