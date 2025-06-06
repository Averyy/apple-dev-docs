# numberOfRows

**Framework**: AppKit  
**Kind**: property

The number of rows in the table.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfRows: Int { get }
```

#### Discussion

Typically you should not ask the table view how many rows it has; instead, interrogate the table view’s data source.

## See Also

- [func numberOfRows(in: NSTableView) -> Int](nstableviewdatasource/numberofrows(in:).md)
  Returns the number of records managed for `aTableView` by the data source object.
- [var numberOfColumns: Int](nstableview/numberofcolumns.md)
  The number of columns in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/numberofrows)*