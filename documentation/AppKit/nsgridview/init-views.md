# init(views:)

**Framework**: AppKit  
**Kind**: init

Creates a newly allocated grid view object with the specified array of arrays of views.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(views rows: [[NSView]])
```

#### Discussion

This method creates an autoreleased grid view large enough to hold the passed array of rows. Each element in the array is itself an array of views for that row.

## Parameters

- `rows`: An array of arrays of grid view row objects.

## See Also

- [convenience init(numberOfColumns: Int, rows: Int)](nsgridview/init(numberofcolumns:rows:).md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [init(frame: NSRect)](nsgridview/init(frame:).md)
  Creates a newly allocated grid view object with the specified frame rectangle.
- [init?(coder: NSCoder)](nsgridview/init(coder:).md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(views:))*