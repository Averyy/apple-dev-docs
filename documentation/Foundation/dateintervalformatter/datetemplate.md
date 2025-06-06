# dateTemplate

**Framework**: Foundation  
**Kind**: property

The template for formatting one date and time value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var dateTemplate: String! { get set }
```

#### Discussion

Use this string to specify a custom fixed format for each of the date and time values. The string you specify is based on the Unicode Technical Standard #35, which uses characters to represent the day, time, year, hour, minute, and other pieces of date or time information.

If you do not assign a value to this string, the formatter object automatically updates the string based on the values in the [`dateStyle`](dateintervalformatter/datestyle.md) and [`timeStyle`](dateintervalformatter/timestyle.md) properties.

For information about how to define a custom formatting string, see [`Date Formatters`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/dfDateFormatting10_4.html#//apple_ref/doc/uid/TP40002369) in [`Data Formatting Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## See Also

- [var dateStyle: DateIntervalFormatter.Style](dateintervalformatter/datestyle.md)
  The style to use when formatting day, month, and year information.
- [var timeStyle: DateIntervalFormatter.Style](dateintervalformatter/timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var calendar: Calendar!](dateintervalformatter/calendar.md)
  The calendar to use for date values.
- [var locale: Locale!](dateintervalformatter/locale.md)
  The locale to use when formatting date and time values.
- [var timeZone: TimeZone!](dateintervalformatter/timezone.md)
  The time zone with which to specify time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/datetemplate)*