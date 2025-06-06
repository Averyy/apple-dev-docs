# event(withIdentifier:)

**Framework**: EventKit  
**Kind**: method

Locates the first occurrence of an event with a given identifier.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func event(withIdentifier identifier: String) -> EKEvent?
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

The event that corresponds with `identifier`, or `nil` if no event is found.

## Parameters

- `identifier`: The identifier of the event.

## See Also

- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](ekeventstore/calendaritem(withidentifier:).md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](ekeventstore/calendaritems(withexternalidentifier:).md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](ekeventstore/remove(_:span:).md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/remove(_:span:commit:).md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func remove(EKReminder, commit: Bool) throws](ekeventstore/remove(_:commit:).md)
  Removes a reminder from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan) throws](ekeventstore/save(_:span:).md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/save(_:span:commit:).md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](ekeventstore/save(_:commit:).md)
  Saves changes to a reminder by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/event(withidentifier:))*