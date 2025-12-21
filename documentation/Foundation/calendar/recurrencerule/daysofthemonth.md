# daysOfTheMonth

**Framework**: Foundation  
**Kind**: property

On which days in the month the event should occur

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
var daysOfTheMonth: [Int]
```

#### Discussion

- 1 signifies the first day of the month.
- Negative values point to a day counted backwards from the last day of the month This field is unused when `frequency` is `.weekly`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/daysofthemonth)*