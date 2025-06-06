# iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.

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
static func iso8601WithTimeZone(includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator = .omitted) -> Self
```

#### Return Value

A `RegexComponent` that matches ISO 8601-formatted date substrings as Foundation [`Date`](https://developer.apple.com/documentation/Foundation/Date) instances.

#### Discussion

This method matches an ISO 8601 date string using the provided separator characters.

The following example creates a [`Regex`](regex.md) that matches an ISO 8601-formatted date. The format looks for a dash for the date separator, the standard date/time separator (none), a colon for the time separator, and no separator for the time zone. It then matches this regex against a source string containing a date with this format (specifying a time zone five hours behind UTC), some whitespace, a substring, more whitespace, and a currency value.

```swift
let iso860Source = "2022-07-14T21:10:15-05:00   Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.iso8601WithTimeZone(includingFractionalSeconds: false,
                                 dateSeparator: .dash,
                                 dateTimeSeparator: .standard,
                                 timeSeparator: .colon,
                                 timeZoneSeparator: .omitted))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code:Locale.Currency("USD"),
                           locale:Locale(identifier: "en_US")))
}
let match = iso860Source.firstMatch(of: matcher)
let date = match?.1 // date == Jul 14, 2022 at 7:10 PM (may vary depending on current locale)
```

## Parameters

- `includingFractionalSeconds`: A Boolean value that specifies whether the source string contains fractional seconds. The default is  .
- `dateSeparator`: The character that separates year, month, and day sections of the date substring. The default is  .
- `dateTimeSeparator`: The character that separates the date and time sections of the substring. The default is  .
- `timeSeparator`: The character that separates the date and time sections of the substring. The default is  .
- `timeZoneSeparator`: The character that separates the hour, minute, and second sections of the substring. The default is 

## See Also

- [static func date(Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/date(_:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar?, twoDigitStartDate: Date) -> Self](regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/datetime(date:time:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [static var iso8601: Date.ISO8601FormatStyle](regexcomponent/iso8601.md)
  A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator) -> Self](regexcomponent/iso8601date(timezone:dateseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator) -> Self](regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/iso8601withtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:))*