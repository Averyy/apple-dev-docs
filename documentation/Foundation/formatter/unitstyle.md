# Formatter.UnitStyle

**Framework**: Foundation  
**Kind**: enum

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

#### Overview

The unit is represented in the shortest notation available. For example, for English, when formatting “3 pounds”: [`Formatter.UnitStyle.long`](formatter/unitstyle/long.md) is “3 pounds”; [`Formatter.UnitStyle.medium`](formatter/unitstyle/medium.md) is “3 lb”; [`Formatter.UnitStyle.short`](formatter/unitstyle/short.md) is “3#”.

## Topics

### Constants
- [Formatter.UnitStyle.short](formatter/unitstyle/short.md)
  Specifies a short unit style.
- [Formatter.UnitStyle.medium](formatter/unitstyle/medium.md)
  Specifies a medium unit style.
- [Formatter.UnitStyle.long](formatter/unitstyle/long.md)
  Specifies a long unit style.
- [Formatter.UnitStyle.short](formatter/unitstyle/short.md)
  Specifies a short unit style.
- [Formatter.UnitStyle.medium](formatter/unitstyle/medium.md)
  Specifies a medium unit style.
- [Formatter.UnitStyle.long](formatter/unitstyle/long.md)
  Specifies a long unit style.
### Initializers
- [init?(rawValue: Int)](formatter/unitstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Formatter.Context](formatter/context.md)
  The formatting context for a formatter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/unitstyle)*