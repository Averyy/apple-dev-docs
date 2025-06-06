# contentWidthValueType

**Framework**: AppKit  
**Kind**: property

The type of value stored for the text block width.

**Availability**:
- macOS ?+

## Declaration

```swift
var contentWidthValueType: NSTextBlock.ValueType { get }
```

#### Discussion

This property determines how the width value should be interpreted.

## See Also

- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](nstextblock/setvalue(_:type:for:).md)
  Sets a dimension of the text block.
- [func value(for: NSTextBlock.Dimension) -> CGFloat](nstextblock/value(for:).md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](nstextblock/valuetype(for:).md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](nstextblock/setcontentwidth(_:type:).md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](nstextblock/contentwidth.md)
  The width of the text block.
- [NSTextBlock.Dimension](nstextblock/dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md), [`value(for:)`](nstextblock/value(for:).md), and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block dimensions.
- [NSTextBlock.ValueType](nstextblock/valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md) and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/contentwidthvaluetype)*