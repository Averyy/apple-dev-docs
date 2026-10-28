# selectionShouldChange(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the outline view should change its selection.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func selectionShouldChange(in outlineView: NSOutlineView) -> Bool
```

```objc
- (BOOL) selectionShouldChangeInOutlineView:(NSOutlineView *) outlineView;
```

## Return Value

[`true`](../../Swift/true.md) to permit `outlineView` to change its selection (typically a row being edited), [`false`](../../Swift/false.md) to deny permission.

## Discussion

For example, if the user is editing a cell and enters an improper value, the delegate can prevent the user from selecting or editing any other cells until a proper value has been entered into the original cell. The delegate can implement this method for complex validation of edited rows based on the values of any of their cells.

## Parameters

- `outlineView`: The outline view that sent the message.

## See Also

### Handling Selection
- [func outlineView(NSOutlineView, shouldSelect: NSTableColumn?) -> Bool](./outlineview%28_,shouldselect%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given table column.
- [func outlineView(NSOutlineView, shouldSelectItem: Any) -> Bool](./outlineview%28_,shouldselectitem%29.md)
  Returns a Boolean value that indicates whether the outline view should select a given item.
- [func outlineView(NSOutlineView, selectionIndexesForProposedSelection: IndexSet) -> IndexSet](./outlineview%28_,selectionindexesforproposedselection%29.md)
  Invoked to allow the delegate to modify the proposed selection.
- [func outlineViewSelectionIsChanging(Notification)](./outlineviewselectionischanging%28_%29.md)
  Invoked when `notification` is posted—that is, whenever the outline view’s selection changes.
- [func outlineViewSelectionDidChange(Notification)](./outlineviewselectiondidchange%28_%29.md)
  Invoked when the selection did change notification is posted—that is, immediately after the outline view’s selection has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/selectionshouldchange(in:))*