# setWidth(_:type:for:)

**Framework**: AppKit  
**Kind**: method

Sets the width of all edges of a specified layer of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setWidth(_ width: CGFloat, type: NSTextBlock.ValueType, for layer: NSTextBlock.Layer)
```

## Parameters

- `width`: The new value for the specified edge width.
- `type`: The type of value being provided. This controls how `width` is interpreted.
- `layer`: The layer of the text block to modify.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](nstextblock/setwidth(_:type:for:rectedge:).md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](nstextblock/width(for:rectedge:).md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:rectedge:).md)
- [NSTextBlock.Layer](nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setwidth(_:type:for:))*