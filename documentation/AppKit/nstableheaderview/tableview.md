# tableView

**Framework**: AppKit  
**Kind**: property

The [`NSTableView`](nstableview.md) instance that this table header view belongs to.

**Availability**:
- macOS ?+

## Declaration

```swift
weak var tableView: NSTableView? { get set }
```

#### Discussion

You should never need to set this property; it’s assigned automatically when you set the header view for an `NSTableView`.

## See Also

- [class NSTableView](nstableview.md)
  A set of related records, displayed in rows that represent individual records and columns that represent the attributes of those records.
- [var headerView: NSTableHeaderView?](nstableview/headerview.md)
  The view object used to draw headers over columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/tableview)*