# EKCalendar

**Framework**: EventKit  
**Kind**: class

A class that represents a calendar in EventKit.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKCalendar
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Overview

Use the properties in this class to get attributes about a calendar, such as its title and type. Use the [`init(for:eventStore:)`](ekcalendar/init(for:eventstore:).md) method to create a calendar object.

## Topics

### Creating Calendars
- [init(for: EKEntityType, eventStore: EKEventStore)](ekcalendar/init(for:eventstore:).md)
  Creates a new calendar that can contain the given entity type.
- [init(eventStore: EKEventStore)](ekcalendar/init(eventstore:).md)
  Creates and returns a calendar belonging to a specified event store.
### Accessing Calendar Properties
- [enum EKCalendarType](ekcalendartype.md)
  Possible calendar types.
- [struct EKCalendarEventAvailabilityMask](ekcalendareventavailabilitymask.md)
  A bitmask indicating the event availability settings that the calendar can support.
- [var allowsContentModifications: Bool](ekcalendar/allowscontentmodifications.md)
  A Boolean value that indicates whether you can add, edit, and delete items in the calendar.
- [var cgColor: CGColor!](ekcalendar/cgcolor.md)
  The calendar’s color.
- [var color: NSColor!](ekcalendar/color.md)
  The calendar’s color.
- [var isImmutable: Bool](ekcalendar/isimmutable.md)
  A Boolean value indicating whether the calendar’s properties can be edited or deleted.
- [var title: String](ekcalendar/title.md)
  The calendar’s title.
- [var type: EKCalendarType](ekcalendar/type.md)
  The calendar’s type.
- [var allowedEntityTypes: EKEntityMask](ekcalendar/allowedentitytypes.md)
  The entity types this calendar can contain.
- [var source: EKSource!](ekcalendar/source.md)
  The source object representing the account to which this calendar belongs.
- [var isSubscribed: Bool](ekcalendar/issubscribed.md)
  A Boolean value indicating whether the calendar is a subscribed calendar.
- [var supportedEventAvailabilities: EKCalendarEventAvailabilityMask](ekcalendar/supportedeventavailabilities.md)
  The event availability settings supported by this calendar, as indicated by a bitmask.
- [var calendarIdentifier: String](ekcalendar/calendaridentifier.md)
  A unique identifier for the calendar.
- [func DATETIME_COMPONENTS_DO_NOT_USE()](datetime_components_do_not_use().md)
  A deprecated function.
- [func DATE_COMPONENTS_DO_NOT_USE()](date_components_do_not_use().md)
  A deprecated function.

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

- [class EKParticipant](ekparticipant.md)
  A class that represents person, group, or room invited to a calendar event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendar)*