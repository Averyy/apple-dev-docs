# NSTextBlock.ValueType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md) and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block value types.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum ValueType
```

```c
enum NSTextBlockValueType : NSInteger;
```

## Topics

### Constants
- [static var absoluteValueType: NSTextBlock.ValueType](./valuetype/absolutevaluetype.md)
  Absolute value in points.
- [static var percentageValueType: NSTextBlock.ValueType](./valuetype/percentagevaluetype.md)
  Percentage value (out of 100).
### Enumeration Cases
- [NSTextBlock.ValueType.absolute](./valuetype/absolute.md)
- [NSTextBlock.ValueType.percentage](./valuetype/percentage.md)
### Initializers
- [init?(rawValue: Int)](./valuetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var contentWidth: CGFloat](./contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](./contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](./dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md), [`value(for:)`](./value%28for%29.md), and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/valuetype)*