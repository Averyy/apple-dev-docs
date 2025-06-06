# widthValueType(for:edge:)

**Framework**: AppKit  
**Kind**: method

Returns the value type of an edge of a specified layer of the text block.

**Availability**:
- macOS ?+

## Declaration

```swift
func widthValueType(for layer: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType
```

#### Return Value

The value type of the `edge` of `layer`. This determines how the value for this `edge` of `layer` should be interpreted.

## Parameters

- `layer`: The layer to examine.
- `edge`: The edge of the layer to examine.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](nstextblock/setwidth(_:type:for:edge:).md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](nstextblock/width(for:edge:).md)
  Returns the width of an edge of a specified layer of the text block.
- [NSTextBlock.Layer](nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/widthvaluetype(for:edge:))*