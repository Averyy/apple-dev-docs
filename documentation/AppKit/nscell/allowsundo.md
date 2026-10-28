# allowsUndo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell assumes responsibility for undo operations.

**Availability**:
- macOS

## Declaration

```swift
var allowsUndo: Bool { get set }
```

```objc
@property BOOL allowsUndo;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the cell handles undo operations itself or [`false`](../../Swift/false.md) if the app’s custom undo manager must handle undo behavior. Cell subclasses set the value of this property to indicate their preference for handling undo operations. For example, the [`NSTextFieldCell`](../nstextfieldcell.md) class uses sets this property to indicate it handles undo operations for edited text, and other controls set a value that is appropriate for their implementation. Do not change the value of this property otherwise.

## See Also

### Managing Cell Attributes
- [func setCellAttribute(NSCell.Attribute, to: Int)](./setcellattribute%28_,to%29.md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](./cellattribute%28_%29.md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](./type.md)
  The type of the cell.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/allowsundo)*