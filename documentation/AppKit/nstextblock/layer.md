# NSTextBlock.Layer

**Framework**: AppKit  
**Kind**: enum

The following constants specify values used by the properties and methods [`contentWidthValueType`](nstextblock/contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](nstextblock/setwidth(_:type:for:edge:).md), [`setWidth(_:type:for:)`](nstextblock/setwidth(_:type:for:).md), [`width(for:edge:)`](nstextblock/width(for:edge:).md), and [`widthValueType(for:edge:)`](nstextblock/widthvaluetype(for:edge:).md) to specify text block layer values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum Layer
```

## Topics

### Constants
- [NSTextBlock.Layer.padding](nstextblock/layer/padding.md)
  Padding of the text block: space surrounding the content area extending to the border.
- [NSTextBlock.Layer.border](nstextblock/layer/border.md)
  The border of the text block.
- [NSTextBlock.Layer.margin](nstextblock/layer/margin.md)
  Margin of the text block: space surrounding the border.
### Initializers
- [init?(rawValue: Int)](nstextblock/layer/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](nstextblock/setwidth(_:type:for:).md)
  Sets the width of all edges of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](nstextblock/setwidth(_:type:for:rectedge:).md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](nstextblock/width(for:rectedge:).md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](nstextblock/widthvaluetype(for:rectedge:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/layer)*