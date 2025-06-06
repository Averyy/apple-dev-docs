# setValue(_:type:for:)

**Framework**: AppKit  
**Kind**: method

Sets a dimension of the text block.

**Availability**:
- macOS ?+

## Declaration

```swift
func setValue(_ val: CGFloat, type: NSTextBlock.ValueType, for dimension: NSTextBlock.Dimension)
```

## Parameters

- `val`: The new value for the dimension.
- `type`: The type of value being provided. This controls how   is interpreted.
- `dimension`: The dimension to set.

## See Also

- [func value(for: NSTextBlock.Dimension) -> CGFloat](nstextblock/value(for:).md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](nstextblock/valuetype(for:).md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](nstextblock/setcontentwidth(_:type:).md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](nstextblock/contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](nstextblock/contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](nstextblock/dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md), [`value(for:)`](nstextblock/value(for:).md), and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block dimensions.
- [NSTextBlock.ValueType](nstextblock/valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md) and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setvalue(_:type:for:))*