# events(matching:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Finds all events that match a given predicate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func events(matching predicate: NSPredicate) -> [EKEvent]
```

```objc
- (NSArray<EKEvent *> *) eventsMatchingPredicate:(NSPredicate *) predicate;
```

## Mentions

- [Retrieving events and reminders](../retrieving-events-and-reminders.md)

#### Return Value

An array of events that match `predicate`.

#### Discussion

Only committed events are included in the results. To include events saved using [`save(_:span:commit:)`](./save%28_,span,commit%29.md) with the `commit` parameter set to [`false`](../../Swift/false.md), call [`commit()`](./commit%28%29.md) first.

This method is synchronous. For asynchronous behavior, run the method on another thread with [`dispatch_async`](../../Dispatch/dispatch_async.md) or [`Operation`](../../Foundation/operation.md).

## Parameters

- `predicate`: A search predicate created with [`predicateForEvents(withStart:end:calendars:)`](./predicateforevents%28withstart,end,calendars%29.md).

## See Also

### Searching calendars
- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](./enumerateevents%28matching,using%29.md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](./fetchreminders%28matching,completion%29.md)
  Fetches reminders that match a given predicate.
- [func cancelFetchRequest(Any)](./cancelfetchrequest%28_%29.md)
  Cancels the request to fetch reminders.
- [func predicateForEvents(withStart: Date, end: Date, calendars: [EKCalendar]?) -> NSPredicate](./predicateforevents%28withstart,end,calendars%29.md)
  Creates a predicate to identify events that occur within a given date range.
- [func predicateForReminders(in: [EKCalendar]?) -> NSPredicate](./predicateforreminders%28in%29.md)
  Creates a predicate to identify all reminders in a collection of calendars.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](./predicateforcompletedreminders%28withcompletiondatestarting,ending,calendars%29.md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](./predicateforincompletereminders%28withduedatestarting,ending,calendars%29.md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.
- [typealias EKEventSearchCallback](../ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/events(matching:))*