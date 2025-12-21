# isDaylightSavingTime(for:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the receiver uses daylight saving time on a given date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isDaylightSavingTime(for aDate: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver uses daylight saving time at `aDate`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `aDate`: The date against which to test the receiver.

## See Also

- [var isDaylightSavingTime: Bool](nstimezone/isdaylightsavingtime.md)
  A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [var daylightSavingTimeOffset: TimeInterval](nstimezone/daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](nstimezone/daylightsavingtimeoffset(for:).md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](nstimezone/nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](nstimezone/nextdaylightsavingtimetransition(after:).md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/isdaylightsavingtime(for:))*