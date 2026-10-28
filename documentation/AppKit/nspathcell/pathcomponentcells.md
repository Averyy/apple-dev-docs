# pathComponentCells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the array of `NSPathComponentCell` objects currently being displayed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var pathComponentCells: [NSPathComponentCell] { get set }
```

```objc
@property (copy) NSArray<__kindof NSPathComponentCell *> * pathComponentCells;
```

## Discussion

Each item in the array must be an instance of `NSPathComponentCell` or a subclass thereof. You cannot set this value to `nil`, but you can set it to an empty array using, for example, `[NSArray array]`.

## Parameters

- `cells`: An array of `NSPathComponentCell` objects.

## See Also

### Managing Path Components
- [class var pathComponentCellClass: AnyClass](./pathcomponentcellclass.md)
  Returns the class used to create `pathComponentCell` objects when automatically filling up the control.
- [func rect(of: NSPathComponentCell, withFrame: NSRect, in: NSView) -> NSRect](./rect%28of,withframe,in%29.md)
  Returns the current rectangle being displayed for a given path component cell, with respect to a given frame in a given view.
- [func pathComponentCell(at: NSPoint, withFrame: NSRect, in: NSView) -> NSPathComponentCell?](./pathcomponentcell%28at,withframe,in%29.md)
  Returns the cell located at the given point within the given frame of the given view.
- [var clickedPathComponentCell: NSPathComponentCell?](./clickedpathcomponentcell.md)
  Sets the value of the path displayed by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcell/pathcomponentcells)*