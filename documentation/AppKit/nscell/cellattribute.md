# cellAttribute(_:)

**Framework**: AppKit  
**Kind**: method

Returns the value for the specified cell attribute.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cellAttribute(_ parameter: NSCell.Attribute) -> Int
```

#### Return Value

The value for the cell attribute specified by `aParameter`.

## Parameters

- `parameter`: The cell attribute whose value you want to get. Attributes include the receiver’s current state and  whether it is disabled, editable, or highlighted.

## See Also

- [func setCellAttribute(NSCell.Attribute, to: Int)](nscell/setcellattribute(_:to:).md)
  Sets the value for the specified cell attribute.
- [var type: NSCell.CellType](nscell/type.md)
  The type of the cell.
- [var isEnabled: Bool](nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](nscell/allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/cellattribute(_:))*