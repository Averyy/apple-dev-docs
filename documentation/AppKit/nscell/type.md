# type

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of the cell.

**Availability**:
- macOS

## Declaration

```swift
var type: NSCell.CellType { get set }
```

```objc
@property NSCellType type;
```

## Discussion

When you change the cell type to [`NSCell.CellType.textCellType`](./celltype/textcelltype.md), the cell converts gives itself a default title and sets the font to the system font at the default size. When you change the cell type to [`NSCell.CellType.imageCellType`](./celltype/imagecelltype.md), the cell type does not change until you assign a new non-`nil` image to it.

For a list of possible cell types, see [`NSCell.CellType`](./celltype.md).

## See Also

### Related Documentation
- [var image: NSImage?](./image.md)
  The image displayed by the cell, if any.
### Managing Cell Attributes
- [func setCellAttribute(NSCell.Attribute, to: Int)](./setcellattribute%28_,to%29.md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](./cellattribute%28_%29.md)
  Returns the value for the specified cell attribute.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](./allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/type)*