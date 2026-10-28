# EKRecurrenceDayOfWeek

**Framework**: EventKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface EKRecurrenceDayOfWeek : NSObject
```

## Mentions

- [Creating a recurring event](./creating-a-recurring-event.md)

## Overview

The `EKRecurrenceDayOfWeek` class represents a day of the week for use with an [`EKRecurrenceRule`](./ekrecurrencerule.md) object.

A day of the week can optionally have a week number, indicating a specific day in the recurrence rule’s frequency. For example, a day of the week with a day value of Tuesday and a week number of 2 would represent the second Tuesday of every month in a monthly recurrence rule, and the second Tuesday of every year in a yearly recurrence rule. A day of the week with a week number of 0 ignores its week number.

## Topics

### Creating a Day of the Week
- [enum EKWeekday](./ekweekday.md)
  The day of the week.
- [convenience init(EKWeekday)](./ekrecurrencedayofweek/init%28_%29.md)
  Creates and returns a day of the week with a given day.
- [convenience init(EKWeekday, weekNumber: Int)](./ekrecurrencedayofweek/init%28_,weeknumber%29.md)
  Creates and returns an autoreleased day of the week with a given day and week number.
- [init(dayOfTheWeek: EKWeekday, weekNumber: Int)](./ekrecurrencedayofweek/init%28dayoftheweek,weeknumber%29.md)
  Initializes and returns a day of the week with a given day and week number.
### Accessing Properties of a Day of the Week
- [var dayOfTheWeek: EKWeekday](./ekrecurrencedayofweek/dayoftheweek.md)
  The day of the week.
- [var weekNumber: Int](./ekrecurrencedayofweek/weeknumber.md)
  The week number of the day of the week.
### Initializers
- [init?(coder: NSCoder)](./ekrecurrencedayofweek/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Recurrence
- [Creating a recurring event](./creating-a-recurring-event.md)
  Set up an event or reminder that repeats.
- [class EKRecurrenceEnd](./ekrecurrenceend.md)
  A class that defines the end of a recurrence rule.
- [class EKRecurrenceRule](./ekrecurrencerule.md)
  A class that describes the pattern for a recurring event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencedayofweek)*