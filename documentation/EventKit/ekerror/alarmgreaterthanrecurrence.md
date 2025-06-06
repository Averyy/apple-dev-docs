# alarmGreaterThanRecurrence

**Framework**: EventKit  
**Kind**: property

The alarm interval is greater than the recurrence interval.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var alarmGreaterThanRecurrence: EKError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekerror/alarmgreaterthanrecurrence)*