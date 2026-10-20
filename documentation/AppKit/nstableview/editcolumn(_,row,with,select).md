# editColumn(_:row:with:select:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Edits the cell at the specified column and row using the specified event and selection behavior.

**Availability**:
- macOS

## Declaration

```swift
func editColumn(_ column: Int, row: Int, with event: NSEvent?, select: Bool)
```

```objc
- (void) editColumn:(NSInteger) column row:(NSInteger) row withEvent:(NSEvent *) event select:(BOOL) select;
```

#### Discussion

This method is invoked automatically in response to user actions; you should rarely need to invoke it directly. `theEvent` is usually the mouse event that triggered editing; it can be `nil` when starting an edit programmatically.

This method scrolls the table view so that the cell is visible and sets up the field editor. If `flag` is [`false`](../../Swift/false.md), it calls the  [`edit(withFrame:in:editor:delegate:event:)`](../nscell/edit%28withframe,in,editor,delegate,event%29.md) method of the field editor’s [`NSCell`](../nscell.md) object, providing the `NSTableView` as the text delegate. If `flag` is [`true`](../../Swift/true.md), this method calls the [`select(withFrame:in:editor:delegate:start:length:)`](../nscell/select%28withframe,in,editor,delegate,start,length%29.md) method instead.

This method can be overridden to customize drawing for `rowIndex` when using [`NSCell`](../nscell.md)-based table views.

> **Note**:  When using [`NSView`](../nsview.md)-based table views, this method attempts to make the view at the specified `column` and `row` the first responder, which will begin editing if the view supports editing. This method should not be subclassed or overridden for [`NSView`](../nsview.md)-based table views. Instead, row drawing customization can be done by subclassing [`NSTableRowView`](../nstablerowview.md).

## Parameters

- `column`: The index of the column in the [`tableColumns`](./tablecolumns.md) array.
- `row`: The row index.
- `event`: The event.
- `select`: [`true`](../../Swift/true.md) if the entered contents should be selected, otherwise [`false`](../../Swift/false.md).

## See Also

### Editing Cells
- [var editedColumn: Int](./editedcolumn.md)
  The index of the column being edited.
- [var editedRow: Int](./editedrow.md)
  The index of the row being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/editcolumn(_:row:with:select:))*