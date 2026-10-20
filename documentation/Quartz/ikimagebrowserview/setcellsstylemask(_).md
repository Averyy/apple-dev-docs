# setCellsStyleMask(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Defines the appearance style of the cells.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setCellsStyleMask(_ mask: Int)
```

```objc
- (void) setCellsStyleMask:(NSUInteger) mask;
```

## Parameters

- `mask`: An integer bit mask.   A mask can be specified by combining any of the options described in [Cell Appearance Style Masks](../api-1564248-cell-appearance-style-masks.md) using the C bitwise `OR` operator.

## See Also

### Setting the Appearance
- [func cellsStyleMask() -> Int](./cellsstylemask%28%29.md)
  Returns the appearance style mask for the cell.
- [func setConstrainsToOriginalSize(Bool)](./setconstrainstooriginalsize%28_%29.md)
  Sets whether the receiver constrains the cell’s image to its original size.
- [func constrainsToOriginalSize() -> Bool](./constrainstooriginalsize%28%29.md)
  Returns whether the receiver constrains the cell’s image to its original size.
- [func setIntercellSpacing(NSSize)](./setintercellspacing%28_%29.md)
  Sets the spacing between cells in the view.
- [func intercellSpacing() -> NSSize](./intercellspacing%28%29.md)
  Returns the spacing between cells in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setcellsstylemask(_:))*