# dateTime(date:time:locale:timeZone:calendar:)

**Framework**: Swift  
**Kind**: method

Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.

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
static func dateTime(date: Date.FormatStyle.DateStyle, time: Date.FormatStyle.TimeStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar? = nil) -> Date.ParseStrategy
```

#### Return Value

A `RegexComponent` that matches date substrings as Foundation [`Date`](https://developer.apple.com/documentation/Foundation/Date) instances.

#### Discussion

This method matches date substrings in accordance with the formatting of Foundation’s [`Date.FormatStyle`](https://developer.apple.com/documentation/Foundation/Date/FormatStyle). If your source contains only a date or a time, use the `.omitted` value for the `date` or `time` style parameter to ignore the missing part.

The following example creates a [`Regex`](regex.md) that matches a date and time formatted with the [`numeric`](https://developer.apple.com/documentation/Foundation/Date/FormatStyle/DateStyle/numeric) style in the `en_US` locale. It then matches this regex against a source string containing a date with this format, some whitespace, a substring, more whitespace, and a currency value.

```swift
let enUSLocale = Locale(languageCode: .english, languageRegion: .unitedStates)
let source = "7/31/2022, 5:15:12 PM  Lemon-lime slushie      $1.99"
let matcher = Regex {
    Capture {
        One(.dateTime(date: .numeric,
                      time: .standard,
                      locale: enUSLocale,
                      timeZone: TimeZone(identifier: "PST")!))
    }
    OneOrMore(.horizontalWhitespace)
    OneOrMore(.any)
    OneOrMore(.horizontalWhitespace)
    One(.localizedCurrency(code: Locale.Currency("USD"),
                           locale: enUSLocale))
}

guard let match = source.firstMatch(of: matcher) else { return }
let date = match.1 // date == Jul 31, 2022 at 5:15 PM PST
```

## Parameters

- `date`: A   to use when matching date substrings. Pass   to match a time-only substring.
- `time`: A   to use when matching time substrings. Pass   to match a date-only substring.
- `locale`: The locale to use when matching date substrings. Matching uses this locale to evaluate the order of date components. It also uses the locale’s language for date format styles that use words.
- `timeZone`: The time zone to use when capturing the date and time values. The regex component ignores this parameter if the source string contains a time zone substring that the format style supports.
- `calendar`: The calendar to use when matching date substrings. If  , matching uses the default calendar of the specified  .

## See Also

- [static func date(Date.FormatStyle.DateStyle, locale: Locale, timeZone: TimeZone, calendar: Calendar?) -> Date.ParseStrategy](regexcomponent/date(_:locale:timezone:calendar:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [static func date(format: Date.FormatString, locale: Locale, timeZone: TimeZone, calendar: Calendar?, twoDigitStartDate: Date) -> Self](regexcomponent/date(format:locale:timezone:calendar:twodigitstartdate:).md)
  Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [static var iso8601: Date.ISO8601FormatStyle](regexcomponent/iso8601.md)
  A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [static func iso8601Date(timeZone: TimeZone, dateSeparator: Date.ISO8601FormatStyle.DateSeparator) -> Self](regexcomponent/iso8601date(timezone:dateseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [static func iso8601(timeZone: TimeZone, includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator) -> Self](regexcomponent/iso8601(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [static func iso8601WithTimeZone(includingFractionalSeconds: Bool, dateSeparator: Date.ISO8601FormatStyle.DateSeparator, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator) -> Self](regexcomponent/iso8601withtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:).md)
  Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/datetime(date:time:locale:timezone:calendar:))*