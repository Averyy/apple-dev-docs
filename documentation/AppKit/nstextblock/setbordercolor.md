# setBorderColor(_:)

**Framework**: AppKit  
**Kind**: method

Sets the color of all borders of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setBorderColor(_ color: NSColor?)
```

#### Discussion

This setting has no visible effect unless the border width is larger than the default, which is 0.

## Parameters

- `color`: The new color.

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [var backgroundColor: NSColor?](nstextblock/backgroundcolor.md)
  The background color of the text block.
- [func setBorderColor(NSColor?, rectEdge: CGRectEdge)](nstextblock/setbordercolor(_:rectedge:).md)
- [func borderColor(for: CGRectEdge) -> NSColor?](nstextblock/bordercolor(for:)-5m8cr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setbordercolor(_:))*