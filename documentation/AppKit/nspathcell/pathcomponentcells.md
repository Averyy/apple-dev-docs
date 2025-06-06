# pathComponentCells

**Framework**: AppKit  
**Kind**: property

Sets the array of `NSPathComponentCell` objects currently being displayed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var pathComponentCells: [NSPathComponentCell] { get set }
```

#### Discussion

Each item in the array must be an instance of `NSPathComponentCell` or a subclass thereof. You cannot set this value to `nil`, but you can set it to an empty array using, for example, `[NSArray array]`.

## Parameters

- `cells`: An array of   objects.

## See Also

- [class var pathComponentCellClass: AnyClass](nspathcell/pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](nspathcell/rect(of:withframe:in:).md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](nspathcell/pathcomponentcell(at:withframe:in:).md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/pathcomponentcells)*