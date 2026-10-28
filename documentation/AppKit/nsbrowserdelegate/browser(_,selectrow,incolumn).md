# browser(_:selectRow:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to select the cell at the specified row and column location.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, selectRow row: Int, inColumn column: Int) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) sender selectRow:(NSInteger) row inColumn:(NSInteger) column;
```

## Return Value

[`true`](../../Swift/true.md) if the cell was selected; otherwise, [`false`](../../Swift/false.md).

## Discussion

Invoked in response to [`selectRow(_:inColumn:)`](../nsbrowser/selectrow%28_,incolumn%29.md) of [`NSBrowser`](../nsbrowser.md) being received by `sender`.

## Parameters

- `sender`: The browser.
- `row`: The index of the row containing the cell to select.
- `column`: The index of the column containing the cell to select.

## See Also

### Related Documentation
- [func selectRow(Int, inColumn: Int)](../nsbrowser/selectrow%28_,incolumn%29.md)
  Selects the cell at the specified row and column index.
- [func selectedRow(inColumn: Int) -> Int](../nsbrowser/selectedrow%28incolumn%29.md)
  Returns the row index of the selected cell in the specified column.
### Managing Selection
- [func browser(NSBrowser, selectCellWith: String, inColumn: Int) -> Bool](./browser%28_,selectcellwith,incolumn%29.md)
  Asks the delegate to select the cell with the given title in the specified column.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](./browser%28_,selectionindexesforproposedselection,incolumn%29.md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:selectrow:incolumn:))*