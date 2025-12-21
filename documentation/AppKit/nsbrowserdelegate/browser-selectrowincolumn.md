# browser(_:selectRow:inColumn:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to select the cell at the specified row and column location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, selectRow row: Int, inColumn column: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the cell was selected; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Invoked in response to [`selectRow(_:inColumn:)`](nsbrowser/selectrow(_:incolumn:).md) of [`NSBrowser`](nsbrowser.md) being received by `sender`.

## Parameters

- `sender`: The browser.
- `row`: The index of the row containing the cell to select.
- `column`: The index of the column containing the cell to select.

## See Also

- [func selectRow(Int, inColumn: Int)](nsbrowser/selectrow(_:incolumn:).md)
  Selects the cell at the specified row and column index.
- [func selectedRow(inColumn: Int) -> Int](nsbrowser/selectedrow(incolumn:).md)
  Returns the row index of the selected cell in the specified column.
- [func browser(NSBrowser, selectCellWith: String, inColumn: Int) -> Bool](nsbrowserdelegate/browser(_:selectcellwith:incolumn:).md)
  Asks the delegate to select the cell with the given title in the specified column.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](nsbrowserdelegate/browser(_:selectionindexesforproposedselection:incolumn:).md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:selectrow:incolumn:))*