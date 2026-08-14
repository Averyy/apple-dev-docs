# NSParagraphStyle.TextTabType

**Framework**: AppKit  
**Kind**: enum

Constants that specify the type of tab stop.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum TextTabType
```

#### Overview

The following mappings define the conversions between text alignment in [`NSTextTab`](nstexttab.md) and tab stop types that [`NSTextTab`](nstexttab.md) defines:

| Alignment | Tab stop type |
| --- | --- |
| [`NSTextAlignment.left`](nstextalignment/left.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](nsparagraphstyle/texttabtype/lefttabstoptype.md) |
| [`NSTextAlignment.right`](nstextalignment/right.md) | [`NSParagraphStyle.TextTabType.rightTabStopType`](nsparagraphstyle/texttabtype/righttabstoptype.md) |
| [`NSTextAlignment.center`](nstextalignment/center.md) | [`NSParagraphStyle.TextTabType.centerTabStopType`](nsparagraphstyle/texttabtype/centertabstoptype.md) |
| [`NSTextAlignment.justified`](nstextalignment/justified.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](nsparagraphstyle/texttabtype/lefttabstoptype.md) |
| [`NSTextAlignment.natural`](nstextalignment/natural.md) | [`NSParagraphStyle.TextTabType.leftTabStopType`](nsparagraphstyle/texttabtype/lefttabstoptype.md), or [`NSParagraphStyle.TextTabType.rightTabStopType`](nsparagraphstyle/texttabtype/righttabstoptype.md), depending on the user setting. |
| [`NSTextAlignment.right`](nstextalignment/right.md) with a terminator | [`NSParagraphStyle.TextTabType.decimalTabStopType`](nsparagraphstyle/texttabtype/decimaltabstoptype.md) |

## Topics

### Constants
- [NSParagraphStyle.TextTabType.leftTabStopType](nsparagraphstyle/texttabtype/lefttabstoptype.md)
  A left-aligned tab stop.
- [NSParagraphStyle.TextTabType.rightTabStopType](nsparagraphstyle/texttabtype/righttabstoptype.md)
  A right-aligned tab stop.
- [NSParagraphStyle.TextTabType.centerTabStopType](nsparagraphstyle/texttabtype/centertabstoptype.md)
  A center-aligned tab stop.
- [NSParagraphStyle.TextTabType.decimalTabStopType](nsparagraphstyle/texttabtype/decimaltabstoptype.md)
  A tab stop that aligns columns of numbers to each number’s decimal point.
### Initializers
- [init?(rawValue: UInt)](nsparagraphstyle/texttabtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var tabStops: [NSTextTab]](nsparagraphstyle/tabstops.md)
  The text tab objects that represent the paragraph’s tab stops.
- [var defaultTabInterval: CGFloat](nsparagraphstyle/defaulttabinterval.md)
  The documentwide default tab interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/texttabtype)*