# NSTextBlock.Layer

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The following constants specify values used by the properties and methods [`contentWidthValueType`](./contentwidthvaluetype.md), [`setWidth(_:type:for:edge:)`](./setwidth%28_,type,for,edge%29.md), [`setWidth(_:type:for:)`](./setwidth%28_,type,for%29.md), [`width(for:edge:)`](./width%28for,edge%29.md), and [`widthValueType(for:edge:)`](./widthvaluetype%28for,edge%29.md) to specify text block layer values.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum Layer
```

```c
enum NSTextBlockLayer : NSInteger;
```

## Topics

### Constants
- [NSTextBlock.Layer.padding](./layer/padding.md)
  Padding of the text block: space surrounding the content area extending to the border.
- [NSTextBlock.Layer.border](./layer/border.md)
  The border of the text block.
- [NSTextBlock.Layer.margin](./layer/margin.md)
  Margin of the text block: space surrounding the border.
### Initializers
- [init?(rawValue: Int)](./layer/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting and setting margins, borders, and padding
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer)](./setwidth%28_,type,for%29.md)
  Sets the width of all edges of a specified layer of the text block.
- [func setWidth(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Layer, rectEdge: CGRectEdge)](./setwidth%28_,type,for,rectedge%29.md)
- [func width(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> CGFloat](./width%28for,rectedge%29.md)
- [func widthValueType(for: NSTextBlock.Layer, rectEdge: CGRectEdge) -> NSTextBlock.ValueType](./widthvaluetype%28for,rectedge%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/layer)*