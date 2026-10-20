# outlineView(_:selectionIndexesForProposedSelection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to modify the proposed selection.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, selectionIndexesForProposedSelection proposedSelectionIndexes: IndexSet) -> IndexSet
```

```objc
- (NSIndexSet *) outlineView:(NSOutlineView *) outlineView selectionIndexesForProposedSelection:(NSIndexSet *) proposedSelectionIndexes;
```

#### Return Value

An [`NSIndexSet`](../../Foundation/nsindexset.md) instance containing the indexes of the new selection. Return `proposedSelectionIndexes` if the proposed selection is acceptable, or the value of the table view’s existing selection to avoid changing the selection.

#### Discussion

This method may be called multiple times with one new index added to the existing selection to find out if a particular index can be selected when the user is extending the selection with the keyboard or mouse.

Implementation of this method is optional. If implemented, this method will be called instead of [`outlineView(_:shouldSelectItem:)`](./outlineview%28_,shouldselectitem%29.md).

## Parameters

- `outlineView`: The outline view that sent the message.
- `proposedSelectionIndexes`: An index set containing the indexes of the proposed selection.

## See Also

### Handling Selection
- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](./outlineview%28_,shouldselect%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](./outlineview%28_,shouldselectitem%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](./selectionshouldchange%28in%29.md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionIsChanging(Notification)](./outlineviewselectionischanging%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](./outlineviewselectiondidchange%28_%29.md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:selectionindexesforproposedselection:))*