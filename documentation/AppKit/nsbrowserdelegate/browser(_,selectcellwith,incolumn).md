# browser(_:selectCellWith:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to select the cell with the given title in the specified column.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func browser(_ sender: NSBrowser, selectCellWith title: String, inColumn column: Int) -> Bool
```

```objc
- (BOOL) browser:(NSBrowser *) sender selectCellWithString:(NSString *) title inColumn:(NSInteger) column;
```

## Return Value

[`true`](../../Swift/true.md) if the cell was successfully selected; otherwise, [`false`](../../Swift/false.md).

## Discussion

Invoked in response to the [`setPath(_:)`](../nsbrowser/setpath%28_%29.md) method of [`NSBrowser`](../nsbrowser.md) being received by `sender`.

## Parameters

- `sender`: The browser.
- `title`: The title of the cell to select.
- `column`: The index of the column containing the cell to select.

## See Also

### Related Documentation
- [func selectedCell(inColumn: Int) -> Any?](../nsbrowser/selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
### Managing Selection
- [func browser(NSBrowser, selectRow: Int, inColumn: Int) -> Bool](./browser%28_,selectrow,incolumn%29.md)
  Asks the delegate to select the cell at the specified row and column location.
- [func browser(NSBrowser, selectionIndexesForProposedSelection: IndexSet, inColumn: Int) -> IndexSet](./browser%28_,selectionindexesforproposedselection,incolumn%29.md)
  Asks the delegate for a set of indexes to select when the user changes the selection in the browser with the keyboard or mouse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowserdelegate/browser(_:selectcellwith:incolumn:))*