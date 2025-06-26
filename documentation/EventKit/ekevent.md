# EKEvent

**Framework**: EventKit  
**Kind**: class

A class that represents an event in a calendar.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKEvent
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)
- [Creating events and reminders](creating-events-and-reminders.md)

#### Overview

Use the [`init(eventStore:)`](ekevent/init(eventstore:).md) method to create a new event. Use the properties in the class to get and modify certain information about an event. Other properties, such as the event’s title and calendar, are inherited from the parent class [`EKCalendarItem`](ekcalendaritem.md).

## Topics

### Creating Events
- [init(eventStore: EKEventStore)](ekevent/init(eventstore:).md)
  Creates and returns a new event belonging to a specified event store.
### Scheduling Events
- [enum EKEventStatus](ekeventstatus.md)
  The event’s status.
- [enum EKEventAvailability](ekeventavailability.md)
  The event’s availability setting for scheduling purposes.
### Comparing Events
- [func compareStartDate(with: EKEvent) -> ComparisonResult](ekevent/comparestartdate(with:).md)
  Compares the start date of the receiving event with the start date of another event.
### Accessing Event Properties
- [var eventIdentifier: String!](ekevent/eventidentifier.md)
  A unique identifier for the event.
- [var availability: EKEventAvailability](ekevent/availability.md)
  The availability setting for the event.
- [var startDate: Date!](ekevent/startdate.md)
  The start date of the event.
- [var endDate: Date!](ekevent/enddate.md)
  The end date for the event.
- [var isAllDay: Bool](ekevent/isallday.md)
  A Boolean value that indicates whether the event is an all-day event.
- [var occurrenceDate: Date!](ekevent/occurrencedate.md)
  The original occurrence date of an event if it is part of a recurring series.
- [var isDetached: Bool](ekevent/isdetached.md)
  A Boolean value that indicates whether an event is a detached instance of a repeating event.
- [var organizer: EKParticipant?](ekevent/organizer.md)
  The organizer associated with the event.
- [var status: EKEventStatus](ekevent/status.md)
  The status of the event.
- [var birthdayContactIdentifier: String?](ekevent/birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var structuredLocation: EKStructuredLocation?](ekevent/structuredlocation.md)
  The event’s location with a potential geocoordinate.
- [var birthdayPersonID: Int](ekevent/birthdaypersonid.md)
  The Address Book framework record identifier of the person for this birthday event.
- [var birthdayPersonUniqueID: String?](ekevent/birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.
### Refreshing Event Data
- [func refresh() -> Bool](ekevent/refresh.md)
  Updates the event’s data with the current information in the Calendar database.

## Relationships

### Inherits From
- [EKCalendarItem](ekcalendaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating events and reminders](creating-events-and-reminders.md)
  Create and modify events and reminders in a person’s database.
- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Updating with notifications](updating-with-notifications.md)
  Register for notifications about changes and keep your app up to date.
- [Managing location-based reminders](managing-location-based-reminders.md)
  Access reminders set up with geofence-enabled alarms on a person’s calendars.
- [class EKReminder](ekreminder.md)
  A class that represents a reminder in a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent)*