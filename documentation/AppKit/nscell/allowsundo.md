# allowsUndo

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell assumes responsibility for undo operations.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsUndo: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the cell handles undo operations itself or [`false`](https://developer.apple.com/documentation/Swift/false) if the app’s custom undo manager must handle undo behavior. Cell subclasses set the value of this property to indicate their preference for handling undo operations. For example, the [`NSTextFieldCell`](nstextfieldcell.md) class uses sets this property to indicate it handles undo operations for edited text, and other controls set a value that is appropriate for their implementation. Do not change the value of this property otherwise.

## See Also

- [func setCellAttribute(NSCell.Attribute, to: Int)](nscell/setcellattribute(_:to:).md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](nscell/cellattribute(_:).md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](nscell/type.md)
  The type of the cell.
- [var isEnabled: Bool](nscell/isenabled.md)
  A Boolean value indicating whether the cell is currently enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/allowsundo)*