# setPathComponentCells(_:)

**Framework**: AppKit  
**Kind**: method

Sets the array of `NSPathComponentCell` objects currently being displayed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func setPathComponentCells(_ cells: [NSPathComponentCell])
```

#### Discussion

Each item in the array must be an instance of `NSPathComponentCell` or a subclass thereof. You cannot set this value to `nil`, but you can set it to an empty array using, for example, `[NSArray array]`.

## Parameters

- `cells`: An array of   objects.

## See Also

- [func clickedPathComponentCell() -> NSPathComponentCell?](nspathcontrol/clickedpathcomponentcell.md)
  Returns the clicked cell.
- [func pathComponentCells() -> [NSPathComponentCell]](nspathcontrol/pathcomponentcells.md)
  Returns an array of the `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/setpathcomponentcells(_:))*