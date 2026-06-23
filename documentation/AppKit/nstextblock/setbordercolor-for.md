# setBorderColor(_:for:)

**Framework**: AppKit  
**Kind**: method

Sets the border color of the specified edge of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setBorderColor(_ color: NSColor?, for edge: NSRectEdge)
```

#### Discussion

This setting has no visible effect unless the border width is larger than the default, which is 0.

## Parameters

- `color`: The new color.
- `edge`: The edge whose color is to be set.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](nstextblock/setwidth(_:type:for:edge:).md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](nstextblock/width(for:edge:).md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:edge:).md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](nstextblock/bordercolor(for:)-273pl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setbordercolor(_:for:))*