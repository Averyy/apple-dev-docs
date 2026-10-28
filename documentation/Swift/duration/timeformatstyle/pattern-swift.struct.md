# Duration.TimeFormatStyle.Pattern

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The units — including hours, minutes, or seconds — and the configuration of those units, used to format a duration.

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
struct Pattern
```

## Overview

Use a pattern when initializing a [`Duration.TimeFormatStyle`](../timeformatstyle.md), or creating a time format style from the convenience method `Swift/Duration/TimeFormatStyle/time(pattern:)`.

Use the type properties [`hourMinute`](./pattern-swift.struct/hourminute.md), [`hourMinuteSecond`](./pattern-swift.struct/hourminutesecond.md), or [`minuteSecond`](./pattern-swift.struct/minutesecond.md) to create patterns with default behavior. To customize how a pattern handles zero-padding and fractional parts, use one of the type methods that take these customizations as parameters.

## Topics

### Creating a pattern
- [static func hourMinute(padHourToLength: Int, roundSeconds: FloatingPointRoundingRule) -> Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/hourminute%28padhourtolength,roundseconds%29.md)
  Returns a pattern to format a duration with hours and minutes only, with the given unit configurations.
- [static func hourMinuteSecond(padHourToLength: Int, fractionalSecondsLength: Int, roundFractionalSeconds: FloatingPointRoundingRule) -> Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/hourminutesecond%28padhourtolength,fractionalsecondslength,roundfractionalseconds%29.md)
  Returns a pattern to format a duration with hours, minutes, and seconds, with the given unit configurations.
- [static func minuteSecond(padMinuteToLength: Int, fractionalSecondsLength: Int, roundFractionalSeconds: FloatingPointRoundingRule) -> Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/minutesecond%28padminutetolength,fractionalsecondslength,roundfractionalseconds%29.md)
  Returns a pattern to format a duration with minutes and seconds only, with the given unit configurations.
### Using common patterns
- [static var hourMinute: Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/hourminute.md)
  A pattern to format a duration with hours and minutes only, with default padding and rounding behavior.
- [static var hourMinuteSecond: Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/hourminutesecond.md)
  A pattern to format a duration with hours, minutes, and seconds, with default padding and rounding behavior.
- [static var minuteSecond: Duration.TimeFormatStyle.Pattern](./pattern-swift.struct/minutesecond.md)
  A pattern to format a duration with minutes and seconds only, with default padding and rounding behavior.

## Relationships

### Conforms To
- [Decodable](../../decodable.md)
- [Encodable](../../encodable.md)
- [Equatable](../../equatable.md)
- [Hashable](../../hashable.md)
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Creating a time format style
- [init(pattern: Duration.TimeFormatStyle.Pattern, locale: Locale)](./init%28pattern,locale%29.md)
  Creates a time format style using the provided pattern and optional locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/timeformatstyle/pattern-swift.struct)*