# formatted(date:time:)

**Framework**: Foundation  
**Kind**: method

Generates a locale-aware string representation of a date using specified date and time format styles.

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
func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String
```

#### Return Value

A string, formatted according to the specified date and time styles.

#### Discussion

When displaying a date to a user, use the convenient [`formatted(date:time:)`](date/formatted(date:time:).md) instance method to customize the string representation of the date. Set the date and time styles of the date format style separately, according to your particular needs.

For example, to create a string with a full date and no time representation, set the [`Date.FormatStyle.DateStyle`](date/formatstyle/datestyle.md) to [`complete`](date/formatstyle/datestyle/complete.md) and the [`Date.FormatStyle.TimeStyle`](date/formatstyle/timestyle.md) to [`omitted`](date/formatstyle/timestyle/omitted.md). Conversely, to create a string representing only the time, set the date style to [`omitted`](date/formatstyle/datestyle/omitted.md) and the time style to [`complete`](date/formatstyle/timestyle/complete.md).

```swift
let birthday = Date()

birthday.formatted(date: .complete, time: .omitted) // Sunday, January 17, 2021
birthday.formatted(date: .omitted, time: .complete) // 4:03:12 PM CST
```

You can create string representations of a [`Date`](date.md) instance with several levels of brevity using a variety of preset date and time styles. This example shows date styles of [`long`](date/formatstyle/datestyle/long.md), [`abbreviated`](date/formatstyle/datestyle/abbreviated.md), and [`numeric`](date/formatstyle/datestyle/numeric.md), and time styles of [`shortened`](date/formatstyle/timestyle/shortened.md), [`standard`](date/formatstyle/timestyle/standard.md), and [`complete`](date/formatstyle/timestyle/complete.md).

```swift
let birthday = Date()

birthday.formatted(date: .long, time: .shortened) // January 17, 2021, 4:03 PM
birthday.formatted(date: .abbreviated, time: .standard) // Jan 17, 2021, 4:03:12 PM
birthday.formatted(date: .numeric, time: .complete) // 1/17/2021, 4:03:12 PM CST

birthday.formatted() // Jan 17, 2021, 4:03 PM
```

The default date style is [`abbreviated`](date/formatstyle/datestyle/abbreviated.md) and the default time style is [`shortened`](date/formatstyle/timestyle/shortened.md).

For the default date formatting, use the [`formatted()`](date/formatted().md) method. To customize the formatted measurement string, use the [`formatted(_:)`](date/formatted(_:).md) method and include a `Date.FormatStyle`.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `date`: The date format style to apply to the date.
- `time`: The time format style to apply to the date.

## See Also

- [func formatted() -> String](date/formatted.md)
  Generates a locale-aware string representation of a date using the default date format style.
- [func formatted<F>(F) -> F.FormatOutput](date/formatted(_:).md)
  Generates a locale-aware string representation of a date using the specified date format style.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [func ISO8601Format(Date.ISO8601FormatStyle) -> String](date/iso8601format(_:).md)
  Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatted(date:time:))*