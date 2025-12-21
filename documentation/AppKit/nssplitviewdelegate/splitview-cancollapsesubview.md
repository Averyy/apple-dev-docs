# splitView(_:canCollapseSubview:)

**Framework**: AppKit  
**Kind**: method

Allows the delegate to determine whether the user can collapse and expand the specified subview.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, canCollapseSubview subview: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `subview` collapses when the user drags a divider beyond the halfway mark between its minimum size and its edge; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The `subview` expands when the user drags the divider beyond the halfway mark between its minimum size and its edge.

To specify the minimum size, define the methods [`splitView(_:constrainMaxCoordinate:ofSubviewAt:)`](nssplitviewdelegate/splitview(_:constrainmaxcoordinate:ofsubviewat:).md) and [`splitView(_:constrainMinCoordinate:ofSubviewAt:)`](nssplitviewdelegate/splitview(_:constrainmincoordinate:ofsubviewat:).md). A subview can collapse only if you also define [`splitView(_:constrainMinCoordinate:ofSubviewAt:)`](nssplitviewdelegate/splitview(_:constrainmincoordinate:ofsubviewat:).md).

A collapsed subview isn’t visible, but the split view object retains it with the same size as before the collapse.

If the delegate doesn’t implement this method, the subviews can’t collapse.

## Parameters

- `splitView`: The split view that sends the message.
- `subview`: The subview to collapse.

## See Also

- [func splitViewWillResizeSubviews(Notification)](nssplitviewdelegate/splitviewwillresizesubviews(_:).md)
  Notifies the delegate when the split view is about to resize its subviews.
- [func splitViewDidResizeSubviews(Notification)](nssplitviewdelegate/splitviewdidresizesubviews(_:).md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](nssplitviewdelegate/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:).md)
  Allows a delegate to determine if a subview collapses in response to a double click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:cancollapsesubview:))*