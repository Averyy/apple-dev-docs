# nextDaylightSavingTimeTransition

**Framework**: Foundation  
**Kind**: property

The date of the next (after the current instant) daylight saving time transition for the time zone.

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
var nextDaylightSavingTimeTransition: Date? { get }
```

#### Discussion

Depending on the time zone, the value of this property may represent a change of the time zone’s offset from GMT. The value is `nil` if the time zone does not currently observe daylight saving time.

## See Also

- [func isDaylightSavingTime(for: Date) -> Bool](timezone/isdaylightsavingtime(for:).md)
  Returns a Boolean value that indicates whether the receiver uses daylight saving time at a given date.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](timezone/daylightsavingtimeoffset(for:).md)
  Returns the daylight saving time offset for a given date.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](timezone/nextdaylightsavingtimetransition(after:).md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/nextdaylightsavingtimetransition)*