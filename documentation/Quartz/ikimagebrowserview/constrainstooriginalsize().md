# constrainsToOriginalSize()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the receiver constrains the cell’s image to its original size.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func constrainsToOriginalSize() -> Bool
```

```objc
- (BOOL) constrainsToOriginalSize;
```

#### Return Value

[`false`](../../Swift/false.md) if the image is not constrained; otherwise [`true`](../../Swift/true.md).

## See Also

### Setting the Appearance
- [func setCellsStyleMask(Int)](./setcellsstylemask%28_%29.md)
  Defines the appearance style of the cells.
- [func cellsStyleMask() -> Int](./cellsstylemask%28%29.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](./setconstrainstooriginalsize%28_%29.md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func setIntercellSpacing(NSSize)](./setintercellspacing%28_%29.md)
  Sets the spacing between cells in the view.
- [func intercellSpacing() -> NSSize](./intercellspacing%28%29.md)
  Returns the spacing between cells in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/constrainstooriginalsize())*