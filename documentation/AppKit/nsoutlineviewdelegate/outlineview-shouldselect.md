# outlineView(_:shouldSelect:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the outline view should select a given table column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldSelect tableColumn: NSTableColumn?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to permit `outlineView` to select `tableColumn`, [`false`](https://developer.apple.com/documentation/Swift/false) to deny permission.

#### Discussion

The delegate can implement this method to disallow selection of specific columns.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldselectitem:).md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](nsoutlineviewdelegate/outlineview(_:selectionindexesforproposedselection:).md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](nsoutlineviewdelegate/selectionshouldchange(in:).md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionIsChanging(Notification)](nsoutlineviewdelegate/outlineviewselectionischanging(_:).md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](nsoutlineviewdelegate/outlineviewselectiondidchange(_:).md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldselect:))*