# init(_:weekNumber:)

**Framework**: EventKit  
**Kind**: init

Creates and returns an autoreleased day of the week with a given day and week number.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(_ dayOfTheWeek: EKWeekday, weekNumber: Int)
```

#### Return Value

The new day of the week.

## Parameters

- `dayOfTheWeek`: The day of the week. Values range from   to  , with Sunday being  .
- `weekNumber`: The week number.

## See Also

- [enum EKWeekday](ekweekday.md)
  The day of the week.
- [convenience init(EKWeekday)](ekrecurrencedayofweek/init(_:).md)
  Creates and returns a day of the week with a given day.
- [init(dayOfTheWeek: EKWeekday, weekNumber: Int)](ekrecurrencedayofweek/init(dayoftheweek:weeknumber:).md)
  Initializes and returns a day of the week with a given day and week number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/init(_:weeknumber:))*