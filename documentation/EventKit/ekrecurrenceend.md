# EKRecurrenceEnd

**Framework**: EventKit  
**Kind**: class

A class that defines the end of a recurrence rule.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKRecurrenceEnd
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)

#### Overview

The `EKRecurrenceEnd` class defines the end of a recurrence rule defined by an [`EKRecurrenceRule`](ekrecurrencerule.md) object. The recurrence end can be specified by a date (date-based) or by a maximum count of occurrences (count-based). An event that is intended to continue indefinitely should have its `EKRecurrenceEnd` set to `nil`.

## Topics

### Creating a Recurrence End
- [convenience init(end: Date)](ekrecurrenceend/init(end:).md)
  Initializes and returns a date-based recurrence end with a given end date.
- [convenience init(occurrenceCount: Int)](ekrecurrenceend/init(occurrencecount:).md)
  Initializes and returns a count-based recurrence end with a given maximum occurrence count.
### Accessing Recurrence End Properties
- [var endDate: Date?](ekrecurrenceend/enddate.md)
  The end date of the recurrence end, or `nil` if the recurrence end is count-based.
- [var occurrenceCount: Int](ekrecurrenceend/occurrencecount.md)
  The occurrence count of the recurrence end, or `0` if the recurrence end is date-based.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Creating a recurring event](creating-a-recurring-event.md)
  Set up an event or reminder that repeats.
- [class EKRecurrenceDayOfWeek](ekrecurrencedayofweek.md)
  A class that represents the day of the week.
- [class EKRecurrenceRule](ekrecurrencerule.md)
  A class that describes the pattern for a recurring event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrenceend)*