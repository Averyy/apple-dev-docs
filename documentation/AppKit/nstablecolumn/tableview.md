# tableView

**Framework**: AppKit  
**Kind**: property

The table view that contains the table column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var tableView: NSTableView? { get set }
```

#### Discussion

You should never need to set this property; it’s set automatically when you add a table column to a table view using the `NSTableView` class’s method [`addTableColumn(_:)`](nstableview/addtablecolumn(_:).md).

## See Also

- [func addTableColumn(NSTableColumn)](nstableview/addtablecolumn(_:).md)
  Adds the specified column as the last column of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/tableview)*