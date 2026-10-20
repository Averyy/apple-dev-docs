# addColumn(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a new column containing the array of views.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func addColumn(with views: [NSView]) -> NSGridColumn
```

```objc
- (NSGridColumn *) addColumnWithViews:(NSArray<NSView *> *) views;
```

#### Return Value

The newly created grid column.

## See Also

### Adding, Removing, and Moving Columns
- [func insertColumn(at: Int, with: [NSView]) -> NSGridColumn](./insertcolumn%28at,with%29.md)
  Inserts the array of view objects at the specified index.
- [func removeColumn(at: Int)](./removecolumn%28at%29.md)
  Removes the column from the grid view at the specified index.
- [func moveColumn(at: Int, to: Int)](./movecolumn%28at,to%29.md)
  Moves the specified column to a new column location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/addcolumn(with:))*