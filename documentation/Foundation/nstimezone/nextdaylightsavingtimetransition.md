# nextDaylightSavingTimeTransition

**Framework**: Foundation  
**Kind**: property

The date of the next daylight saving time transition for the receiver.

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
var nextDaylightSavingTimeTransition: Date? { get }
```

#### Discussion

This property contains the date of the next (after the current instant) daylight saving time transition for the receiver. Depending on the time zone of the receiver, the value of this property may represent a change of the time zone’s offset from GMT. Returns `nil` if the time zone of the receiver does not currently observe daylight saving time.

## See Also

- [var isDaylightSavingTime: Bool](nstimezone/isdaylightsavingtime.md)
  A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [func isDaylightSavingTime(for: Date) -> Bool](nstimezone/isdaylightsavingtime(for:).md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](nstimezone/daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](nstimezone/daylightsavingtimeoffset(for:).md)
  Returns the daylight saving time offset for a given date.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](nstimezone/nextdaylightsavingtimetransition(after:).md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/nextdaylightsavingtimetransition)*