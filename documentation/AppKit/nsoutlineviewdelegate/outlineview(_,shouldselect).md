# outlineView(_:shouldSelect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the outline view should select a given table column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldSelect tableColumn: NSTableColumn?) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldSelectTableColumn:(NSTableColumn *) tableColumn;
```

#### Return Value

[`true`](../../Swift/true.md) to permit `outlineView` to select `tableColumn`, [`false`](../../Swift/false.md) to deny permission.

#### Discussion

The delegate can implement this method to disallow selection of specific columns.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

### Handling Selection
- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](./outlineview%28_,shouldselectitem%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](./outlineview%28_,selectionindexesforproposedselection%29.md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](./selectionshouldchange%28in%29.md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionIsChanging(Notification)](./outlineviewselectionischanging%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](./outlineviewselectiondidchange%28_%29.md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldselect:))*