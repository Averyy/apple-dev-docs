# clickedPathComponentCell()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the clicked cell.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the clickedPathItem property instead

## Declaration

```swift
func clickedPathComponentCell() -> NSPathComponentCell?
```

```objc
- (NSPathComponentCell *) clickedPathComponentCell;
```

## Return Value

The component cell that was clicked.

## Discussion

The value returned is generally valid only when the action or double action is being sent.

> **Note**:  In OS X v10.5 and earlier the returned value was [nil] if no cell had been clicked. In OS X v10.6, the folder of the cell that the user selected is returned instead.

## See Also

### Deprecated
- [func pathComponentCells() -> [NSPathComponentCell]](./pathcomponentcells%28%29.md)
  Returns an array of the `NSPathComponentCell` objects currently being displayed.
- [func setPathComponentCells([NSPathComponentCell])](./setpathcomponentcells%28_%29.md)
  Sets the array of `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/clickedpathcomponentcell())*