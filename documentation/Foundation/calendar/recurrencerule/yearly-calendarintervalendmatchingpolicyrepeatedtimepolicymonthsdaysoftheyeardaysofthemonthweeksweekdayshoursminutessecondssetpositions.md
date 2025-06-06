# yearly(calendar:interval:end:matchingPolicy:repeatedTimePolicy:months:daysOfTheYear:daysOfTheMonth:weeks:weekdays:hours:minutes:seconds:setPositions:)

**Framework**: Foundation  
**Kind**: method

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
static func yearly(calendar: Calendar, interval: Int = 1, end: Calendar.RecurrenceRule.End = .never, matchingPolicy: Calendar.MatchingPolicy = .nextTimePreservingSmallerComponents, repeatedTimePolicy: Calendar.RepeatedTimePolicy = .first, months: [Calendar.RecurrenceRule.Month] = [], daysOfTheYear: [Int] = [], daysOfTheMonth: [Int] = [], weeks: [Int] = [], weekdays: [Calendar.RecurrenceRule.Weekday] = [], hours: [Int] = [], minutes: [Int] = [], seconds: [Int] = [], setPositions: [Int] = []) -> Calendar.RecurrenceRule
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/recurrencerule/yearly(calendar:interval:end:matchingpolicy:repeatedtimepolicy:months:daysoftheyear:daysofthemonth:weeks:weekdays:hours:minutes:seconds:setpositions:))*