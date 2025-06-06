# autosizesCells

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the cell sizes change when the receiver is resized.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var autosizesCells: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), whenever the matrix is resized, the sizes of the cells change in proportion, keeping the intercell space constant. This property verifies that the cell sizes and intercell spacing add up to the exact size of the matrix, adjusting the size of the cells and updating the matrix if they don’t. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), then the intercell spacing and cell size remain constant.

## See Also

- [func setValidateSize(Bool)](nsmatrix/setvalidatesize(_:).md)
  Specifies whether the receiver’s size information is validated.
- [func sizeToCells()](nsmatrix/sizetocells.md)
  Changes the width and the height of the receiver’s frame so it exactly contains the cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/autosizescells)*