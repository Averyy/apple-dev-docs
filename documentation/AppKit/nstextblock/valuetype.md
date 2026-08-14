# NSTextBlock.ValueType

**Framework**: AppKit  
**Kind**: enum

The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md) and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block value types.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum ValueType
```

## Topics

### Constants
- [static var absoluteValueType: NSTextBlock.ValueType](nstextblock/valuetype/absolutevaluetype.md)
  Absolute value in points.
- [static var percentageValueType: NSTextBlock.ValueType](nstextblock/valuetype/percentagevaluetype.md)
  Percentage value (out of 100).
### Enumeration Cases
- [NSTextBlock.ValueType.absolute](nstextblock/valuetype/absolute.md)
- [NSTextBlock.ValueType.percentage](nstextblock/valuetype/percentage.md)
### Initializers
- [init?(rawValue: Int)](nstextblock/valuetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func setValue(CGFloat, type: NSTextBlock.ValueType, for: NSTextBlock.Dimension)](nstextblock/setvalue(_:type:for:).md)
  Sets a dimension of the text block.
- [func value(for: NSTextBlock.Dimension) -> CGFloat](nstextblock/value(for:).md)
  Returns the value of the specified text block dimension.
- [func valueType(for: NSTextBlock.Dimension) -> NSTextBlock.ValueType](nstextblock/valuetype(for:).md)
  Returns the value type of the specified text block dimension.
- [func setContentWidth(CGFloat, type: NSTextBlock.ValueType)](nstextblock/setcontentwidth(_:type:).md)
  Sets the width of the text block.
- [var contentWidth: CGFloat](nstextblock/contentwidth.md)
  The width of the text block.
- [var contentWidthValueType: NSTextBlock.ValueType](nstextblock/contentwidthvaluetype.md)
  The type of value stored for the text block width.
- [NSTextBlock.Dimension](nstextblock/dimension.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md), [`value(for:)`](nstextblock/value(for:).md), and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/valuetype)*