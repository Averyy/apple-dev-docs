# daylightSavingTimeOffset(for:)

**Framework**: Foundation  
**Kind**: method

Returns the daylight saving time offset for a given date.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func daylightSavingTimeOffset(for date: Date = Date()) -> TimeInterval
```

## Parameters

- `date`: The date to use for the calculation. The default value is the current date.

## See Also

- [func isDaylightSavingTime(for: Date) -> Bool](timezone/isdaylightsavingtime(for:).md)
  Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [var nextDaylightSavingTimeTransition: Date?](timezone/nextdaylightsavingtimetransition.md)
  The date of the next (after the current instant) daylight saving time transition for the time zone.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](timezone/nextdaylightsavingtimetransition(after:).md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/daylightsavingtimeoffset(for:))*