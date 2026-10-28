# isDaylightSavingTime

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isDaylightSavingTime) BOOL daylightSavingTime;
```

## Discussion

If [`true`](../../Swift/true.md), the receiver is currently using daylight saving time, otherwise [`false`](../../Swift/false.md). This property invokes [`isDaylightSavingTime(for:)`](./isdaylightsavingtime%28for%29.md) with the current date as the argument.

## See Also

### Working with Daylight Savings
- [func isDaylightSavingTime(for: Date) -> Bool](./isdaylightsavingtime%28for%29.md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](./daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [func daylightSavingTimeOffset(for: Date) -> TimeInterval](./daylightsavingtimeoffset%28for%29.md)
  Returns the daylight saving time offset for a given date.
- [var nextDaylightSavingTimeTransition: Date?](./nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](./nextdaylightsavingtimetransition%28after%29.md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/isdaylightsavingtime)*