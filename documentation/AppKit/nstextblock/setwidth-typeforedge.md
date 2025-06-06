# setWidth(_:type:for:edge:)

**Framework**: AppKit  
**Kind**: method

Sets the width of a specified edge of a specified layer of the text block.

**Availability**:
- macOS ?+

## Declaration

```swift
func setWidth(_ val: CGFloat, type: NSTextBlock.ValueType, for layer: NSTextBlock.Layer, edge: NSRectEdge)
```

## Parameters

- `val`: The new value for the specified edge width.
- `type`: The type of value being provided. This controls how   is interpreted.
- `layer`: The layer of the text block to modify.
- `edge`: The edge of the layer to modify.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](nstextblock/width(for:edge:).md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [NSTextBlock.Layer](nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setwidth(_:type:for:edge:))*