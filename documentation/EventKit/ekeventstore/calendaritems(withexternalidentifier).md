# calendarItems(withExternalIdentifier:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Locates all reminders or the first occurrences of all events with the specified external identifier.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func calendarItems(withExternalIdentifier externalIdentifier: String) -> [EKCalendarItem]
```

```objc
- (NSArray<EKCalendarItem *> *) calendarItemsWithExternalIdentifier:(NSString *) externalIdentifier;
```

#### Return Value

An array of calendar items with the specified identifier.

#### Discussion

Use [`calendarItemExternalIdentifier`](../ekcalendaritem/calendaritemexternalidentifier.md) to obtain the external identifier. There may be more than one matching calendar item due to reasons discussed in `calendarItemExternalIdentifier`.

## Parameters

- `externalIdentifier`: The calendar item’s external identifier.

## See Also

### Accessing calendar events
- [func event(withIdentifier: String) -> EKEvent?](./event%28withidentifier%29.md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](./calendaritem%28withidentifier%29.md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/calendaritems(withexternalidentifier:))*