# EKError.Code.sourceMismatch

**Framework**: EventKit  
**Kind**: case

The object’s source doesn’t match its container’s source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case sourceMismatch
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekerror/code/sourcemismatch)*