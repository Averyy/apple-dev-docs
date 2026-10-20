# daylightSavingTimeOffset(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the daylight saving time offset for a given date.

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
func daylightSavingTimeOffset(for aDate: Date) -> TimeInterval
```

```objc
- (NSTimeInterval) daylightSavingTimeOffsetForDate:(NSDate *) aDate;
```

#### Return Value

The daylight saving time offset for `aDate`.

## Parameters

- `aDate`: A date.

## See Also

### Working with Daylight Savings
- [var isDaylightSavingTime: Bool](./isdaylightsavingtime.md)
  A Boolean value that indicates whether the receiver is currently using daylight saving time.
- [func isDaylightSavingTime(for: Date) -> Bool](./isdaylightsavingtime%28for%29.md)
  Indicates whether the receiver uses daylight saving time on a given date.
- [var daylightSavingTimeOffset: TimeInterval](./daylightsavingtimeoffset.md)
  The current daylight saving time offset of the receiver.
- [var nextDaylightSavingTimeTransition: Date?](./nextdaylightsavingtimetransition.md)
  The date of the next daylight saving time transition for the receiver.
- [func nextDaylightSavingTimeTransition(after: Date) -> Date?](./nextdaylightsavingtimetransition%28after%29.md)
  Returns the next daylight saving time transition after a given date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstimezone/daylightsavingtimeoffset(for:))*