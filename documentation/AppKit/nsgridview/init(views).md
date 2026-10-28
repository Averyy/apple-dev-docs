# init(views:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated grid view object with the specified array of arrays of views.

**Availability**:
- macOS 10.12+

## Declaration

```swift
convenience init(views rows: [[NSView]])
```

```objc
+ (instancetype) gridViewWithViews:(NSArray<NSArray<NSView *> *> *) rows;
```

## Discussion

This method creates an autoreleased grid view large enough to hold the passed array of rows. Each element in the array is itself an array of views for that row.

## Parameters

- `rows`: An array of arrays of grid view row objects.

## See Also

### Creating a Grid View
- [convenience init(numberOfColumns: Int, rows: Int)](./init%28numberofcolumns,rows%29.md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [init(frame: NSRect)](./init%28frame%29.md)
  Creates a newly allocated grid view object with the specified frame rectangle.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a newly allocated grid view object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(views:))*