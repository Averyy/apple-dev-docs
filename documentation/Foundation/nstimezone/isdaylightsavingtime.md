# isDaylightSavingTime

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the receiver is currently using daylight saving time.

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
var isDaylightSavingTime: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the receiver is currently using daylight saving time, otherwise [`false`](https://developer.apple.com/documentation/swift/false). This property invokes [`isDaylightSavingTime(for:)`](nstimezone/isdaylightsavingtime(for:).md) with the current date as the argument.

## See Also

- [func isDaylightSavingTime(for: Date) -> Bool](nstimezone/isdaylightsavingtime(for:).md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](nstimezone/daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](nstimezone/daylightsavingtimeoffset(for:).md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](nstimezone/nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](nstimezone/nextdaylightsavingtimetransition(after:).md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/isdaylightsavingtime)*