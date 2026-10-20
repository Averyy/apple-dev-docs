# widthValueType(for:edge:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value type of an edge of a specified layer of the text block.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
func widthValueType(for layer: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType
```

```objc
- (NSTextBlockValueType) widthValueTypeForLayer:(NSTextBlockLayer) layer edge:(NSRectEdge) edge;
```

#### Return Value

The value type of the `edge` of `layer`. This determines how the value for this `edge` of `layer` should be interpreted.

## Parameters

- `layer`: The layer to examine.
- `edge`: The edge of the layer to examine.

## See Also

### Deprecated
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](./setwidth%28_,type,for,edge%29.md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](./width%28for,edge%29.md)
  Returns the width of an edge of a specified layer of the text block.
- [func borderColor(for: NSRectEdge) -> NSColor?](./bordercolor%28for%29-273pl.md)
- [func setBorderColor(NSColor?, for: NSRectEdge)](./setbordercolor%28_,for%29.md)
  Sets the border color of the specified edge of the text block.
- [func borderColor(for: CGRectEdge) -> NSColor?](./bordercolor%28for%29-5m8cr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/widthvaluetype(for:edge:))*