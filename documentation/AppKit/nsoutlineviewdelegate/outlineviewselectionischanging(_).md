# outlineViewSelectionIsChanging(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func outlineViewSelectionIsChanging(_ notification: Notification)
```

```objc
- (void) outlineViewSelectionIsChanging:(NSNotification *) notification;
```

## Discussion

This method is invoked as a result of posting an [`selectionIsChangingNotification`](../nsoutlineview/selectionischangingnotification.md).

## Parameters

- `notification`: The posted notification.

## See Also

### Handling Selection
- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](./outlineview%28_,shouldselect%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](./outlineview%28_,shouldselectitem%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](./outlineview%28_,selectionindexesforproposedselection%29.md)
  Invoked to allow the delegate to modify the proposed selection.
- [func selectionShouldChange(in: NSOutlineView) -> Bool](./selectionshouldchange%28in%29.md)
  Returns a Boolean value that indicates whether the outline view should change its selection.
- [func outlineViewSelectionDidChange(Notification)](./outlineviewselectiondidchange%28_%29.md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineviewselectionischanging(_:))*