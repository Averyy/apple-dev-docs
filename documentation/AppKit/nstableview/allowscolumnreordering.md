# allowsColumnReordering

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsColumnReordering: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), which allows the user to rearrange the table view’s columns. You can rearrange columns programmatically regardless of this setting.

## See Also

- [func moveColumn(Int, toColumn: Int)](nstableview/movecolumn(_:tocolumn:).md)
  Moves the column and heading at the specified index to the new specified index.
- [var allowsColumnResizing: Bool](nstableview/allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](nstableview/allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](nstableview/allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowscolumnreordering)*