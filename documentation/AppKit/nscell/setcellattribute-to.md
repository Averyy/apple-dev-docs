# setCellAttribute(_:to:)

**Framework**: AppKit  
**Kind**: method

Sets the value for the specified cell attribute.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setCellAttribute(_ parameter: NSCell.Attribute, to value: Int)
```

## Parameters

- `parameter`: The cell attribute whose value you want to set. Attributes include the receiver’s current state and  whether it is disabled, editable, or highlighted.
- `value`: The new value for the attribute.

## See Also

- [func cellAttribute(NSCell.Attribute) -> Int](nscell/cellattribute(_:).md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](nscell/type.md)
  The type of the cell.
- [var isEnabled: Bool](nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](nscell/allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setcellattribute(_:to:))*