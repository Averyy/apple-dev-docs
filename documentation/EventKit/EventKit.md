# EventKit

**Framework**: EventKit  
**Kind**: module

Create, view, and edit calendar and reminder events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The EventKit framework provides access to calendar and reminders data so people can create, retrieve, and edit calendar items in your app. In iOS, [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI) provides user interfaces you can implement in your app so people can create and edit calendar items.

You can use EventKit to set up alarms and create recurring events. And if a change to the Calendar database occurs from outside your app, EventKit detects the change and sends a notification, allowing your app to stay up to date.

## Topics

### Essentials
- [Accessing the event store](accessing-the-event-store.md)
  Request access to a person’s calendar data through the event store.
- [class EKEventStore](ekeventstore.md)
  An object that accesses a person’s calendar events and reminders and supports the scheduling of new events.
- [Accessing Calendar using EventKit and EventKitUI](accessing-calendar-using-eventkit-and-eventkitui.md)
  Choose and implement the appropriate Calendar access level in your app.
### Events and reminders
- [Creating events and reminders](creating-events-and-reminders.md)
  Create and modify events and reminders in a person’s database.
- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Updating with notifications](updating-with-notifications.md)
  Register for notifications about changes and keep your app up to date.
- [Managing Location-Based Reminders](managing-location-based-reminders.md)
  Add, fetch, complete, remove, and sort location-based reminders in your app.
- [class EKEvent](ekevent.md)
  A class that represents an event in a calendar.
- [class EKReminder](ekreminder.md)
  A class that represents a reminder in a calendar.
### Calendars
- [class EKCalendar](ekcalendar.md)
  A class that represents a calendar in EventKit.
- [class EKParticipant](ekparticipant.md)
  A class that represents person, group, or room invited to a calendar event.
### Recurrence
- [Creating a recurring event](creating-a-recurring-event.md)
  Set up an event or reminder that repeats.
- [class EKRecurrenceDayOfWeek](ekrecurrencedayofweek.md)
  A class that represents the day of the week.
- [class EKRecurrenceEnd](ekrecurrenceend.md)
  A class that defines the end of a recurrence rule.
- [class EKRecurrenceRule](ekrecurrencerule.md)
  A class that describes the pattern for a recurring event.
### Alarms
- [Setting an alarm](setting-an-alarm.md)
  Alert users of events and reminders with an alarm.
- [class EKAlarm](ekalarm.md)
  A class that represents an alarm.
- [class EKStructuredLocation](ekstructuredlocation.md)
  `A` class that specifies a geofence to activate the alarm of a calendar item.
### Common objects
- [class EKCalendarItem](ekcalendaritem.md)
  An abstract superclass for calendar events and reminders.
- [class EKObject](ekobject.md)
  An abstract superclass for all EventKit classes that have persistent instances.
- [class EKSource](eksource.md)
  An abstract superclass that represents the account a calendar belongs to.
### Virtual conferences
- [class EKVirtualConferenceProvider](ekvirtualconferenceprovider.md)
  An object that associates virtual conferencing details with an event object in a user’s calendar.
- [class EKVirtualConferenceDescriptor](ekvirtualconferencedescriptor.md)
  Details about a virtual conference that uses a custom room type.
- [class EKVirtualConferenceRoomTypeDescriptor](ekvirtualconferenceroomtypedescriptor.md)
  Details about a room where virtual conferences take place.
### Errors
- [struct EKError](ekerror.md)
  An EventKit error.
- [EKError.Code](ekerror/code.md)
  Error codes for EventKit errors.
- [let EKErrorDomain: String](ekerrordomain.md)
  A string that identifies the EventKit error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/EventKit)*