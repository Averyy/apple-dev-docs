# setWidth(_:type:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the width of all edges of a specified layer of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setWidth(_ width: CGFloat, type: NSTextBlock.ValueType, for layer: NSTextBlock.Layer)
```

```objc
- (void) setWidth:(CGFloat) width type:(NSTextBlockValueType) type forLayer:(NSTextBlockLayer) layer;
```

## Parameters

- `width`: The new value for the specified edge width.
- `type`: The type of value being provided. This controls how `width` is interpreted.
- `layer`: The layer of the text block to modify.

## See Also

### Getting and setting margins, borders, and padding
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](./setwidth%28_,type,for,rectedge%29.md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](./width%28for,rectedge%29.md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](./widthvaluetype%28for,rectedge%29.md)
- [NSTextBlock.Layer](./layer.md)
  The following constants specify values used by the properties and methods [`contentWidthValueType`](./contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](./setwidth%28_,type,for,edge%29.md), [`setWidth(_:type:for:)`](./setwidth%28_,type,for%29.md), [`width(for:edge:)`](./width%28for,edge%29.md), and [`widthValueType(for:edge:)`](./widthvaluetype%28for,edge%29.md) to specify text block layer values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/setwidth(_:type:for:))*