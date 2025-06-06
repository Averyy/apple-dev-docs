# hourMinuteSecond(padHourToLength:fractionalSecondsLength:roundFractionalSeconds:)

**Framework**: Swift  
**Kind**: method

Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.

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
static func hourMinuteSecond(padHourToLength: Int, fractionalSecondsLength: Int = 0, roundFractionalSeconds: FloatingPointRoundingRule = .toNearestOrEven) -> Duration.TimeFormatStyle.Pattern
```

#### Return Value

A [`Duration.TimeFormatStyle.Pattern`](duration/timeformatstyle/pattern-swift.struct.md) that formats a duration with hours, minutes, and seconds, using the given unit configurations.

## Parameters

- `padHourToLength`: Padding for the hour field. For example, setting this value to   formats one hour as   in   locale.
- `fractionalSecondsLength`: The length of the fractional seconds. For example, setting this value to   formats one hour as   in the   locale.
- `roundFractionalSeconds`: The rule to use for rounding the seconds value, given the remaining fractional seconds value. Use one of the cases from the   enumeration.

## See Also

- [static func hourMinute(padHourToLength: Int, roundSeconds: FloatingPointRoundingRule) -> Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct/hourminute(padhourtolength:roundseconds:).md)
  Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.
- [static func minuteSecond(padMinuteToLength: Int, fractionalSecondsLength: Int, roundFractionalSeconds: FloatingPointRoundingRule) -> Duration.TimeFormatStyle.Pattern](duration/timeformatstyle/pattern-swift.struct/minutesecond(padminutetolength:fractionalsecondslength:roundfractionalseconds:).md)
  Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct/hourminutesecond(padhourtolength:fractionalsecondslength:roundfractionalseconds:))*