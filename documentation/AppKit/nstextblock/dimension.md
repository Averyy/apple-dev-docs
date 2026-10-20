# NSTextBlock.Dimension

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md), [`value(for:)`](./value%28for%29.md), and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block dimensions.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum Dimension
```

```c
enum NSTextBlockDimension : NSInteger;
```

## Topics

### Constants
- [NSTextBlock.Dimension.width](./dimension/width.md)
  Width of the text block.
- [NSTextBlock.Dimension.minimumWidth](./dimension/minimumwidth.md)
  Minimum width of the text block.
- [NSTextBlock.Dimension.maximumWidth](./dimension/maximumwidth.md)
  Maximum width of the text block.
- [NSTextBlock.Dimension.height](./dimension/height.md)
  Height of the text block.
- [NSTextBlock.Dimension.minimumHeight](./dimension/minimumheight.md)
  Minimum height of the text block.
- [NSTextBlock.Dimension.maximumHeight](./dimension/maximumheight.md)
  Maximum height of the text block.
### Initializers
- [init?(rawValue: Int)](./dimension/init%28rawvalue%29.md)

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
- [NSTextBlock.ValueType](./valuetype.md)
  The following constants specify values used by the methods [`setValue(_:type:for:)`](./setvalue%28_,type,for%29.md) and [`valueType(for:)`](./valuetype%28for%29.md) to specify text block value types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextblock/dimension)*