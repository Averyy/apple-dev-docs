# EKSource

**Framework**: EventKit  
**Kind**: class

An abstract superclass that represents the account a calendar belongs to.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKSource
```

#### Overview

You do not create instances of this class; instead, you retrieve `EKSource` objects from an [`EKEventStore`](ekeventstore.md) object. Use the sources property to get all the `EKSource` objects for an event store, and use the methods in this class to access properties of the source object.

## Topics

### Accessing Source Properties
- [enum EKSourceType](eksourcetype.md)
  The type of source object.
- [var sourceIdentifier: String](eksource/sourceidentifier.md)
  A unique identifier for the source object.
- [var sourceType: EKSourceType](eksource/sourcetype.md)
  The type of this source object.
- [var title: String](eksource/title.md)
  The name of this source object.
### Accessing Calendars
- [func calendars(for: EKEntityType) -> Set<EKCalendar>](eksource/calendars(for:).md)
  Returns the calendars that belong to this source object that support a particular entity type.
- [var calendars: Set<EKCalendar>](eksource/calendars.md)
  The calendars that belong to this source object.
### Entity Type
- [enum EKEntityType](ekentitytype.md)
  The type of entities allowed for a source.
### Instance Properties
- [var isDelegate: Bool](eksource/isdelegate.md)

## Relationships

### Inherits From
- [EKObject](ekobject.md)
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
- [class EKObject](ekobject.md)
  An abstract superclass for all EventKit classes that have persistent instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/eksource)*