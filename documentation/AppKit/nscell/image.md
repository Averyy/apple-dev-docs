# image

**Framework**: AppKit  
**Kind**: property

The image displayed by the cell, if any.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var image: NSImage? { get set }
```

#### Discussion

Setting the value of this property converts the cell to an image-type cell, if it is not one already. The value of this property is `nil` if the cell is not an image-type cell.

## See Also

- [var type: NSCell.CellType](nscell/type.md)
  The type of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/image)*