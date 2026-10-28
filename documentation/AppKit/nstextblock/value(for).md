# value(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of the specified text block dimension.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func value(for dimension: NSTextBlock.Dimension) -> CGFloat
```

```objc
- (CGFloat) valueForDimension:(NSTextBlockDimension) dimension;
```

## Return Value

The value for the specified dimension. This value should be interpreted according to the value type returned by [`valueType(for:)`](./valuetype%28for%29.md).

## See Also

### Working with dimensions of content
- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](./setvalue%28_,type,for%29.md)
  Sets a dimension of the text block.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](./valuetype%28for%29.md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](./setcontentwidth%28_,type%29.md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](./contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](./contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](./dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md), [`value(for:)`](./value%28for%29.md), and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block dimensions.
- [NSTextBlock.ValueType](./valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md) and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/value(for:))*