# init(numberOfColumns:rows:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated grid view object with the specified number of columns and rows.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(numberOfColumns columnCount: Int, rows rowCount: Int)
```

```objc
+ (instancetype) gridViewWithNumberOfColumns:(NSInteger) columnCount rows:(NSInteger) rowCount;
```

## Parameters

- `columnCount`: The number of columns for this grid view.
- `rowCount`: The number of rows for this grid view.

## See Also

### Creating a Grid View
- [convenience init(views: [[NSView]])](./init%28views%29.md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init(frame: NSRect)](./init%28frame%29.md)
  Creates a newly allocated grid view object with the specified frame rectangle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(numberofcolumns:rows:))*