# addRow(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds an array of views to a new row.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func addRow(with views: [NSView]) -> NSGridRow
```

```objc
- (NSGridRow *) addRowWithViews:(NSArray<NSView *> *) views;
```

## Discussion

You can insert and remove rows and columns dynamically in a grid view. The grid is enlarged as needed to hold the specified views.

## See Also

### Adding, Removing, and Moving Rows
- [func insertRow(at: Int, with: [NSView]) -> NSGridRow](./insertrow%28at,with%29.md)
  Inserts the array of view objects into the grid view at the index.
- [func removeRow(at: Int)](./removerow%28at%29.md)
  Removes the row from the grid view at the index.
- [func moveRow(at: Int, to: Int)](./moverow%28at,to%29.md)
  Moves the specified row to the new row location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview/addrow(with:))*