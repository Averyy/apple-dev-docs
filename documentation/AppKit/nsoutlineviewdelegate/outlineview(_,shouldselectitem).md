# outlineView(_:shouldSelectItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the outline view should select a given item.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldSelectItem item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldSelectItem:(id) item;
```

#### Return Value

[`true`](../../Swift/true.md) to permit `outlineView` to select `item`, [`false`](../../Swift/false.md) to deny permission.

#### Discussion

You implement this method to disallow selection of particular items.

For better performance and finer grain control over the selection, use [`outlineView(_:selectionIndexesForProposedSelection:)`](./outlineview%28_,selectionindexesforproposedselection%29.md).

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: The item.

## See Also

### Handling Selection
- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](./outlineview%28_,shouldselect%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](./outlineview%28_,selectionindexesforproposedselection%29.md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](./selectionshouldchange%28in%29.md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionIsChanging(Notification)](./outlineviewselectionischanging%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](./outlineviewselectiondidchange%28_%29.md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldselectitem:))*