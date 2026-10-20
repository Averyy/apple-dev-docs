# NSParagraphStyle.TextTabType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the type of tab stop.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

> **Deprecated**: Use NSTextAlignment-based API.

## Declaration

```swift
enum TextTabType
```

```c
enum NSTextTabType : NSUInteger;
```

#### Overview

The following mappings define the conversions between text alignment in [`NSTextTab`](../nstexttab.md) and tab stop types that [`NSTextTab`](../nstexttab.md) defines:

| Alignment | Tab stop type |
| --- | --- |
| [`NSTextAlignment.left`](../nstextalignment/left.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](./texttabtype/lefttabstoptype.md) |
| [`NSTextAlignment.right`](../nstextalignment/right.md) | [`NSParagraphStyle.TextTabType.rightTabStopType`](./texttabtype/righttabstoptype.md) |
| [`NSTextAlignment.center`](../nstextalignment/center.md) | [`NSParagraphStyle.TextTabType.centerTabStopType`](./texttabtype/centertabstoptype.md) |
| [`NSTextAlignment.justified`](../nstextalignment/justified.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](./texttabtype/lefttabstoptype.md) |
| [`NSTextAlignment.natural`](../nstextalignment/natural.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](./texttabtype/lefttabstoptype.md), or [`NSParagraphStyle.TextTabType.rightTabStopType`](./texttabtype/righttabstoptype.md), depending on the user setting. |
| [`NSTextAlignment.right`](../nstextalignment/right.md) with a terminator | [`NSParagraphStyle.TextTabType.decimalTabStopType`](./texttabtype/decimaltabstoptype.md) |

## Topics

### Constants
- [NSParagraphStyle.TextTabType.leftTabStopType](./texttabtype/lefttabstoptype.md)
  A left-aligned tab stop.
- [NSParagraphStyle.TextTabType.rightTabStopType](./texttabtype/righttabstoptype.md)
  A right-aligned tab stop.
- [NSParagraphStyle.TextTabType.centerTabStopType](./texttabtype/centertabstoptype.md)
  A center-aligned tab stop.
- [NSParagraphStyle.TextTabType.decimalTabStopType](./texttabtype/decimaltabstoptype.md)
  A tab stop that aligns columns of numbers to each number’s decimal point.
### Initializers
- [init?(rawValue: UInt)](./texttabtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing tab information
- [var tabStops: [NSTextTab]](./tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](./defaulttabinterval.md)
  The documentwide default tab interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/texttabtype)*