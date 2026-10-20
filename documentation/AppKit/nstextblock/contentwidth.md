# contentWidth

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The width of the text block.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var contentWidth: CGFloat { get }
```

```objc
@property (readonly) CGFloat contentWidth;
```

#### Discussion

This property interpreted according to the value type returned by [`contentWidthValueType`](./contentwidthvaluetype.md).

## See Also

### Working with dimensions of content
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](./setvalue%28_,type,for%29.md)
  Sets a dimension of the text block.
- [func value(for: NSTextBlock.Dimension) -> CGFloat](./value%28for%29.md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](./valuetype%28for%29.md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](./setcontentwidth%28_,type%29.md)
  Sets the width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](./contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](./dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md), [`value(for:)`](./value%28for%29.md), and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block dimensions.
- [NSTextBlock.ValueType](./valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md) and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/contentwidth)*