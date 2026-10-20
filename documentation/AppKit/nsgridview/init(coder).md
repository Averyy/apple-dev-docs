# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated grid view object from the coder.

**Availability**:
- macOS 10.12+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The coder object.

## See Also

### Creating a Grid View
- [convenience init(numberOfColumns: Int, rows: Int)](./init%28numberofcolumns,rows%29.md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [convenience init(views: [[NSView]])](./init%28views%29.md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init(frame: NSRect)](./init%28frame%29.md)
  Creates a newly allocated grid view object with the specified frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/init(coder:))*