# rect(of:withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func rect(of cell: NSPathComponentCell, withFrame frame: NSRect, in view: NSView) -> NSRect
```

```objc
- (NSRect) rectOfPathComponentCell:(NSPathComponentCell *) cell withFrame:(NSRect) frame inView:(NSView *) view;
```

## Return Value

The rectangle occupied by the path component cell. `NSZeroRect` is returned if `cell` is not found or is not currently visible.

## Parameters

- `cell`: The path component cell.
- `frame`: The frame of the view in which the cell appears.
- `view`: The view in which the cell appears.

## See Also

### Managing Path Components
- [class var pathComponentCellClass: AnyClass](./pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](./pathcomponentcell%28at,withframe,in%29.md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](./clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
- [var pathComponentCells: [NSPathComponentCell]](./pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/rect(of:withframe:in:))*