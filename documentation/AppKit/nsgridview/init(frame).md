# init(frame:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated grid view object with the specified frame rectangle.

**Availability**:
- macOS 10.12+

## Declaration

```swift
init(frame frameRect: NSRect)
```

```objc
- (instancetype) initWithFrame:(NSRect) frameRect;
```

## Parameters

- `frameRect`: The frame rectangle for the view, measured in points. The origin of the frame is relative to the superview in which you plan to add it.

## See Also

### Creating a Grid View
- [convenience init(numberOfColumns: Int, rows: Int)](./init%28numberofcolumns,rows%29.md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [convenience init(views: [[NSView]])](./init%28views%29.md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(frame:))*