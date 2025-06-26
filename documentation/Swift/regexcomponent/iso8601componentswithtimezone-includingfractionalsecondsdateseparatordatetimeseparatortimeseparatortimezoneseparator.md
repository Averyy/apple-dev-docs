# iso8601ComponentsWithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)

**Framework**: Swift  
**Kind**: method

Creates a regex component to match an ISO 8601 date and time string, including time zone, and capture the string as a `DateComponents` using the time zone as specified in the string.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func iso8601ComponentsWithTimeZone(includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon, timeZoneSeparator: Date.ISO8601FormatStyle.TimeZoneSeparator = .omitted) -> Self
```

#### Return Value

A `RegexComponent` to match an ISO 8601 string, including time zone.

## Parameters

- `includingFractionalSeconds`: Specifies if the string contains fractional seconds.
- `dateSeparator`: The separator between date components.
- `dateTimeSeparator`: The separator between date and time parts.
- `timeSeparator`: The separator between time components.
- `timeZoneSeparator`: The separator between time parts in the time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/iso8601componentswithtimezone(includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:timezoneseparator:))*