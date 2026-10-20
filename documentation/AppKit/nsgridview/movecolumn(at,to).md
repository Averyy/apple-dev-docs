# moveColumn(at:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the specified column to a new column location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func moveColumn(at fromIndex: Int, to toIndex: Int)
```

```objc
- (void) moveColumnAtIndex:(NSInteger) fromIndex toIndex:(NSInteger) toIndex;
```

## See Also

### Adding, Removing, and Moving Columns
- [func addColumn(with: [NSView]) -> NSGridColumn](./addcolumn%28with%29.md)
  Adds a new column containing the array of views.
- [func insertColumn(at: Int, with: [NSView]) -> NSGridColumn](./insertcolumn%28at,with%29.md)
  Inserts the array of view objects at the specified index.
- [func removeColumn(at: Int)](./removecolumn%28at%29.md)
  Removes the column from the grid view at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/movecolumn(at:to:))*