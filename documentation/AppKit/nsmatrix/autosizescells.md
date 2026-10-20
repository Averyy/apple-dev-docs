# autosizesCells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the cell sizes change when the receiver is resized.

**Availability**:
- macOS

## Declaration

```swift
var autosizesCells: Bool { get set }
```

```objc
@property BOOL autosizesCells;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), whenever the matrix is resized, the sizes of the cells change in proportion, keeping the intercell space constant. This property verifies that the cell sizes and intercell spacing add up to the exact size of the matrix, adjusting the size of the cells and updating the matrix if they don’t. When the value of this property is [`false`](../../Swift/false.md), then the intercell spacing and cell size remain constant.

## See Also

### Resizing the Matrix and Its Cells
- [func setValidateSize(Bool)](./setvalidatesize%28_%29.md)
  Specifies whether the receiver’s size information is validated.
- [func sizeToCells()](./sizetocells%28%29.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/autosizescells)*