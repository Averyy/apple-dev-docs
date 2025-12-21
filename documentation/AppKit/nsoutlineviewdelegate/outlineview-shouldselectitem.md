# outlineView(_:shouldSelectItem:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the outline view should select a given item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldSelectItem item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit `outlineView` to select `item`, [`false`](https://developer.apple.com/documentation/Swift/false) to deny permission.

#### Discussion

You implement this method to disallow selection of particular items.

For better performance and finer grain control over the selection, use [`outlineView(_:selectionIndexesForProposedSelection:)`](nsoutlineviewdelegate/outlineview(_:selectionindexesforproposedselection:).md).

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item.

## See Also

- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldselect:).md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](nsoutlineviewdelegate/outlineview(_:selectionindexesforproposedselection:).md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](nsoutlineviewdelegate/selectionshouldchange(in:).md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionIsChanging(Notification)](nsoutlineviewdelegate/outlineviewselectionischanging(_:).md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](nsoutlineviewdelegate/outlineviewselectiondidchange(_:).md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldselectitem:))*