# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsMultipleSelection: Bool { get set }
```

#### Discussion

The default is [`false`](https://developer.apple.com/documentation/swift/false), which allows the user to select only one column or row at a time. You can select multiple columns or rows programmatically regardless of this setting.

## See Also

- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectcolumnindexes(_:byextendingselection:).md)
  Sets the column selection using `indexes` possibly extending the selection.
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectrowindexes(_:byextendingselection:).md)
  Sets the row selection using `indexes` extending the selection if specified.
- [var allowsColumnReordering: Bool](nstableview/allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](nstableview/allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](nstableview/allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowsmultipleselection)*