# rect(of:withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func rect(of cell: NSPathComponentCell, withFrame frame: NSRect, in view: NSView) -> NSRect
```

#### Return Value

The rectangle occupied by the path component cell. `NSZeroRect` is returned if `cell` is not found or is not currently visible.

## Parameters

- `cell`: The path component cell.
- `frame`: The frame of the view in which the cell appears.
- `view`: The view in which the cell appears.

## See Also

- [class var pathComponentCellClass: AnyClass](nspathcell/pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](nspathcell/pathcomponentcell(at:withframe:in:).md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
- [var pathComponentCells: [NSPathComponentCell]](nspathcell/pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/rect(of:withframe:in:))*