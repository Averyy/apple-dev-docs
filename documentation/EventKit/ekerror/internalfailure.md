# internalFailure

**Framework**: EventKit  
**Kind**: property  
**Role**: Type Property

An internal error occurred.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
static var internalFailure: EKError.Code { get }
```

## See Also

### Error Codes
- [static var eventNotMutable: EKError.Code](./eventnotmutable.md)
  The event isn’t mutable and you can’t save or delete it.
- [static var noCalendar: EKError.Code](./nocalendar.md)
  The event isn’t associated with a calendar.
- [static var noEndDate: EKError.Code](./noenddate.md)
  The event has no start date set.
- [static var noStartDate: EKError.Code](./nostartdate.md)
  The event has no end date set.
- [static var datesInverted: EKError.Code](./datesinverted.md)
  The event’s end date occurs before its start date.
- [static var calendarReadOnly: EKError.Code](./calendarreadonly.md)
  The calendar is read-only and you can’t add events to it.
- [static var durationGreaterThanRecurrence: EKError.Code](./durationgreaterthanrecurrence.md)
  The duration of an event is greater than its recurrence interval.
- [static var alarmGreaterThanRecurrence: EKError.Code](./alarmgreaterthanrecurrence.md)
  The alarm interval is greater than the recurrence interval.
- [static var startDateTooFarInFuture: EKError.Code](./startdatetoofarinfuture.md)
  The start date is further into the future than the calendar can display.
- [static var startDateCollidesWithOtherOccurrence: EKError.Code](./startdatecollideswithotheroccurrence.md)
  The event’s start date collides with another occurrence of the event.
- [static var objectBelongsToDifferentStore: EKError.Code](./objectbelongstodifferentstore.md)
  The object belongs to a different calendar store.
- [static var invitesCannotBeMoved: EKError.Code](./invitescannotbemoved.md)
  You can’t move the event because it’s an invitation.
- [static var invalidSpan: EKError.Code](./invalidspan.md)
  The system encountered an invalid span during a save or deletion.
- [static var calendarHasNoSource: EKError.Code](./calendarhasnosource.md)
  You can’t save the calendar without setting a source first.
- [static var calendarSourceCannotBeModified: EKError.Code](./calendarsourcecannotbemodified.md)
  You can’t move the calendar to another source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekerror/internalfailure)*