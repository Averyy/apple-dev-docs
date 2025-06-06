# init(frame:)

**Framework**: AppKit  
**Kind**: init

Creates a newly allocated grid view object with the specified frame rectangle.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
init(frame frameRect: NSRect)
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it.

## See Also

- [convenience init(numberOfColumns: Int, rows: Int)](nsgridview/init(numberofcolumns:rows:).md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [convenience init(views: [[NSView]])](nsgridview/init(views:).md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init?(coder: NSCoder)](nsgridview/init(coder:).md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(frame:))*