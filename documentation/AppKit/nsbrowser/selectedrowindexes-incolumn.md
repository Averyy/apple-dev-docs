# selectedRowIndexes(inColumn:)

**Framework**: AppKit  
**Kind**: method

Provides the indexes of the selected rows in a given column of the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func selectedRowIndexes(inColumn column: Int) -> IndexSet?
```

#### Return Value

Rows selected in column `columnIndex`.

## Parameters

- `column`: The column whose selected rows are provided.

## See Also

- [var allowsBranchSelection: Bool](nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](nsbrowser/allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectRowIndexes(IndexSet, inColumn: Int)](nsbrowser/selectrowindexes(_:incolumn:).md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedrowindexes(incolumn:))*