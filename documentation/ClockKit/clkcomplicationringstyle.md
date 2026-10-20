# CLKComplicationRingStyle

**Framework**: ClockKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the appearance of a progress ring.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
enum CLKComplicationRingStyle
```

```c
enum CLKComplicationRingStyle : NSInteger;
```

## Topics

### Constants
- [CLKComplicationRingStyle.closed](./clkcomplicationringstyle/closed.md)
  A ring in which the values increase clockwise, starting at 12 o’clock, to create a closed circle.
- [CLKComplicationRingStyle.open](./clkcomplicationringstyle/open.md)
  A ring in which the values increase clockwise, starting in the lower-left corner, leaving an opening at the bottom of the circle.
### Initializers
- [init?(rawValue: Int)](./clkcomplicationringstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying Styles
- [enum CLKComplicationColumnAlignment](./clkcomplicationcolumnalignment.md)
  Constants indicating the alignment of text in columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationringstyle)*