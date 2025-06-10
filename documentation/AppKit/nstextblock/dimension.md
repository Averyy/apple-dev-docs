# NSTextBlock.Dimension

**Framework**: AppKit  
**Kind**: enum

The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md), [`value(for:)`](nstextblock/value(for:).md), and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block dimensions.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Dimension
```

## Topics

### Constants
- [NSTextBlock.Dimension.width](nstextblock/dimension/width.md)
  Width of the text block.
- [NSTextBlock.Dimension.minimumWidth](nstextblock/dimension/minimumwidth.md)
  Minimum width of the text block.
- [NSTextBlock.Dimension.maximumWidth](nstextblock/dimension/maximumwidth.md)
  Maximum width of the text block.
- [NSTextBlock.Dimension.height](nstextblock/dimension/height.md)
  Height of the text block.
- [NSTextBlock.Dimension.minimumHeight](nstextblock/dimension/minimumheight.md)
  Minimum height of the text block.
- [NSTextBlock.Dimension.maximumHeight](nstextblock/dimension/maximumheight.md)
  Maximum height of the text block.
### Initializers
- [init?(rawValue: UInt)](nstextblock/dimension/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [NSTextBlock.ValueType](nstextblock/valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](nstextblock/setvalue(_:type:for:).md) and [`valueType(for:)`](nstextblock/valuetype(for:).md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/dimension)*