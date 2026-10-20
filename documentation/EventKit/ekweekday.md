# EKWeekday

**Framework**: EventKit  
**Kind**: enum  
**Role**: Enumeration

The day of the week.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
@frozen
enum EKWeekday
```

```c
enum EKWeekday : NSInteger;
```

## Topics

### Constants
- [EKWeekday.sunday](./ekweekday/sunday.md)
  The value for Sunday.
- [EKWeekday.monday](./ekweekday/monday.md)
  The value for Monday.
- [EKWeekday.tuesday](./ekweekday/tuesday.md)
  The value for Tuesday.
- [EKWeekday.wednesday](./ekweekday/wednesday.md)
  The value for Wednesday.
- [EKWeekday.thursday](./ekweekday/thursday.md)
  The value for Thursday.
- [EKWeekday.friday](./ekweekday/friday.md)
  The value for Friday.
- [EKWeekday.saturday](./ekweekday/saturday.md)
  The value for Saturday.
### Deprecated
- [static var EKSunday: EKWeekday](./ekweekday/eksunday.md)
  The value for Sunday.
- [static var EKMonday: EKWeekday](./ekweekday/ekmonday.md)
  The value for Monday.
- [static var EKTuesday: EKWeekday](./ekweekday/ektuesday.md)
  The value for Tuesday.
- [static var EKWednesday: EKWeekday](./ekweekday/ekwednesday.md)
  The value for Wednesday.
- [static var EKThursday: EKWeekday](./ekweekday/ekthursday.md)
  The value for Thursday.
- [static var EKFriday: EKWeekday](./ekweekday/ekfriday.md)
  The value for Friday.
- [static var EKSaturday: EKWeekday](./ekweekday/eksaturday.md)
  The value for Saturday.
### Initializers
- [init?(rawValue: Int)](./ekweekday/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Day of the Week
- [convenience init(EKWeekday)](./ekrecurrencedayofweek/init%28_%29.md)
  Creates and returns a day of the week with a given day.
- [convenience init(EKWeekday, weekNumber: Int)](./ekrecurrencedayofweek/init%28_,weeknumber%29.md)
  Creates and returns an autoreleased day of the week with a given day and week number.
- [init(dayOfTheWeek: EKWeekday, weekNumber: Int)](./ekrecurrencedayofweek/init%28dayoftheweek,weeknumber%29.md)
  Initializes and returns a day of the week with a given day and week number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekweekday)*