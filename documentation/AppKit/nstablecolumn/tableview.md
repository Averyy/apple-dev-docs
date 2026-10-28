# tableView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The table view that contains the table column.

**Availability**:
- macOS

## Declaration

```swift
weak var tableView: NSTableView? { get set }
```

```objc
@property (weak, nullable) NSTableView * tableView;
```

## Discussion

You should never need to set this property; it’s set automatically when you add a table column to a table view using the `NSTableView` class’s method [`addTableColumn(_:)`](../nstableview/addtablecolumn%28_%29.md).

## See Also

### Related Documentation
- [func addTableColumn(NSTableColumn)](../nstableview/addtablecolumn%28_%29.md)
  Adds the specified column as the last column of the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/tableview)*