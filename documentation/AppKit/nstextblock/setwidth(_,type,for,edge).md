# setWidth(_:type:for:edge:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the width of a specified edge of a specified layer of the text block.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
func setWidth(_ val: CGFloat, type: NSTextBlock.ValueType, for layer: NSTextBlock.Layer, edge: NSRectEdge)
```

```objc
- (void) setWidth:(CGFloat) val type:(NSTextBlockValueType) type forLayer:(NSTextBlockLayer) layer edge:(NSRectEdge) edge;
```

## Parameters

- `val`: The new value for the specified edge width.
- `type`: The type of value being provided. This controls how `val` is interpreted.
- `layer`: The layer of the text block to modify.
- `edge`: The edge of the layer to modify.

## See Also

### Deprecated
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](./width%28for,edge%29.md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](./widthvaluetype%28for,edge%29.md)
  Returns the value type of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](./bordercolor%28for%29-273pl.md)
- [func setBorderColor(NSColor?, for: NSRectEdge)](./setbordercolor%28_,for%29.md)
  Sets the border color of the specified edge of the text block.
- [func borderColor(for: CGRectEdge) -> NSColor?](./bordercolor%28for%29-5m8cr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setwidth(_:type:for:edge:))*