# Formatter.UnitStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Specifies the width of the unit, determining the textual representation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum UnitStyle
```

```c
enum NSFormattingUnitStyle : NSInteger;
```

#### Overview

The unit is represented in the shortest notation available. For example, for English, when formatting “3 pounds”: [`Formatter.UnitStyle.long`](./unitstyle/long.md) is “3 pounds”; [`Formatter.UnitStyle.medium`](./unitstyle/medium.md) is “3 lb”; [`Formatter.UnitStyle.short`](./unitstyle/short.md) is “3#”.

## Topics

### Constants
- [Formatter.UnitStyle.short](./unitstyle/short.md)
  Specifies a short unit style.
- [Formatter.UnitStyle.medium](./unitstyle/medium.md)
  Specifies a medium unit style.
- [Formatter.UnitStyle.long](./unitstyle/long.md)
  Specifies a long unit style.
### Initializers
- [init?(rawValue: Int)](./unitstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Formatter.Context](./context.md)
  The formatting context for a formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/unitstyle)*