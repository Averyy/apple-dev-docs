# EKError

**Framework**: EventKit  
**Kind**: struct

An EventKit error.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct EKError
```

## Topics

### Error Codes
- [static var eventNotMutable: EKError.Code](ekerror/eventnotmutable.md)
  The event isn’t mutable and you can’t save or delete it.
- [static var noCalendar: EKError.Code](ekerror/nocalendar.md)
  The event isn’t associated with a calendar.
- [static var noEndDate: EKError.Code](ekerror/noenddate.md)
  The event has no start date set.
- [static var noStartDate: EKError.Code](ekerror/nostartdate.md)
  The event has no end date set.
- [static var datesInverted: EKError.Code](ekerror/datesinverted.md)
  The event’s end date occurs before its start date.
- [static var internalFailure: EKError.Code](ekerror/internalfailure.md)
  An internal error occurred.
- [static var calendarReadOnly: EKError.Code](ekerror/calendarreadonly.md)
  The calendar is read-only and you can’t add events to it.
- [static var durationGreaterThanRecurrence: EKError.Code](ekerror/durationgreaterthanrecurrence.md)
  The duration of an event is greater than its recurrence interval.
- [static var alarmGreaterThanRecurrence: EKError.Code](ekerror/alarmgreaterthanrecurrence.md)
  The alarm interval is greater than the recurrence interval.
- [static var startDateTooFarInFuture: EKError.Code](ekerror/startdatetoofarinfuture.md)
  The start date is further into the future than the calendar can display.
- [static var startDateCollidesWithOtherOccurrence: EKError.Code](ekerror/startdatecollideswithotheroccurrence.md)
  The event’s start date collides with another occurrence of the event.
- [static var objectBelongsToDifferentStore: EKError.Code](ekerror/objectbelongstodifferentstore.md)
  The object belongs to a different calendar store.
- [static var invitesCannotBeMoved: EKError.Code](ekerror/invitescannotbemoved.md)
  You can’t move the event because it’s an invitation.
- [static var invalidSpan: EKError.Code](ekerror/invalidspan.md)
  The system encountered an invalid span during a save or deletion.
- [static var calendarHasNoSource: EKError.Code](ekerror/calendarhasnosource.md)
  You can’t save the calendar without setting a source first.
- [static var calendarSourceCannotBeModified: EKError.Code](ekerror/calendarsourcecannotbemodified.md)
  You can’t move the calendar to another source.
- [static var calendarIsImmutable: EKError.Code](ekerror/calendarisimmutable.md)
  The calendar is immutable and you can’t modify or delete it.
- [static var sourceDoesNotAllowCalendarAddDelete: EKError.Code](ekerror/sourcedoesnotallowcalendaradddelete.md)
  The source doesn’t allow you to add or delete calendars.
- [static var recurringReminderRequiresDueDate: EKError.Code](ekerror/recurringreminderrequiresduedate.md)
  The recurring reminder requires a due date.
- [static var structuredLocationsNotSupported: EKError.Code](ekerror/structuredlocationsnotsupported.md)
  The source to which this calendar belongs doesn’t support structured locations.
- [static var reminderLocationsNotSupported: EKError.Code](ekerror/reminderlocationsnotsupported.md)
  The source doesn’t support locations on reminders.
- [static var alarmProximityNotSupported: EKError.Code](ekerror/alarmproximitynotsupported.md)
  The source doesn’t allow geofences on alarms.
- [static var calendarDoesNotAllowEvents: EKError.Code](ekerror/calendardoesnotallowevents.md)
  The calendar doesn’t allow you to add events.
- [static var calendarDoesNotAllowReminders: EKError.Code](ekerror/calendardoesnotallowreminders.md)
  The calendar doesn’t allow you to add reminders.
- [static var sourceDoesNotAllowReminders: EKError.Code](ekerror/sourcedoesnotallowreminders.md)
  The source doesn’t allow calendars supporting reminder entity types.
- [static var sourceDoesNotAllowEvents: EKError.Code](ekerror/sourcedoesnotallowevents.md)
  The source doesn’t allow calendars supporting event entity types.
- [static var priorityIsInvalid: EKError.Code](ekerror/priorityisinvalid.md)
  The priority number for the reminder is invalid.
- [static var invalidEntityType: EKError.Code](ekerror/invalidentitytype.md)
  The entity type is invalid.
- [static var procedureAlarmsNotMutable: EKError.Code](ekerror/procedurealarmsnotmutable.md)
  You can’t create or modify procedure alarms.
- [static var eventStoreNotAuthorized: EKError.Code](ekerror/eventstorenotauthorized.md)
  The user hasn’t authorized your app to access events or reminders.
- [static var osNotSupported: EKError.Code](ekerror/osnotsupported.md)
  The action isn’t supported on the current operating system.
- [static var invalidInviteReplyCalendar: EKError.Code](ekerror/invalidinvitereplycalendar.md)
  The calendar is invalid or nil.
- [static var notificationsCollectionFlagNotSet: EKError.Code](ekerror/notificationscollectionflagnotset.md)
  The notification collection doesn’t have the notifications collection flag.
- [static var sourceMismatch: EKError.Code](ekerror/sourcemismatch.md)
  The object’s source doesn’t match its container’s source.
- [static var notificationCollectionMismatch: EKError.Code](ekerror/notificationcollectionmismatch.md)
  The notification collection that contains this notification doesn’t match the collection the system is trying to save.
- [static var notificationSavedWithoutCollection: EKError.Code](ekerror/notificationsavedwithoutcollection.md)
  The notification can’t save because you haven’t added it to a notification collection and saved the collection first.
- [static var last: EKError.Code](ekerror/last.md)
  This error is for internal use.
### Error Domain
- [let EKErrorDomain: String](ekerrordomain.md)
  A string that identifies the EventKit error domain.
### Type Properties
- [static var errorDomain: String](ekerror/errordomain.md)
- [static var reminderAlarmContainsEmailOrUrl: EKError.Code](ekerror/reminderalarmcontainsemailorurl.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [EKError.Code](ekerror/code.md)
  Error codes for EventKit errors.
- [let EKErrorDomain: String](ekerrordomain.md)
  A string that identifies the EventKit error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekerror)*