# setIntercellSpacing(_:)

**Framework**: Quartz  
**Kind**: method

Sets the spacing between cells in the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setIntercellSpacing(_ aSize: NSSize)
```

#### Discussion

By default, both values are `10.0` in the receiver’s coordinate system.

## Parameters

- `aSize`: The vertical and horizontal spacing between cells.

## See Also

- [func setCellsStyleMask(Int)](ikimagebrowserview/setcellsstylemask(_:).md)
  Defines the appearance style of the cells.
- [func cellsStyleMask() -> Int](ikimagebrowserview/cellsstylemask.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](ikimagebrowserview/setconstrainstooriginalsize(_:).md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](ikimagebrowserview/constrainstooriginalsize.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func intercellSpacing() -> NSSize](ikimagebrowserview/intercellspacing.md)
  Returns the spacing between cells in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setintercellspacing(_:))*