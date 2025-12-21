# daysOfTheYear

**Framework**: Foundation  
**Kind**: property

On which days of the year the event may occur.

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
var daysOfTheYear: [Int]
```

#### Discussion

- 1 signifies the first day of the year.
- Negative values point to a day counted backwards from the last day of the year This field is unused when `frequency` is any of `.daily`, `.weekly`, or `.monthly`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/daysoftheyear)*