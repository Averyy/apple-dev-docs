# EKObject

**Framework**: EventKit  
**Kind**: class

An abstract superclass for all EventKit classes that have persistent instances.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class EKObject
```

#### Overview

`EKObject` provides fine control when saving and restoring property settings. For example, you can find out if a persistent object was modified locally and whether it needs to be saved. If the object has changed in the event store since it was fetched, you can refresh the local copy by keeping local changes or by removing local changes. You can also roll back the object to the state when it was first fetched.

## Topics

### Saving and Restoring State
- [var hasChanges: Bool](ekobject/haschanges.md)
  Returns whether this object or any of the objects it contains has uncommitted changes.
- [var isNew: Bool](ekobject/isnew.md)
  A Boolean value that indicates whether this object has ever been saved.
- [func refresh() -> Bool](ekobject/refresh.md)
  Merges changes to this object with the latest saved values.
- [func reset()](ekobject/reset.md)
  Returns this object to its saved state.
- [func rollback()](ekobject/rollback.md)
  Rolls back the property values of this object to its original state when it was first fetched.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [EKAlarm](ekalarm.md)
- [EKCalendar](ekcalendar.md)
- [EKCalendarItem](ekcalendaritem.md)
- [EKParticipant](ekparticipant.md)
- [EKRecurrenceRule](ekrecurrencerule.md)
- [EKSource](eksource.md)
- [EKStructuredLocation](ekstructuredlocation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class EKCalendarItem](ekcalendaritem.md)
  An abstract superclass for calendar events and reminders.
- [class EKSource](eksource.md)
  An abstract superclass that represents the account a calendar belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekobject)*