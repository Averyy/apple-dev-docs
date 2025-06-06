# outlineViewSelectionIsChanging(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func outlineViewSelectionIsChanging(_ notification: Notification)
```

#### Discussion

This method is invoked as a result of posting an [`selectionIsChangingNotification`](nsoutlineview/selectionischangingnotification.md).

## Parameters

- `notification`: The posted notification.

## See Also

- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldselect:).md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldselectitem:).md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](nsoutlineviewdelegate/outlineview(_:selectionindexesforproposedselection:).md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](nsoutlineviewdelegate/selectionshouldchange(in:).md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionDidChange(Notification)](nsoutlineviewdelegate/outlineviewselectiondidchange(_:).md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineviewselectionischanging(_:))*