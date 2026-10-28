# numberOfColumns

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the number of columns represented by views in the table row view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var numberOfColumns: Int { get }
```

```objc
@property (readonly) NSInteger numberOfColumns;
```

## Discussion

The number of columns may not be equal to the number of columns in the enclosing [`NSTableView`](../nstableview.md), if this row view is a group style and has a single view that spans the entire width of the row.

## See Also

### Row Grouping
- [var isGroupRowStyle: Bool](./isgrouprowstyle.md)
  Specifies whether this row view is a group row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview/numberofcolumns)*