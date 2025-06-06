# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the cell is currently enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the cell is enabled or [`false`](https://developer.apple.com/documentation/swift/false) when it is disabled. The text of disabled cells is gray. If a cell is disabled, it cannot be highlighted, does not support mouse tracking (and thus cannot participate in target/action functionality), and cannot be edited. However, you can still alter many attributes of a disabled cell programmatically. (The [`state`](nscell/state.md) property, for instance, still works.)

## See Also

- [func setCellAttribute(NSCell.Attribute, to: Int)](nscell/setcellattribute(_:to:).md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](nscell/cellattribute(_:).md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](nscell/type.md)
  The type of the cell.
- [var allowsUndo: Bool](nscell/allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isenabled)*