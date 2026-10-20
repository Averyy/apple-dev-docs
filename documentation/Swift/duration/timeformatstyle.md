# Duration.TimeFormatStyle

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

Create a `TimeFormatStyle` by providing a [`Duration.TimeFormatStyle.Pattern`](./timeformatstyle/pattern-swift.struct.md) and an optional locale. The pattern specifies which units (hours, minutes, and seconds) to include in the formatted string, with optional configuration of the units. Then create a formatted string by calling [`formatted(_:)`](./formatted%28_%29.md) on a duration, passing the style, or [`format(_:)`](./timeformatstyle/format%28_%29.md) on the style, passing a duration. You can also use the style’s [`attributed`](./timeformatstyle/attributed-swift.property.md) property to create a style that produces [`AttributedString`](../../Foundation/attributedstring.md) instances, which contains attributes that indicate the unit value of formatted runs of the string.

In situations that expect a [`Duration.TimeFormatStyle`](./timeformatstyle.md), such as [`formatted(_:)`](./formatted%28_%29.md), you can use the convenience function `Swift/Duration/TimeFormatStyle/time(pattern:)` to create a [`Duration.TimeFormatStyle`](./timeformatstyle.md), rather than using the full initializer.

If you want to reuse a style to format many durations, call [`format(_:)`](./timeformatstyle/format%28_%29.md) on the style, passing in a new duration each time.

The following example creates `duration` to represent 1 hour, 10 minutes, 32 seconds, and 400 milliseconds. It then creates a [`Duration.TimeFormatStyle`](./timeformatstyle.md) to show hours, minutes, and seconds, padding the hours part to two digits and limiting the fractional seconds to two digits. When used with the [`formatted(_:)`](./formatted%28_%29.md) method, the resulting string is `01:10:32.40`.

```swift
let duration = Duration.seconds(70 * 60 + 32) + Duration.milliseconds(400)
let format = duration.formatted(
    .time(pattern: .hourMinuteSecond(padHourToLength: 2,
                                     fractionalSecondsLength: 2)))
// format == "01:10:32.40"
```

## Topics

### Creating a time format style
- [init(pattern: Duration.TimeFormatStyle.Pattern, locale: Locale)](./timeformatstyle/init%28pattern,locale%29.md)
  Creates a time format style using the provided pattern and optional locale.
- [Duration.TimeFormatStyle.Pattern](./timeformatstyle/pattern-swift.struct.md)
  The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.
### Formatting a duration
- [func format(Duration) -> String](./timeformatstyle/format%28_%29.md)
  Creates a locale-aware string representation from a duration value.
### Formatting a duration as an attributed string
- [var attributed: Duration.TimeFormatStyle.Attributed](./timeformatstyle/attributed-swift.property.md)
  A property that formats the duration as an attributed string.
- [Duration.TimeFormatStyle.Attributed](./timeformatstyle/attributed-swift.struct.md)
  A format style that formats durations as attributed strings.
### Using a style pattern
- [var pattern: Duration.TimeFormatStyle.Pattern](./timeformatstyle/pattern-swift.property.md)
  The pattern to display a Duration with.
- [Duration.TimeFormatStyle.Pattern](./timeformatstyle/pattern-swift.struct.md)
  The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.
### Working with locales
- [var locale: Locale](./timeformatstyle/locale.md)
  The locale to use when formatting the duration.
- [func locale(Locale) -> Duration.TimeFormatStyle](./timeformatstyle/locale%28_%29.md)
  Modifies the format style to use the specified locale.
### Instance Properties
- [var grouping: NumberFormatStyleConfiguration.Grouping](./timeformatstyle/grouping.md)
  The `grouping` rule applied to high number values on the largest field in the pattern.
### Instance Methods
- [func grouping(NumberFormatStyleConfiguration.Grouping) -> Duration.TimeFormatStyle](./timeformatstyle/grouping%28_%29.md)
  Returns a modified style that applies the given `grouping` rule to the highest field in the pattern.

## Relationships

### Conforms To
- [Copyable](../copyable.md)
- [Decodable](../decodable.md)
- [DiscreteFormatStyle](../../Foundation/discreteformatstyle.md)
- [Encodable](../encodable.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [FormatStyle](../../Foundation/formatstyle.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Formatting a duration
- [func formatted() -> String](./formatted%28%29.md)
  Formats the string using a localized hour-minute-second time pattern.
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
  Formats the duration, using the provided format style.
- [Duration.UnitsFormatStyle](./unitsformatstyle.md)
  A format style that shows durations with localized labeled components


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle)*