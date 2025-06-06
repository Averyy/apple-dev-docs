# editColumn(_:row:with:select:)

**Framework**: AppKit  
**Kind**: method

Edits the cell at the specified column and row using the specified event and selection behavior.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func editColumn(_ column: Int, row: Int, with event: NSEvent?, select: Bool)
```

#### Discussion

This method is invoked automatically in response to user actions; you should rarely need to invoke it directly. `theEvent` is usually the mouse event that triggered editing; it can be `nil` when starting an edit programmatically.

This method scrolls the table view so that the cell is visible and sets up the field editor. If `flag` is [`false`](https://developer.apple.com/documentation/swift/false), it calls the  [`edit(withFrame:in:editor:delegate:event:)`](nscell/edit(withframe:in:editor:delegate:event:).md) method of the field editor’s [`NSCell`](nscell.md) object, providing the `NSTableView` as the text delegate. If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), this method calls the [`select(withFrame:in:editor:delegate:start:length:)`](nscell/select(withframe:in:editor:delegate:start:length:).md) method instead.

This method can be overridden to customize drawing for `rowIndex` when using [`NSCell`](nscell.md)-based table views.

> **Note**:  When using [`NSView`](nsview.md)-based table views, this method attempts to make the view at the specified `column` and `row` the first responder, which will begin editing if the view supports editing. This method should not be subclassed or overridden for [`NSView`](nsview.md)-based table views. Instead, row drawing customization can be done by subclassing [`NSTableRowView`](nstablerowview.md).

 When using [`NSView`](nsview.md)-based table views, this method attempts to make the view at the specified `column` and `row` the first responder, which will begin editing if the view supports editing. This method should not be subclassed or overridden for [`NSView`](nsview.md)-based table views. Instead, row drawing customization can be done by subclassing [`NSTableRowView`](nstablerowview.md).

## Parameters

- `column`: The index of the column in the   array.
- `row`: The row index.
- `event`: The event.
- `select`:   if the entered contents should be selected, otherwise  .

## See Also

- [var editedColumn: Int](nstableview/editedcolumn.md)
  The index of the column being edited.
- [var editedRow: Int](nstableview/editedrow.md)
  The index of the row being edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/editcolumn(_:row:with:select:))*