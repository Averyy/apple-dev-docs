# NSTableView.RowSizeStyle.medium

**Framework**: AppKit  
**Kind**: case

The table will use a row height specified for a medium table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.

**Availability**:
- macOS 10.7+

## Declaration

```swift
case medium
```

## See Also

- [NSTableView.RowSizeStyle.default](nstableview/rowsizestyle-swift.enum/default.md)
  The table will use the system default layout size: small, medium or large.
- [NSTableView.RowSizeStyle.custom](nstableview/rowsizestyle-swift.enum/custom.md)
  The table will use the [`rowHeight`](nstableview/rowheight.md) or invoke the delegate method [`tableView(_:heightOfRow:)`](nstableviewdelegate/tableview(_:heightofrow:).md), if implemented. The cell layout is not changed.
- [NSTableView.RowSizeStyle.small](nstableview/rowsizestyle-swift.enum/small.md)
  The table will use a row height specified for a small table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.
- [NSTableView.RowSizeStyle.large](nstableview/rowsizestyle-swift.enum/large.md)
  The table will use a row height specified for a large table. It is required that the size be fully tested and supported if `NSTableViewRowSizeStyleCustom` is not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowsizestyle-swift.enum/medium)*