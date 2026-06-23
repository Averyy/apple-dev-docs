# width(for:edge:)

**Framework**: AppKit  
**Kind**: method

Returns the width of an edge of a specified layer of the text block.

**Availability**:
- macOS 10.0+

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
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](nstextblock/bordercolor(for:)-273pl.md)
- [func setBorderColor(NSColor?, for: NSRectEdge)](nstextblock/setbordercolor(_:for:).md)
  Sets the border color of the specified edge of the text block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/width(for:edge:))*