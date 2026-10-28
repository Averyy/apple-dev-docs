# setPathComponentCells(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the array of `NSPathComponentCell` objects currently being displayed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use the pathItems property instead

## Declaration

```swift
func setPathComponentCells(_ cells: [NSPathComponentCell])
```

```objc
- (void) setPathComponentCells:(NSArray<NSPathComponentCell *> *) cells;
```

## Discussion

Each item in the array must be an instance of `NSPathComponentCell` or a subclass thereof. You cannot set this value to `nil`, but you can set it to an empty array using, for example, `[NSArray array]`.

## Parameters

- `cells`: An array of `NSPathComponentCell` objects.

## See Also

### Deprecated
- [func clickedPathComponentCell() -> NSPathComponentCell?](./clickedpathcomponentcell%28%29.md)
  Returns the clicked cell.
- [func pathComponentCells() -> [NSPathComponentCell]](./pathcomponentcells%28%29.md)
  Returns an array of the `NSPathComponentCell` objects currently being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/setpathcomponentcells(_:))*