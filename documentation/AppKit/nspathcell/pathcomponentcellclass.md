# pathComponentCellClass

**Framework**: AppKit  
**Kind**: property

Returns the class used to create `pathComponentCell` objects when automatically filling up the control.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
class var pathComponentCellClass: AnyClass { get }
```

#### Return Value

The class used to create `NSPathComponentCell` objects.

#### Discussion

Subclasses can override this method to return a custom cell class that is automatically used. By default, the method returns `[NSPathComponentCell class]`, or a specialized subclass thereof.

## See Also

- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](nspathcell/rect(of:withframe:in:).md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](nspathcell/pathcomponentcell(at:withframe:in:).md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](nspathcell/clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.
- [var pathComponentCells: [NSPathComponentCell]](nspathcell/pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/pathcomponentcellclass)*