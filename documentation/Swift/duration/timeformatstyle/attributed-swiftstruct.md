# Duration.TimeFormatStyle.Attributed

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

Apply the [`Duration.TimeFormatStyle.Attributed`](duration/timeformatstyle/attributed-swift.struct.md) property to a configured [`Duration.TimeFormatStyle`](duration/timeformatstyle.md) to produce an instance of this style. You can then format a duration with this style to create a formatted [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString). The formatted attributed string contains instances of [`AttributeScopes.FoundationAttributes.DateFieldAttribute`](https://developer.apple.com/documentation/Foundation/AttributeScopes/FoundationAttributes/DateFieldAttribute) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.TimeFormatStyle(pattern: .hourMinuteSecond).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1:10:32` contains the following runs:

| Run | Attributes |
| --- | --- |
| `1` | `Foundation.DurationFormatAttribute = hours` |
| `:` | None |
| `10` | `Foundation.DurationFormatAttribute = minutes` |
| `:` | None |
| `32` | `Foundation.DurationFormatAttribute = seconds` |

## Topics

### Formatting a duration
- [func format(Duration) -> AttributedString](duration/timeformatstyle/attributed-swift.struct/format(_:).md)
  Creates a locale-aware attributed string representation from a duration value.
### Working with locales
- [func locale(Locale) -> Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct/locale(_:).md)
  Modifies the format style to use the specified locale.
### Instance Methods
- [func grouping(NumberFormatStyleConfiguration.Grouping) -> Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct/grouping(_:).md)
  Returns a modified style that applies the given `grouping` rule to the highest field in the pattern.
### Subscripts
- [subscript<T>(dynamicMember _: WritableKeyPath<Duration.TimeFormatStyle, T>) -> T](duration/timeformatstyle/attributed-swift.struct/subscript(dynamicmember:)-32lo0.md)
- [subscript<T>(dynamicMember _: KeyPath<Duration.TimeFormatStyle, T>) -> T](duration/timeformatstyle/attributed-swift.struct/subscript(dynamicmember:)-8cksi.md)

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

- [var attributed: Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.property.md)
  A property that formats the duration as an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle/attributed-swift.struct)*