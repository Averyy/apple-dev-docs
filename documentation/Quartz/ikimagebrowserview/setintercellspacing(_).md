# setIntercellSpacing(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Sets the spacing between cells in the view.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setIntercellSpacing(_ aSize: NSSize)
```

```objc
- (void) setIntercellSpacing:(NSSize) aSize;
```

## Discussion

By default, both values are `10.0` in the receiver’s coordinate system.

## Parameters

- `aSize`: The vertical and horizontal spacing between cells.

## See Also

### Setting the Appearance
- [func setCellsStyleMask(Int)](./setcellsstylemask%28_%29.md)
  Defines the appearance style of the cells.
- [func cellsStyleMask() -> Int](./cellsstylemask%28%29.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](./setconstrainstooriginalsize%28_%29.md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](./constrainstooriginalsize%28%29.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func intercellSpacing() -> NSSize](./intercellspacing%28%29.md)
  Returns the spacing between cells in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setintercellspacing(_:))*