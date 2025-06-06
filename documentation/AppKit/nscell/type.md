# type

**Framework**: AppKit  
**Kind**: property

The type of the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var type: NSCell.CellType { get set }
```

#### Discussion

When you change the cell type to [`NSCell.CellType.textCellType`](nscell/celltype/textcelltype.md), the cell converts gives itself a default title and sets the font to the system font at the default size. When you change the cell type to [`NSCell.CellType.imageCellType`](nscell/celltype/imagecelltype.md), the cell type does not change until you assign a new non-`nil` image to it.

For a list of possible cell types, see [`NSCell.CellType`](nscell/celltype.md).

## See Also

- [var image: NSImage?](nscell/image.md)
  The image displayed by the cell, if any.
- [func setCellAttribute(NSCell.Attribute, to: Int)](nscell/setcellattribute(_:to:).md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](nscell/cellattribute(_:).md)
  Returns the value for the specified cell attribute.
- [var isEnabled: Bool](nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](nscell/allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/type)*