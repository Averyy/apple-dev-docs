# cellAttribute(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified cell attribute.

**Availability**:
- macOS

## Declaration

```swift
func cellAttribute(_ parameter: NSCell.Attribute) -> Int
```

```objc
- (NSInteger) cellAttribute:(NSCellAttribute) parameter;
```

#### Return Value

The value for the cell attribute specified by `aParameter`.

## Parameters

- `parameter`: The cell attribute whose value you want to get. Attributes include the receiver’s current state and  whether it is disabled, editable, or highlighted.

## See Also

### Managing Cell Attributes
- [func setCellAttribute(NSCell.Attribute, to: Int)](./setcellattribute%28_,to%29.md)
  Sets the value for the specified cell attribute.
- [var type: NSCell.CellType](./type.md)
  The type of the cell.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](./allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/cellattribute(_:))*