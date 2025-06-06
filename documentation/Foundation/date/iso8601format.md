# ISO8601Format(_:)

**Framework**: Foundation  
**Kind**: method

Generates a locale-aware string representation of a date using the ISO 8601 date format.

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
func ISO8601Format(_ style: Date.ISO8601FormatStyle = .init()) -> String
```

#### Return Value

A string, formatted according to the specified style.

#### Discussion

Calling this method is equivalent to passing a [`Date.ISO8601FormatStyle`](date/iso8601formatstyle.md) to a date’s [`formatted()`](date/formatted().md) method.

## Parameters

- `style`: A customized   to apply. By default, the method applies an unmodified ISO 8601 format style.

## See Also

- [func formatted() -> String](date/formatted.md)
  Generates a locale-aware string representation of a date using the default date format style.
- [func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String](date/formatted(date:time:).md)
  Generates a locale-aware string representation of a date using specified date and time format styles.
- [func formatted<F>(F) -> F.FormatOutput](date/formatted(_:).md)
  Generates a locale-aware string representation of a date using the specified date format style.
- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/iso8601format(_:))*