# width(for:edge:)

**Framework**: AppKit  
**Kind**: method

Returns the width of an edge of a specified layer of the text block.

**Availability**:
- macOS ?+

## Declaration

```swift
func width(for layer: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat
```

#### Return Value

The width of the `edge` of `layer`. This value must be interpreted according to the value type returned by [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md).

## Parameters

- `layer`: The layer to examine.
- `edge`: The edge of the layer to examine.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](nstextblock/setwidth(_:type:for:edge:).md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [NSTextBlock.Layer](nstextblock/layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/width(for:edge:))*