# widthValueType(for:rectEdge:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
func widthValueType(for layer: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType
```

```objc
- (NSTextBlockValueType) widthValueTypeForLayer:(NSTextBlockLayer) layer rectEdge:(CGRectEdge) rectEdge;
```

## See Also

### Getting and setting margins, borders, and padding
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./setwidth%28_,type,for%29.md)
  Sets the width of all edges of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](./setwidth%28_,type,for,rectedge%29.md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](./width%28for,rectedge%29.md)
- [NSTextBlock.Layer](./layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](./contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](./setwidth%28_,type,for,edge%29.md), [`setWidth(_:type:for:)`](./setwidth%28_,type,for%29.md), [`width(for:edge:)`](./width%28for,edge%29.md), and [`widthValueType(for:edge:)`](./widthvaluetype%28for,edge%29.md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/widthvaluetype(for:rectedge:))*