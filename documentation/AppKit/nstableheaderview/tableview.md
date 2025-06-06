# tableView

**Framework**: AppKit  
**Kind**: property

The [`NSTableView`](nstableview.md) instance that this table header view belongs to.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var tableView: NSTableView? { get set }
```

#### Discussion

You should never need to set this property; it’s assigned automatically when you set the header view for an `NSTableView`.

## See Also

- [Table View Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TableView/Introduction/Introduction.html#//apple_ref/doc/uid/10000026i)
- [var headerView: NSTableHeaderView?](nstableview/headerview.md)
  The view object used to draw headers over columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview/tableview)*