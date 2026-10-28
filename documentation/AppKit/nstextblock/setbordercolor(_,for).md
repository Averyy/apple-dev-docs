# setBorderColor(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the border color of the specified edge of the text block.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
func setBorderColor(_ color: NSColor?, for edge: NSRectEdge)
```

```objc
- (void) setBorderColor:(NSColor *) color forEdge:(NSRectEdge) edge;
```

## Discussion

This setting has no visible effect unless the border width is larger than the default, which is 0.

## Parameters

- `color`: The new color.
- `edge`: The edge whose color is to be set.

## See Also

### Related Documentation
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./setwidth%28_,type,for%29.md)
  Sets the width of all edges of a specified layer of the text block.
### Deprecated
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](./setwidth%28_,type,for,edge%29.md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](./width%28for,edge%29.md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](./widthvaluetype%28for,edge%29.md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](./bordercolor%28for%29-273pl.md)
- [func borderColor(for: CGRectEdge) -> NSColor?](./bordercolor%28for%29-5m8cr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setbordercolor(_:for:))*