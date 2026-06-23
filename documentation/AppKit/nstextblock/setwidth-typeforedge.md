# setWidth(_:type:for:edge:)

**Framework**: AppKit  
**Kind**: method

Sets the width of a specified edge of a specified layer of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setWidth(_ val: CGFloat, type: NSTextBlock.ValueType, for layer: NSTextBlock.Layer, edge: NSRectEdge)
```

## Parameters

- `val`: The new value for the specified edge width.
- `type`: The type of value being provided. This controls how `val` is interpreted.
- `layer`: The layer of the text block to modify.
- `edge`: The edge of the layer to modify.

## See Also

- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](nstextblock/width(for:edge:).md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](nstextblock/bordercolor(for:)-273pl.md)
- [func setBorderColor(NSColor?, for: NSRectEdge)](nstextblock/setbordercolor(_:for:).md)
  Sets the border color of the specified edge of the text block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setwidth(_:type:for:edge:))*