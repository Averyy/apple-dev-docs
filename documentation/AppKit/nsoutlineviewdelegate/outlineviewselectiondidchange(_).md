# outlineViewSelectionDidChange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func outlineViewSelectionDidChange(_ notification: Notification)
```

```objc
- (void) outlineViewSelectionDidChange:(NSNotification *) notification;
```

## Discussion

This method is invoked as a result of posting an [`selectionDidChangeNotification`](../nsoutlineview/selectiondidchangenotification.md).

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
- [func outlineViewSelectionIsChanging(Notification)](./outlineviewselectionischanging%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineviewselectiondidchange(_:))*