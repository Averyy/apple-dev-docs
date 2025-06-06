# init(numberOfColumns:rows:)

**Framework**: AppKit  
**Kind**: init

Creates a newly allocated grid view object with the specified number of columns and rows.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(numberOfColumns columnCount: Int, rows rowCount: Int)
```

## Parameters

- `columnCount`: The number of columns for this grid view.
- `rowCount`: The number of rows for this grid view.

## See Also

- [convenience init(views: [[NSView]])](nsgridview/init(views:).md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init(frame: NSRect)](nsgridview/init(frame:).md)
  Creates a newly allocated grid view object with the specified frame rectangle.
- [init?(coder: NSCoder)](nsgridview/init(coder:).md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(numberofcolumns:rows:))*