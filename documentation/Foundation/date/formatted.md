# formatted(_:)

**Framework**: Foundation  
**Kind**: method

Generates a locale-aware string representation of a date using the specified date format style.

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
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == Date
```

#### Return Value

A string, formatted according to the specified style.

#### Discussion

For full customization of the string representation of a date, use the [`formatted(_:)`](date/formatted(_:).md) instance method of [`Date`](date.md) and provide a [`Date.FormatStyle`](date/formatstyle.md) object.

You can achieve any customization of date and time representation your app requires by appying a series of convenience modifiers to your format style. This example applies a series of modifiers to the format style to precisely define the formatting of the year, month, day, hour, minute, and timezone components of the resulting string.

```swift
// Call the .formatted method on an instance of Date passing in an instance of Date.FormatStyle.

let birthday = Date()

birthday.formatted(
    Date.FormatStyle()
        .year(.defaultDigits)
        .month(.abbreviated)
        .day(.twoDigits)
        .hour(.defaultDigits(amPM: .abbreviated))
        .minute(.twoDigits)
        .timeZone(.identifier(.long))
        .era(.wide)
        .dayOfYear(.defaultDigits)
        .weekday(.abbreviated)
        .week(.defaultDigits)
) 
// Sun, Jan 17, 2021 Anno Domini (week: 4), 11:18 AM America/Chicago
```

For the default date formatting, use the [`formatted()`](date/formatted().md) method. For basic customization of the formatted date string, use the [`formatted(date:time:)`](date/formatted(date:time:).md) and include a date and time style.

For more information about formatting dates, see [`Date.FormatStyle`](date/formatstyle.md).

## Parameters

- `format`: The date format style to apply to the date.

## See Also

- [func formatted() -> String](date/formatted.md)
  Generates a locale-aware string representation of a date using the default date format style.
- [func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String](date/formatted(date:time:).md)
  Generates a locale-aware string representation of a date using specified date and time format styles.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatted(_:))*