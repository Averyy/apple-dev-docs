# insertRow(at:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the array of view objects into the grid view at the index.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func insertRow(at index: Int, with views: [NSView]) -> NSGridRow
```

```objc
- (NSGridRow *) insertRowAtIndex:(NSInteger) index withViews:(NSArray<NSView *> *) views;
```

## See Also

### Adding, Removing, and Moving Rows
- [func addRow(with: [NSView]) -> NSGridRow](./addrow%28with%29.md)
  Adds an array of views to a new row.
- [func removeRow(at: Int)](./removerow%28at%29.md)
  Removes the row from the grid view at the index.
- [func moveRow(at: Int, to: Int)](./moverow%28at,to%29.md)
  Moves the specified row to the new row location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/insertrow(at:with:))*