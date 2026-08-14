# EKRecurrenceDayOfWeek

**Framework**: EventKit  
**Kind**: class

A class that represents the day of the week.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKRecurrenceDayOfWeek
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)

#### Overview

The `EKRecurrenceDayOfWeek` class represents a day of the week for use with an [`EKRecurrenceRule`](ekrecurrencerule.md) object.

A day of the week can optionally have a week number, indicating a specific day in the recurrence rule’s frequency. For example, a day of the week with a day value of Tuesday and a week number of 2 would represent the second Tuesday of every month in a monthly recurrence rule, and the second Tuesday of every year in a yearly recurrence rule. A day of the week with a week number of 0 ignores its week number.

## Topics

### Creating a Day of the Week
- [enum EKWeekday](ekweekday.md)
  The day of the week.
- [convenience init(EKWeekday)](ekrecurrencedayofweek/init(_:).md)
  Creates and returns a day of the week with a given day.
- [convenience init(EKWeekday, weekNumber: Int)](ekrecurrencedayofweek/init(_:weeknumber:).md)
  Creates and returns an autoreleased day of the week with a given day and week number.
- [init(dayOfTheWeek: EKWeekday, weekNumber: Int)](ekrecurrencedayofweek/init(dayoftheweek:weeknumber:).md)
  Initializes and returns a day of the week with a given day and week number.
### Accessing Properties of a Day of the Week
- [var dayOfTheWeek: EKWeekday](ekrecurrencedayofweek/dayoftheweek.md)
  The day of the week.
- [var weekNumber: Int](ekrecurrencedayofweek/weeknumber.md)
  The week number of the day of the week.
### Initializers
- [init?(coder: NSCoder)](ekrecurrencedayofweek/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Creating a recurring event](creating-a-recurring-event.md)
  Set up an event or reminder that repeats.
- [class EKRecurrenceEnd](ekrecurrenceend.md)
  A class that defines the end of a recurrence rule.
- [class EKRecurrenceRule](ekrecurrencerule.md)
  A class that describes the pattern for a recurring event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)*