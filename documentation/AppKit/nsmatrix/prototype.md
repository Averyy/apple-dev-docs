# prototype

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The prototype cell that’s copied whenever the matrix creates a new cell.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var prototype: NSCell? { get set }
```

```objc
@property (copy, nullable) NSCell * prototype;
```

## Discussion

When the value of this property is `nil`, there is no prototype cell.

## See Also

### Related Documentation
- [init(frame: NSRect, mode: NSMatrix.Mode, prototype: NSCell, numberOfRows: Int, numberOfColumns: Int)](./init%28frame,mode,prototype,numberofrows,numberofcolumns%29.md)
  Initializes and returns a newly allocated matrix of the specified size using the given cell as a prototype.
- [func makeCell(atRow: Int, column: Int) -> NSCell](./makecell%28atrow,column%29.md)
  Creates a new cell at the location specified by the given row and column in the receiver.
### Managing the Cell Class
- [var cellClass: AnyClass](./cellclass.md)
  The subclass of [`NSCell`](../nscell.md) that the matrix uses when creating new (empty) cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/prototype)*