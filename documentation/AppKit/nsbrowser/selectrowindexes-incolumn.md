# selectRowIndexes(_:inColumn:)

**Framework**: AppKit  
**Kind**: method

Specifies the selected rows in a given column of the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func selectRowIndexes(_ indexes: IndexSet, inColumn column: Int)
```

## Parameters

- `indexes`: Rows to be selected in column  .
- `column`: Column in which to select rows  .

## See Also

- [var allowsBranchSelection: Bool](nsbrowser/allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](nsbrowser/allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](nsbrowser/allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](nsbrowser/selectedrowindexes(incolumn:).md)
  Provides the indexes of the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](nsbrowser/allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectrowindexes(_:incolumn:))*