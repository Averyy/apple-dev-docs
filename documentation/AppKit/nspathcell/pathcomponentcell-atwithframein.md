# pathComponentCell(at:withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Returns the cell located at the given point within the given frame of the given view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func pathComponentCell(at point: NSPoint, withFrame frame: NSRect, in view: NSView) -> NSPathComponentCell?
```

#### Return Value

The component cell within which the given point is located, or `nil` if no cell exists at that location.

## Parameters

- `point`: The point within the returned cell.
- `frame`: The frame within which the point is located.
- `view`: The view within which the frame is located.

## See Also

- [class var pathComponentCellClass: AnyClass](nspathcell/pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](nspathcell/rect(of:withframe:in:).md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
- [var pathComponentCells: [NSPathComponentCell]](nspathcell/pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/pathcomponentcell(at:withframe:in:))*