# Duration.TimeFormatStyle

**Framework**: Swift  
**Kind**: struct

A format style that shows durations in a compact, localized format with separators.

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
struct TimeFormatStyle
```

#### Overview

This style produces formatted strings that uses separators between components, like “2:03”

Create a `TimeFormatStyle` by providing a [`Duration.TimeFormatStyle.Pattern`](duration/timeformatstyle/pattern-swift.struct.md) and an optional locale. The pattern specifies which units (hours, minutes, and seconds) to include in the formatted string, with optional configuration of the units. Then create a formatted string by calling [`formatted(_:)`](duration/formatted(_:).md) on a duration, passing the style, or [`format(_:)`](duration/timeformatstyle/format(_:).md) on the style, passing a duration. You can also use the style’s [`attributed`](duration/timeformatstyle/attributed-swift.property.md) property to create a style that produces [`AttributedString`](https://developer.apple.com/documentation/Foundation/AttributedString) instances, which contains attributes that indicate the unit value of formatted runs of the string.

In situations that expect a [`Duration.TimeFormatStyle`](duration/timeformatstyle.md), such as [`formatted(_:)`](duration/formatted(_:).md), you can use the convenience function `Swift/Duration/TimeFormatStyle/time(pattern:)` to create a [`Duration.TimeFormatStyle`](duration/timeformatstyle.md), rather than using the full initializer.

If you want to reuse a style to format many durations, call [`format(_:)`](duration/timeformatstyle/format(_:).md) on the style, passing in a new duration each time.

The following example creates `duration` to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [`Duration.TimeFormatStyle`](duration/timeformatstyle.md) to show hours, minutes, and seconds, padding the hours part to two digits and limiting the fractional seconds to two digits. When used with the [`formatted(_:)`](duration/formatted(_:).md) method, the resulting string is `01:10:32.40`.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration.formatted(
    .time(pattern: .hourMinuteSecond(padHourToLength: 2,
                                     fractionalSecondsLength: 2)))
// format == "01:10:32.40"
```

## Topics

### Creating a time format style
- [init(pattern: Duration.TimeFormatStyle.Pattern, locale: Locale)](duration/timeformatstyle/init(pattern:locale:).md)
  Creates a time format style using the provided pattern and optional locale.
- [Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct.md)
  The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.
### Formatting a duration
- [func format(Duration) -> String](duration/timeformatstyle/format(_:).md)
  Creates a locale-aware string representation from a duration value.
### Formatting a duration as an attributed string
- [var attributed: Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.property.md)
  A property that formats the duration as an attributed string.
- [Duration.TimeFormatStyle.Attributed](duration/timeformatstyle/attributed-swift.struct.md)
  A format style that formats durations as attributed strings.
### Using a style pattern
- [var pattern: Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.property.md)
  The pattern to display a Duration with.
- [Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct.md)
  The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.
### Working with locales
- [var locale: Locale](duration/timeformatstyle/locale.md)
  The locale to use when formatting the duration.
- [func locale(Locale) -> Duration.TimeFormatStyle](duration/timeformatstyle/locale(_:).md)
  Modifies the format style to use the specified locale.
### Instance Properties
- [var grouping: NumberFormatStyleConfiguration.Grouping](duration/timeformatstyle/grouping.md)
  The `grouping` rule applied to high number values on the largest field in the pattern.
### Instance Methods
- [func grouping(NumberFormatStyleConfiguration.Grouping) -> Duration.TimeFormatStyle](duration/timeformatstyle/grouping(_:).md)
  Returns a modified style that applies the given `grouping` rule to the highest field in the pattern.

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

- [func formatted() -> String](duration/formatted.md)
  Formats the string using a localized hour-minute-second time pattern.
- [func formatted<S>(S) -> S.FormatOutput](duration/formatted(_:).md)
  Formats the duration, using the provided format style.
- [Duration.UnitsFormatStyle](duration/unitsformatstyle.md)
  A format style that shows durations with localized labeled components


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle)*