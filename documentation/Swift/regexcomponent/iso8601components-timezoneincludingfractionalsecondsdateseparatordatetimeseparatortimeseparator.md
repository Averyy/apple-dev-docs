# iso8601Components(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)

**Framework**: Swift  
**Kind**: method

Creates a regex component to match an ISO 8601 date and time string without time zone, and capture the string as a `DateComponents` using the specified `timeZone`. If the string contains time zone designators, matches up until the start of time zone designators.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

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