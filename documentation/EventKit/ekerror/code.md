# EKError.Code

**Framework**: EventKit  
**Kind**: enum

Error codes for EventKit errors.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Code
```

## Topics

### Constants
- [EKError.Code.eventNotMutable](ekerror/code/eventnotmutable.md)
  The event isn’t mutable and you can’t save or delete it.
- [EKError.Code.noCalendar](ekerror/code/nocalendar.md)
  The event isn’t associated with a calendar.
- [EKError.Code.noStartDate](ekerror/code/nostartdate.md)
  The event has no start date set.
- [EKError.Code.noEndDate](ekerror/code/noenddate.md)
  The event has no end date set.
- [EKError.Code.datesInverted](ekerror/code/datesinverted.md)
  The event’s end date occurs before its start date.
- [EKError.Code.internalFailure](ekerror/code/internalfailure.md)
  An internal error occurred.
- [EKError.Code.calendarReadOnly](ekerror/code/calendarreadonly.md)
  The calendar is read-only and you can’t add events to it.
- [EKError.Code.durationGreaterThanRecurrence](ekerror/code/durationgreaterthanrecurrence.md)
  The duration of an event is greater than its recurrence interval.
- [EKError.Code.alarmGreaterThanRecurrence](ekerror/code/alarmgreaterthanrecurrence.md)
  The alarm interval is greater than the recurrence interval.
- [EKError.Code.startDateTooFarInFuture](ekerror/code/startdatetoofarinfuture.md)
  The start date is further into the future than the calendar can display.
- [EKError.Code.startDateCollidesWithOtherOccurrence](ekerror/code/startdatecollideswithotheroccurrence.md)
  The event’s start date collides with another occurrence of the event.
- [EKError.Code.objectBelongsToDifferentStore](ekerror/code/objectbelongstodifferentstore.md)
  The object belongs to a different calendar store.
- [EKError.Code.invitesCannotBeMoved](ekerror/code/invitescannotbemoved.md)
  You can’t move the event because it’s an invitation.
- [EKError.Code.invalidSpan](ekerror/code/invalidspan.md)
  The system encountered an invalid span during a save or deletion.
- [EKError.Code.calendarHasNoSource](ekerror/code/calendarhasnosource.md)
  You can’t save the calendar without setting a source first.
- [EKError.Code.calendarSourceCannotBeModified](ekerror/code/calendarsourcecannotbemodified.md)
  You can’t move the calendar to another source.
- [EKError.Code.calendarIsImmutable](ekerror/code/calendarisimmutable.md)
  The calendar is immutable and you can’t modify or delete it.
- [EKError.Code.sourceDoesNotAllowCalendarAddDelete](ekerror/code/sourcedoesnotallowcalendaradddelete.md)
  The source doesn’t allow you to add or delete calendars.
- [EKError.Code.recurringReminderRequiresDueDate](ekerror/code/recurringreminderrequiresduedate.md)
  The recurring reminder requires a due date.
- [EKError.Code.structuredLocationsNotSupported](ekerror/code/structuredlocationsnotsupported.md)
  The source to which this calendar belongs doesn’t support structured locations.
- [EKError.Code.reminderLocationsNotSupported](ekerror/code/reminderlocationsnotsupported.md)
  The source doesn’t support locations on reminders.
- [EKError.Code.alarmProximityNotSupported](ekerror/code/alarmproximitynotsupported.md)
  The source doesn’t allow geofences on alarms.
- [EKError.Code.calendarDoesNotAllowEvents](ekerror/code/calendardoesnotallowevents.md)
  The calendar doesn’t allow you to add events.
- [EKError.Code.calendarDoesNotAllowReminders](ekerror/code/calendardoesnotallowreminders.md)
  The calendar doesn’t allow you to add reminders.
- [EKError.Code.sourceDoesNotAllowReminders](ekerror/code/sourcedoesnotallowreminders.md)
  The source doesn’t allow calendars supporting reminder entity types.
- [EKError.Code.sourceDoesNotAllowEvents](ekerror/code/sourcedoesnotallowevents.md)
  The source doesn’t allow calendars supporting event entity types.
- [EKError.Code.priorityIsInvalid](ekerror/code/priorityisinvalid.md)
  The priority number for the reminder is invalid.
- [EKError.Code.invalidEntityType](ekerror/code/invalidentitytype.md)
  The entity type is invalid.
- [EKError.Code.procedureAlarmsNotMutable](ekerror/code/procedurealarmsnotmutable.md)
  You can’t create or modify procedure alarms.
- [EKError.Code.eventStoreNotAuthorized](ekerror/code/eventstorenotauthorized.md)
  The user hasn’t authorized your app to access events or reminders.
- [EKError.Code.osNotSupported](ekerror/code/osnotsupported.md)
  The action isn’t supported on the current operating system.
- [EKError.Code.invalidInviteReplyCalendar](ekerror/code/invalidinvitereplycalendar.md)
  The calendar is invalid or nil.
- [EKError.Code.notificationsCollectionFlagNotSet](ekerror/code/notificationscollectionflagnotset.md)
  The notification collection doesn’t have the notifications collection flag.
- [EKError.Code.sourceMismatch](ekerror/code/sourcemismatch.md)
  The object’s source doesn’t match its container’s source.
- [EKError.Code.notificationCollectionMismatch](ekerror/code/notificationcollectionmismatch.md)
  The notification collection that contains this notification doesn’t match the collection the system is trying to save.
- [EKError.Code.notificationSavedWithoutCollection](ekerror/code/notificationsavedwithoutcollection.md)
  The notification can’t save because you haven’t added it to a notification collection and saved the collection first.
- [EKError.Code.last](ekerror/code/last.md)
  This error is for internal use.
### Enumeration Cases
- [EKError.Code.reminderAlarmContainsEmailOrUrl](ekerror/code/reminderalarmcontainsemailorurl.md)
### Initializers
- [init?(rawValue: Int)](ekerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct EKError](ekerror.md)
  An EventKit error.
- [let EKErrorDomain: String](ekerrordomain.md)
  A string that identifies the EventKit error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekerror/code)*