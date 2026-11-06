# borderColor(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the border color of the specified text block edge.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
func borderColor(for edge: NSRectEdge) -> NSColor?
```

```objc
- (NSColor *) borderColorForEdge:(NSRectEdge) edge;
```

## Return Value

The border color of the text block edge `edge`.

## Parameters

- `edge`: The edge of the text block in question.

## See Also

### Deprecated
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, edge: NSRectEdge)](./setwidth%28_,type,for,edge%29.md)
  Sets the width of a specified edge of a specified layer of the text block.
- [func width(for: NSTextBlock.Layer, edge: NSRectEdge) -> CGFloat](./width%28for,edge%29.md)
  Returns the width of an edge of a specified layer of the text block.
- [func widthValueType(for: NSTextBlock.Layer, edge: NSRectEdge) -> NSTextBlock.ValueType](./widthvaluetype%28for,edge%29.md)
  Returns the value type of an edge of a specified layer of the text block.
- [func setBorderColor(NSColor?, for: NSRectEdge)](./setbordercolor%28_,for%29.md)
  Sets the border color of the specified edge of the text block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/bordercolor(for:)-273pl)*