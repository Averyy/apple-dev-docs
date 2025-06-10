# clickedPathComponentCell()

**Framework**: AppKit  
**Kind**: method

Returns the clicked cell.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func clickedPathComponentCell() -> NSPathComponentCell?
```

#### Return Value

The component cell that was clicked.

#### Discussion

The value returned is generally valid only when the action or double action is being sent.

> **Note**:  In OS X v10.5 and earlier the returned value was [nil] if no cell had been clicked. In OS X v10.6, the folder of the cell that the user selected is returned instead.

## See Also

- [func pathComponentCells() -> [NSPathComponentCell]](nspathcontrol/pathcomponentcells.md)
  Returns an array of the `NSPathComponentCell` objects currently being displayed.
- [func setPathComponentCells([NSPathComponentCell])](nspathcontrol/setpathcomponentcells(_:).md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/clickedpathcomponentcell())*