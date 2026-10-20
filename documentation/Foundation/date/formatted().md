# formatted()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Generates a locale-aware string representation of a date using the default date format style.

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
func formatted() -> String
```

#### Return Value

A string, formatted according to the default style.

#### Discussion

Use the [`formatted()`](./formatted%28%29.md) method to apply the default format style to a date, as in the following example:

```swift
let birthday = Date()
print(birthday.formatted())
// 6/4/2021, 2:24 PM
```

The default date format style uses the `numeric` date style and the `shortened` time style.

To customize the formatted measurement string, use either the [`formatted(_:)`](./formatted%28_%29.md) method and include a `Measurement.FormatStyle` or the [`formatted(date:time:)`](./formatted%28date,time%29.md) and include a date and time style.

For more information about formatting dates, see [`Date.FormatStyle`](./formatstyle.md).

## See Also

### Formatting a Date
- [func formatted(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle) -> String](./formatted%28date,time%29.md)
  Generates a locale-aware string representation of a date using specified date and time format styles.
- [func formatted<F>(F) -> F.FormatOutput](./formatted%28_%29.md)
  Generates a locale-aware string representation of a date using the specified date format style.
- [struct FormatStyle](./formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct RelativeFormatStyle](./relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [struct IntervalFormatStyle](./intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [func ISO8601Format(Date.ISO8601FormatStyle) -> String](./iso8601format%28_%29.md)
  Generates a locale-aware string representation of a date using the ISO 8601 date format.
- [struct ISO8601FormatStyle](./iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatted())*