# init(dayOfTheWeek:weekNumber:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a day of the week with a given day and week number.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(dayOfTheWeek: EKWeekday, weekNumber: Int)
```

```objc
- (id) initWithDayOfTheWeek:(EKWeekday) dayOfTheWeek weekNumber:(NSInteger) weekNumber;
```

## Return Value

The initialized day of the week.

## Parameters

- `dayOfTheWeek`: The day of the week. Values range from `1` to `7`, with Sunday being `1`.
- `weekNumber`: The week number.

## See Also

### Creating a Day of the Week
- [enum EKWeekday](../ekweekday.md)
  The day of the week.
- [convenience init(EKWeekday)](./init%28_%29.md)
  Creates and returns a day of the week with a given day.
- [convenience init(EKWeekday, weekNumber: Int)](./init%28_,weeknumber%29.md)
  Creates and returns an autoreleased day of the week with a given day and week number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/init(dayoftheweek:weeknumber:))*