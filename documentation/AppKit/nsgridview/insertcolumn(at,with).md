# insertColumn(at:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the array of view objects at the specified index.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func insertColumn(at index: Int, with views: [NSView]) -> NSGridColumn
```

```objc
- (NSGridColumn *) insertColumnAtIndex:(NSInteger) index withViews:(NSArray<NSView *> *) views;
```

## See Also

### Adding, Removing, and Moving Columns
- [func addColumn(with: [NSView]) -> NSGridColumn](./addcolumn%28with%29.md)
  Adds a new column containing the array of views.
- [func removeColumn(at: Int)](./removecolumn%28at%29.md)
  Removes the column from the grid view at the specified index.
- [func moveColumn(at: Int, to: Int)](./movecolumn%28at,to%29.md)
  Moves the specified column to a new column location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/insertcolumn(at:with:))*