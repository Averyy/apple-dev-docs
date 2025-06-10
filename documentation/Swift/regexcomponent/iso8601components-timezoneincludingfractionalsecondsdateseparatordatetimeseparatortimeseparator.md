# iso8601Components(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)

**Framework**: Swift  
**Kind**: method

Creates a regex component to match an ISO 8601 date and time string without time zone, and capture the string as a `DateComponents` using the specified `timeZone`. If the string contains time zone designators, matches up until the start of time zone designators.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
static func iso8601Components(timeZone: TimeZone, includingFractionalSeconds: Bool = false, dateSeparator: Date.ISO8601FormatStyle.DateSeparator = .dash, dateTimeSeparator: Date.ISO8601FormatStyle.DateTimeSeparator = .standard, timeSeparator: Date.ISO8601FormatStyle.TimeSeparator = .colon) -> Self
```

#### Return Value

A `RegexComponent` to match an ISO 8601 string.

## Parameters

- `timeZone`: The time zone to create the captured   with.
- `includingFractionalSeconds`: Specifies if the string contains fractional seconds.
- `dateSeparator`: The separator between date components.
- `dateTimeSeparator`: The separator between date and time parts.
- `timeSeparator`: The separator between time components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexcomponent/iso8601components(timezone:includingfractionalseconds:dateseparator:datetimeseparator:timeseparator:))*