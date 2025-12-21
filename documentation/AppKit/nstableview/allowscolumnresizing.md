# allowsColumnResizing

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsColumnResizing: Bool { get set }
```

#### Discussion

The default of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which allows the user to resize the table view’s columns. You can resize columns programmatically regardless of this setting.

## See Also

- [var width: CGFloat](nstablecolumn/width.md)
  The table column’s width, in points.
- [var allowsColumnReordering: Bool](nstableview/allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsMultipleSelection: Bool](nstableview/allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](nstableview/allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](nstableview/usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowscolumnresizing)*