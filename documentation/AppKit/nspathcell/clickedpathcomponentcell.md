# clickedPathComponentCell

**Framework**: AppKit  
**Kind**: property

Sets the value of the path displayed by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var clickedPathComponentCell: NSPathComponentCell? { get }
```

#### Discussion

When setting, an array of `NSPathComponentCell` objects is automatically set, based on the path in `url`. The type of `NSPathComponentCell` objects created can be controlled by subclassing `NSPathCell` and overriding [`pathComponentCellClass`](nspathcell/pathcomponentcellclass.md).

If `url` is a file URL (returns [`true`](https://developer.apple.com/documentation/swift/true) from [`isFileURL`](https://developer.apple.com/documentation/Foundation/NSURL/isFileURL)), the images are automatically filled with file icons, if the path exists. The URL value itself is stored in the `objectValue` property of the cell.

## Parameters

- `url`: The new path value to display.

## See Also

- [class var pathComponentCellClass: AnyClass](nspathcell/pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](nspathcell/rect(of:withframe:in:).md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](nspathcell/pathcomponentcell(at:withframe:in:).md)
  Returns the cell located at the given point within the given frame of the given view.
- [var pathComponentCells: [NSPathComponentCell]](nspathcell/pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/clickedpathcomponentcell)*