# Date.FormatStyle.Symbol.Hour.AMPMStyle

**Framework**: Foundation  
**Kind**: struct

The format style of the string representation of the day period, before or after noon, in a date.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AMPMStyle
```

#### Overview

Possible values for this style are: [`omitted`](date/formatstyle/symbol/hour/ampmstyle/omitted.md), [`narrow`](date/formatstyle/symbol/hour/ampmstyle/narrow.md), [`abbreviated`](date/formatstyle/symbol/hour/ampmstyle/abbreviated.md), and [`wide`](date/formatstyle/symbol/hour/ampmstyle/wide.md).

## Topics

### Creating AMPM Styles
- [static let abbreviated: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/abbreviated.md)
  A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [static let narrow: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/narrow.md)
  A type that specifies the narrow day period if the locale prefers using day period with hour.
- [static let omitted: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/omitted.md)
  A type that hides the day period marker.
- [static let wide: Date.FormatStyle.Symbol.Hour.AMPMStyle](date/formatstyle/symbol/hour/ampmstyle/wide.md)
  A type that represents the wide day period if the locale prefers using day period with hour.
### Comparing AMPM Styles
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle)*