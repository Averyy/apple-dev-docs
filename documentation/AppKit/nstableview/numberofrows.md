# numberOfRows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of rows in the table.

**Availability**:
- macOS

## Declaration

```swift
var numberOfRows: Int { get }
```

```objc
@property (readonly) NSInteger numberOfRows;
```

## Discussion

Typically you should not ask the table view how many rows it has; instead, interrogate the table view’s data source.

## See Also

### Related Documentation
- [func numberOfRows(in: NSTableView) -> Int](../nstableviewdatasource/numberofrows%28in%29.md)
  Returns the number of records managed for `aTableView` by the data source object.
### Table Dimensions
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/numberofrows)*