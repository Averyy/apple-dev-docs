# nextDaylightSavingTimeTransition(after:)

**Framework**: Foundation  
**Kind**: method

Returns the next daylight saving time transition after a given date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func nextDaylightSavingTimeTransition(after aDate: Date) -> Date?
```

#### Return Value

The next daylight saving time transition after `aDate`. Depending on the time zone of the receiver, this method may return a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not observe daylight savings time as of `aDate`.

## Parameters

- `aDate`: A date.

## See Also

- [var isDaylightSavingTime: Bool](nstimezone/isdaylightsavingtime.md)
  A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [func isDaylightSavingTime(for: Date) -> Bool](nstimezone/isdaylightsavingtime(for:).md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](nstimezone/daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](nstimezone/daylightsavingtimeoffset(for:).md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](nstimezone/nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/nextdaylightsavingtimetransition(after:))*