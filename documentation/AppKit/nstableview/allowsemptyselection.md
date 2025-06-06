# allowsEmptySelection

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view allows the user to select zero columns or rows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsEmptySelection: Bool { get set }
```

#### Discussion

The default is [`true`](https://developer.apple.com/documentation/swift/true), which allows the user to select zero columns or rows.

## See Also

- [func deselectRow(Int)](nstableview/deselectrow(_:).md)
  Deselects the row at the specified index if it’s selected.
- [func deselectColumn(Int)](nstableview/deselectcolumn(_:).md)
  Deselects the column at the specified index if it’s selected.
- [func deselectAll(Any?)](nstableview/deselectall(_:).md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.
- [var allowsColumnReordering: Bool](nstableview/allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](nstableview/allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](nstableview/allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsColumnSelection: Bool](nstableview/allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowsemptyselection)*