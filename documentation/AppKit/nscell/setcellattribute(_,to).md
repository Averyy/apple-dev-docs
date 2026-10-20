# setCellAttribute(_:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the value for the specified cell attribute.

**Availability**:
- macOS

## Declaration

```swift
func setCellAttribute(_ parameter: NSCell.Attribute, to value: Int)
```

```objc
- (void) setCellAttribute:(NSCellAttribute) parameter to:(NSInteger) value;
```

## Parameters

- `parameter`: The cell attribute whose value you want to set. Attributes include the receiver’s current state and  whether it is disabled, editable, or highlighted.
- `value`: The new value for the attribute.

## See Also

### Managing Cell Attributes
- [func cellAttribute(NSCell.Attribute) -> Int](./cellattribute%28_%29.md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](./type.md)
  The type of the cell.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.
- [var allowsUndo: Bool](./allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/setcellattribute(_:to:))*