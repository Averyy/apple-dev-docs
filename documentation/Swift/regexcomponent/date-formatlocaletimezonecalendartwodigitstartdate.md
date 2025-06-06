# date(format:locale:timeZone:calendar:twoDigitStartDate:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.

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
static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar? = nil, twoDigitStartDate: Date = Date(timeIntervalSince1970: 0)) -> Self
```

#### Return Value

A `RegexComponent` that matches date substrings as Foundation [`Date`](https://developer.apple.com/documentation/Foundation/Date) instances.

#### Discussion

This method matches date substrings in accordance with a format from a [`Date.FormatString`](https://developer.apple.com/documentation/Foundation/Date/FormatString).

If a time value follows the date substring, the matcher ignores it, treating it as any other character sequence. To match date and time substrings, use [`dateTime(date:time:locale:timeZone:calendar:)`](regexcomponent/datetime(date:time:locale:timezone:calendar:).md).

If the date substring uses a two-digit year, the matcher uses the `twoDigitStartDate` parameter, which defines the earliest date a string with a two-digit year can denote. The matcher ignores this parameter if the year contains more than two digits.

The following example creates a [`Regex`](regex.md) that matches a date formatted with two-digit month, day, and year fields, and slash (`/`) separator characters. It sets midnight on January 1, 1970, as the `twoDigitStartDate`, and `PST` as the time zone. It then matches this regex against a source string containing a date with this format and a two-digit year, some whitespace, a substring, more whitespace, and a currency value. Because the source year `76` is after `thetwoDigitStartDate`, the date substring matches as `1976`.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "4/1/76  Lemon-lime slushie      $0.40"
let matcher = Regex {
    Capture {
        One(.date(format: "\(month: .twoDigits)/\(day: .twoDigits)/\(year: .twoDigits)",
                  locale: enUSLocale,
                  timeZone: TimeZone(identifier: "PST")!,
                  twoDigitStartDate: try! Date("1970-01-01T00:00:00-0800", strategy: .iso8601)))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code: Locale.Currency("USD"),
                           locale: enUSLocale))
}

let match = source.firstMatch(of: matcher)
let date = match?.1 // date == Mar 1, 1976 at 12:00 AM (may vary based on current locale)
```

## Parameters

- `format`: A   to use when matching date substrings.
- `locale`: The locale to use when matching date substrings. Matching uses this locale to evaluate the order of date components. It also uses the locale’s language for date format styles that use words.
- `timeZone`: The time zone to use when returning a captured  . The returned date’s time value is   in this time zone.
- `calendar`: The calendar to use when matching date substrings. If  , matching uses the default calendar of the specified  .
- `twoDigitStartDate`: The earliest date a matched two-year date can represent. For example, with the default value of  , the matcher treats   as 2022, and   as 1984. The matcher ignores this parameter for date substrings that contain year components with more than two digits.

## See Also

- [static func date(Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/date(_:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/datetime(date:time:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [static var iso8601: Date.ISO8601FormatStyle](regexcomponent/iso8601.md)
  A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator) -> Self](regexcomponent/iso8601date(timezone:dateseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator) -> Self](regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [static func iso8601WithTimeZone(includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Self](regexcomponent/iso8601withtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:))*