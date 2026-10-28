# init(_:weekNumber:)

**Framework**: EventKit  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) dayOfWeek:(EKWeekday) dayOfTheWeek weekNumber:(NSInteger) weekNumber;
```

## Return Value

The new day of the week.

## Parameters

- `dayOfTheWeek`: The day of the week. Values range from `1` to `7`, with Sunday being `1`.
- `weekNumber`: The week number.

## See Also

### Creating a Day of the Week
- [enum EKWeekday](../ekweekday.md)
  The day of the week.
- [convenience init(EKWeekday)](./init%28_%29.md)
  Creates and returns a day of the week with a given day.
- [init(dayOfTheWeek: EKWeekday, weekNumber: Int)](./init%28dayoftheweek,weeknumber%29.md)
  Initializes and returns a day of the week with a given day and week number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek/init(_:weeknumber:))*