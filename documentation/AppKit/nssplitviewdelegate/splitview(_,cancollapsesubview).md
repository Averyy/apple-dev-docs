# splitView(_:canCollapseSubview:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Allows the delegate to determine whether the user can collapse and expand the specified subview.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func splitView(_ splitView: NSSplitView, canCollapseSubview subview: NSView) -> Bool
```

```objc
- (BOOL) splitView:(NSSplitView *) splitView canCollapseSubview:(NSView *) subview;
```

#### Return Value

[`true`](../../Swift/true.md) if `subview` collapses when the user drags a divider beyond the halfway mark between its minimum size and its edge; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The `subview` expands when the user drags the divider beyond the halfway mark between its minimum size and its edge.

To specify the minimum size, define the methods [`splitView(_:constrainMaxCoordinate:ofSubviewAt:)`](./splitview%28_,constrainmaxcoordinate,ofsubviewat%29.md) and [`splitView(_:constrainMinCoordinate:ofSubviewAt:)`](./splitview%28_,constrainmincoordinate,ofsubviewat%29.md). A subview can collapse only if you also define [`splitView(_:constrainMinCoordinate:ofSubviewAt:)`](./splitview%28_,constrainmincoordinate,ofsubviewat%29.md).

A collapsed subview isn’t visible, but the split view object retains it with the same size as before the collapse.

If the delegate doesn’t implement this method, the subviews can’t collapse.

## Parameters

- `splitView`: The split view that sends the message.
- `subview`: The subview to collapse.

## See Also

### Managing Subviews
- [func splitViewWillResizeSubviews(Notification)](./splitviewwillresizesubviews%28_%29.md)
  Notifies the delegate when the split view is about to resize its subviews.
- [func splitViewDidResizeSubviews(Notification)](./splitviewdidresizesubviews%28_%29.md)
  Notifies the delegate when the split view resizes its subviews.
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](./splitview%28_,shouldcollapsesubview,fordoubleclickondividerat%29.md)
  Allows a delegate to determine if a subview collapses in response to a double click.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewdelegate/splitview(_:cancollapsesubview:))*