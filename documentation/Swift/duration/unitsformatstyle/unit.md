# Duration.UnitsFormatStyle.Unit

**Framework**: Swift  
**Kind**: struct

A unit to use in formatting a duration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Unit
```

#### Overview

Supported units range from hours to nanoseconds. Use these with the `allowed` parameter of the [`Duration.UnitsFormatStyle`](duration/unitsformatstyle.md) initializers to specify which units to use in a formatted string.

## Topics

### Duration units
- [static var hours: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/hours.md)
  The hours unit, used for formatting a duration.
- [static var minutes: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/minutes.md)
  The minutes unit, used for formatting a duration.
- [static var seconds: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/seconds.md)
  The seconds unit, used for formatting a duration.
- [static var milliseconds: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/milliseconds.md)
  The milliseconds unit, used for formatting a duration.
- [static var microseconds: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/microseconds.md)
  The microseconds unit, used for formatting a duration.
- [static var nanoseconds: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/nanoseconds.md)
  The nanoseconds unit, used for formatting a duration.
### Type Properties
- [static var days: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/days.md)
  The unit for days. One day is always 86400 seconds.
- [static var weeks: Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit/weeks.md)
  The unit for weeks. One week is always 604800 seconds.

## Relationships

### Conforms To
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [var allowedUnits: Set<Duration.UnitsFormatStyle.Unit>](duration/unitsformatstyle/allowedunits.md)
  The units that may be included in the output string.
- [var maximumUnitCount: Int?](duration/unitsformatstyle/maximumunitcount.md)
  The maximum number of time units to include in the output string.
- [var valueLengthLimits: Range<Int>?](duration/unitsformatstyle/valuelengthlimits.md)
  The padding or truncating behavior of the unit value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unit)*