# clickedPathComponentCell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the value of the path displayed by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var clickedPathComponentCell: NSPathComponentCell? { get }
```

```objc
@property (strong, readonly, nullable) NSPathComponentCell * clickedPathComponentCell;
```

#### Discussion

When setting, an array of `NSPathComponentCell` objects is automatically set, based on the path in `url`. The type of `NSPathComponentCell` objects created can be controlled by subclassing `NSPathCell` and overriding [`pathComponentCellClass`](./pathcomponentcellclass.md).

If `url` is a file URL (returns [`true`](../../Swift/true.md) from [`isFileURL`](../../Foundation/nsurl/isfileurl.md)), the images are automatically filled with file icons, if the path exists. The URL value itself is stored in the `objectValue` property of the cell.

## Parameters

- `url`: The new path value to display.

## See Also

### Managing Path Components
- [class var pathComponentCellClass: AnyClass](./pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](./rect%28of,withframe,in%29.md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](./pathcomponentcell%28at,withframe,in%29.md)
  Returns the cell located at the given point within the given frame of the given view.
- [var pathComponentCells: [NSPathComponentCell]](./pathcomponentcells.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/clickedpathcomponentcell)*