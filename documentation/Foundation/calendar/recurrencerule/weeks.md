# weeks

**Framework**: Foundation  
**Kind**: property

On which weeks of the year the event should occur.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var weeks: [Int]
```

#### Discussion

- 1 is the first week of the year. `calendar.minimumDaysInFirstWeek` defines which week is considered first.
- Negative values refer to weeks if counting backwards from the last week of the year. -1 is the last week of the year. This field is unused when `frequency` is other than `.yearly`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/weeks)*