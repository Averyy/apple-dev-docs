# setCellsStyleMask(_:)

**Framework**: Quartz  
**Kind**: method

Defines the appearance style of the cells.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setCellsStyleMask(_ mask: Int)
```

## Parameters

- `mask`: An integer bit mask.   A mask can be specified by combining any of the options described in   using the C bitwise   operator.

## See Also

- [func cellsStyleMask() -> Int](ikimagebrowserview/cellsstylemask.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](ikimagebrowserview/setconstrainstooriginalsize(_:).md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](ikimagebrowserview/constrainstooriginalsize.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func setIntercellSpacing(NSSize)](ikimagebrowserview/setintercellspacing(_:).md)
  Sets the spacing between cells in the view.
- [func intercellSpacing() -> NSSize](ikimagebrowserview/intercellspacing.md)
  Returns the spacing between cells in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcellsstylemask(_:))*