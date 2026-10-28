# iso8601Date(timeZone:dateSeparator:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.

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
static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash) -> Self
```

Available when `Self` is `Date.ISO8601FormatStyle`.

## Return Value

A `RegexComponent` that matches ISO 8601-formatted date substrings as Foundation [`Date`](../../Foundation/date.md) instances.

## Discussion

This method matches an ISO 8601 date string using the provided date separator. This method only matches a date substring. If the source string also contains a time, this method doesn’t match it. To match both date and time in an ISO 8601-formatted string, use [`iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)`](./iso8601%28timezone,includingfractionalseconds,dateseparator,datetimeseparator,timeseparator%29.md).

The returned date’s time is midnight in the provided time zone.

The following example creates a [`Regex`](../regex.md) that matches a date formatted with the base ISO 8601 format and dashes for date separators. It then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let iso860Source = "2022-07-14   Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.iso8601Date(timeZone: TimeZone(identifier: "PST")!,
                         dateSeparator: .dash))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code:Locale.Currency("USD"),
                           locale:Locale(identifier: "en_US")))
}
let match = iso860Source.firstMatch(of: matcher)
let date = match?.1 // date == Jul 14, 2022 at 12:00 AM PST
```

## Parameters

- `timeZone`: The time zone to use when returning a captured [`Date`](../../Foundation/date.md). The returned date’s time value is `00:00:00` in this time zone.
- `dateSeparator`: The character that separates year, month, and day sections of the date substring.

## See Also

### Matching dates and times
- [static func date(Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](./date%28_,locale,timezone,calendar%29.md)
  Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar?, twoDigitStartDate: Date) -> Self](./date%28format,locale,timezone,calendar,twodigitstartdate%29.md)
  Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](./datetime%28date,time,locale,timezone,calendar%29.md)
  Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [static var iso8601: Date.ISO8601FormatStyle](./iso8601.md)
  A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator) -> Self](./iso8601%28timezone,includingfractionalseconds,dateseparator,datetimeseparator,timeseparator%29.md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [static func iso8601WithTimeZone(includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Self](./iso8601withtimezone%28includingfractionalseconds,dateseparator,datetimeseparator,timeseparator,timezoneseparator%29.md)
  Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/iso8601date(timezone:dateseparator:))*