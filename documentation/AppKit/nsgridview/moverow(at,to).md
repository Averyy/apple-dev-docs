# moveRow(at:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the specified row to the new row location.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func moveRow(at fromIndex: Int, to toIndex: Int)
```

```objc
- (void) moveRowAtIndex:(NSInteger) fromIndex toIndex:(NSInteger) toIndex;
```

## See Also

### Adding, Removing, and Moving Rows
- [func addRow(with: [NSView]) -> NSGridRow](./addrow%28with%29.md)
  Adds an array of views to a new row.
- [func insertRow(at: Int, with: [NSView]) -> NSGridRow](./insertrow%28at,with%29.md)
  Inserts the array of view objects into the grid view at the index.
- [func removeRow(at: Int)](./removerow%28at%29.md)
  Removes the row from the grid view at the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/moverow(at:to:))*