# Creating events and reminders

**Framework**: EventKit

Create and modify events and reminders in a person’s database.

#### Overview

Once you have permission to access a person’s Calendar and Reminder data, you can create, display, and edit events and reminders.

##### Create Events

Create a new event with the [`init(eventStore:)`](ekevent/init(eventstore:).md) method of the [`EKEvent`](ekevent.md) class.

You can edit the details of a new event or an event you previously fetched from the Calendar database by setting the event’s corresponding properties. Some of the details you can edit include:

- The event’s title with the [`title`](ekcalendar/title.md) property.
- The event’s start and end dates with the [`startDate`](ekevent/startdate.md) and [`endDate`](ekevent/enddate.md) properties.
- The calendar with which the event is associated with the [`calendar`](ekcalendaritem/calendar.md) property.
- The alarms associated with the event with the [`alarms`](ekcalendaritem/alarms.md) property (see “[`Setting an alarm`](setting-an-alarm.md)” for more details).
- The event’s recurrence rule, if it is a repeating event, with the `recurrenceRules` property (see “[`Creating a recurring event`](creating-a-recurring-event.md)” for more details).

> **Note**:  In iOS, you have the option of letting users modify event data with the event view controllers provided in the EventKit UI framework. For information on how to use these event view controllers, see [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI).

###### Save and Delete Events

> ❗ **Important**:  If your app modifies a user’s Calendar database, it must get confirmation from the user before doing so. An app should never modify the Calendar database without specific instruction from the user.

Save your changes to the Calendar database with the [`EKEventStore`](ekeventstore.md) method [`save(_:span:commit:)`](ekeventstore/save(_:span:commit:).md). If you want to remove an event from the Calendar database, use the `EKEventStore` method [`remove(_:span:commit:)`](ekeventstore/remove(_:span:commit:).md). Whether you are saving or removing an event, implementing the respective method automatically syncs your changes with the calendar the event belongs to (CalDAV, Exchange, and so on).

If you are saving a recurring event, your changes can apply to all future occurrences of the event by specifying [`EKSpan.futureEvents`](ekspan/futureevents.md) for the span parameter of the [`save(_:span:commit:)`](ekeventstore/save(_:span:commit:).md) method. Likewise, you can remove all future occurrences of an event by specifying [`EKSpan.futureEvents`](ekspan/futureevents.md) for the `span` parameter of the [`remove(_:span:commit:)`](ekeventstore/remove(_:span:commit:).md) method.

> **Note**:  If you pass `NO` to the `commit` parameter, make sure that you later invoke the [`commit()`](ekeventstore/commit().md) method to permanently save your changes.

##### Create Reminders

Reminders are tasks that may be tied to a specific time or location. They are similar to calendar events, but can be marked complete and may not necessarily span an exact period of time.

Because [`EKReminder`](ekreminder.md) inherits from [`EKCalendarItem`](ekcalendaritem.md), you can perform the same methods on a reminder as you would on an event, such as adding an alarm with [`addAlarm(_:)`](ekcalendaritem/addalarm(_:).md) or setting a recurrence rule with [`addRecurrenceRule(_:)`](ekcalendaritem/addrecurrencerule(_:).md).

> ❗ **Important**:  If your iOS app links on macOS and you need to access Reminders data, be sure to include the [`NSRemindersUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW16) key in your `Info.plist` file.

You can create reminders using the [`init(eventStore:)`](ekreminder/init(eventstore:).md) class method. The [`title`](ekcalendaritem/title.md) and [`calendar`](ekcalendaritem/calendar.md) properties are required. The calendar for a reminder is the list with which it is grouped.

Like events, reminders can trigger time-based or location-based alarms to alert the user of a certain task. Read “`Setting an Alarm`” for more information on how to attach alarms to calendar items.

###### Save and Delete Reminders

To save a reminder to the Calendar database, call the [`save(_:commit:)`](ekeventstore/save(_:commit:).md) method. To remove an event, call the [`remove(_:commit:)`](ekeventstore/remove(_:commit:).md) method. The [`title`](ekcalendar/title.md) and [`calendars`](ekeventstore/calendars.md) properties must explicitly be set before you save the reminder.

> **Note**:  Just like when saving or removing events, make sure that if you pass `NO` to the `commit` parameter, you later invoke the [`commit()`](ekeventstore/commit().md) method to save your changes.

###### Edit Reminders

To associate a start date or due date with a reminder, use the [`startDateComponents`](ekreminder/startdatecomponents.md) and [`dueDateComponents`](ekreminder/duedatecomponents.md) properties. To complete a reminder, set the completed property to `YES`, which automatically sets [`completionDate`](ekreminder/completiondate.md) to the current date.

> ❗ **Important**:  If your app modifies a user’s Calendar database, it must get confirmation from the user before doing so. An app should never modify the Calendar database without specific instruction from the user.

## See Also

- [Retrieving events and reminders](retrieving-events-and-reminders.md)
  Fetch events and reminders from the Calendar database.
- [Updating with notifications](updating-with-notifications.md)
  Register for notifications about changes and keep your app up to date.
- [Managing location-based reminders](managing-location-based-reminders.md)
  Access reminders set up with geofence-enabled alarms on a person’s calendars.
- [class EKEvent](ekevent.md)
  A class that represents an event in a calendar.
- [class EKReminder](ekreminder.md)
  A class that represents a reminder in a calendar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/creating-events-and-reminders)*