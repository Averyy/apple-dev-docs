# Duration.UnitsFormatStyle.Attributed

**Framework**: Swift  
**Kind**: struct

A format style that formats durations as attributed strings.

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
@dynamicMemberLookup
struct Attributed
```

#### Overview

Apply the [`attributed`](duration/unitsformatstyle/attributed-swift.property.md) property to a configured [`Duration.UnitsFormatStyle`](duration/unitsformatstyle.md) to produce an instance of this style. You can then format a duration with this style to create a formatted   [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString). The formatted attributed string contains instances of [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes/DateFieldAttribute) and [`AttributeScopes.FoundationAttributes.MeasurementAttribute`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes/MeasurementAttribute) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.UnitsFormatStyle(allowedUnits: [.hours, .minutes, .seconds],
                                      width: .abbreviated).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1 hr, 10 min, 32 sec` contains the following runs:

| Run | Attributes |
| --- | --- |
| `1` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = hours` |
| (space) | `Foundation.DurationFormatAttribute = hours` |
| `hr` | `Foundation.DurationFormatAttribute = hours`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `10` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = minutes` |
| (space) | `Foundation.DurationFormatAttribute = minutes` |
| `min` | `Foundation.DurationFormatAttribute = minutes`, `Foundation.MeasurementAttribute = unit` |
| `,  ` | None |
| `32` | `Foundation.MeasurementAttribute = value`, `Foundation.DurationFormatAttribute = seconds` |
| (space) | `Foundation.DurationFormatAttribute = seconds` |
| `sec` | `Foundation.DurationFormatAttribute = seconds`, `Foundation.MeasurementAttribute = unit` |

## Topics

### Formatting a duration
- [func format(Duration) -> AttributedString](duration/unitsformatstyle/attributed-swift.struct/format(_:).md)
  Creates a locale-aware attributed string representation from a duration value.
### Working with locales
- [func locale(Locale) -> Duration.UnitsFormatStyle.Attributed](duration/unitsformatstyle/attributed-swift.struct/locale(_:).md)
  Modifies the format style to use the specified locale.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<Duration.UnitsFormatStyle, T>) -> T](duration/unitsformatstyle/attributed-swift.struct/subscript(dynamicmember:)-57dpz.md)
- [subscript<T>(dynamicMember _: WritableKeyPath<Duration.UnitsFormatStyle, T>) -> T](duration/unitsformatstyle/attributed-swift.struct/subscript(dynamicmember:)-65x7d.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Decodable](decodable.md)
- [DiscreteFormatStyle](../Foundation/DiscreteFormatStyle.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [FormatStyle](../Foundation/FormatStyle.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [var attributed: Duration.UnitsFormatStyle.Attributed](duration/unitsformatstyle/attributed-swift.property.md)
  A property that formats the duration as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/attributed-swift.struct)*