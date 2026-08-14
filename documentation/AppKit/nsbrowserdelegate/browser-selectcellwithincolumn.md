# browser(_:selectCellWith:inColumn:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to select the cell with the given title in the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, selectCellWith title: String, inColumn column: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the cell was successfully selected; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Invoked in response to the [`setPath(_:)`](nsbrowser/setpath(_:).md) method of [`NSBrowser`](nsbrowser.md) being received by `sender`.

## Parameters

- `sender`: The browser.
- `title`: The title of the cell to select.
- `column`: The index of the column containing the cell to select.

## See Also

- [func selectedCell(inColumn: Int) -> Any?](nsbrowser/selectedcell(incolumn:).md)
  Returns the last (lowest) cell selected in the given column.
- [func browser(NSBrowser, selectRow: Int, inColumn: Int) -> Bool](nsbrowserdelegate/browser(_:selectrow:incolumn:).md)
  Asks the delegate to select the cell at the specified row and column location.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](nsbrowserdelegate/browser(_:selectionindexesforproposedselection:incolumn:).md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:selectcellwith:incolumn:))*