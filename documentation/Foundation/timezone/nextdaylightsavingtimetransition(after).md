# nextDaylightSavingTimeTransition(after:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the next daylight saving time transition after a given date.

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
func nextDaylightSavingTimeTransition(after date: Date) -> Date?
```

#### Return Value

The next daylight saving time transition after `date`. Depending on the time zone, this function may return a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not observe daylight savings time as of `date`.

## Parameters

- `date`: A date.

## See Also

### Working with Daylight Savings
- [func isDaylightSavingTime(for: Date) -> Bool](./isdaylightsavingtime%28for%29.md)
  Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](./daylightsavingtimeoffset%28for%29.md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](./nextdaylightsavingtimetransition.md)
  The date of the next (after the current instant) daylight saving time transition for the time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/nextdaylightsavingtimetransition(after:))*