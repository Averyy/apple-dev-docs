# isEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the cell is currently enabled.

**Availability**:
- macOS

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (getter=isEnabled) BOOL enabled;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the cell is enabled or [`false`](../../Swift/false.md) when it is disabled. The text of disabled cells is gray. If a cell is disabled, it cannot be highlighted, does not support mouse tracking (and thus cannot participate in target/action functionality), and cannot be edited. However, you can still alter many attributes of a disabled cell programmatically. (The [`state`](./state.md) property, for instance, still works.)

## See Also

### Managing Cell Attributes
- [func setCellAttribute(NSCell.Attribute, to: Int)](./setcellattribute%28_,to%29.md)
  Sets the value for the specified cell attribute.
- [func cellAttribute(NSCell.Attribute) -> Int](./cellattribute%28_%29.md)
  Returns the value for the specified cell attribute.
- [var type: NSCell.CellType](./type.md)
  The type of the cell.
- [var allowsUndo: Bool](./allowsundo.md)
  A Boolean value indicating whether the cell assumes responsibility for undo operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/isenabled)*