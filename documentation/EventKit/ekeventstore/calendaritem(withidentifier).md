# calendarItem(withIdentifier:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Locates a reminder or the first occurrence of an event with the specified identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func calendarItem(withIdentifier identifier: String) -> EKCalendarItem?
```

```objc
- (EKCalendarItem *) calendarItemWithIdentifier:(NSString *) identifier;
```

## Mentions

- [Retrieving events and reminders](../retrieving-events-and-reminders.md)

#### Return Value

The reminder or the first occurrence of an event with the specified identifier, or `nil` if neither is found.

## Parameters

- `identifier`: The calendar item’s unique identifier.

## See Also

### Accessing calendar events
- [func event(withIdentifier: String) -> EKEvent?](./event%28withidentifier%29.md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](./calendaritems%28withexternalidentifier%29.md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](./remove%28_,span%29.md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](./remove%28_,span,commit%29.md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func remove(EKReminder, commit: Bool) throws](./remove%28_,commit%29.md)
  Removes a reminder from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan) throws](./save%28_,span%29.md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](./save%28_,span,commit%29.md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](./save%28_,commit%29.md)
  Saves changes to a reminder by either committing or batching the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendaritem(withidentifier:))*