# fetchReminders(matching:completion:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Fetches reminders that match a given predicate.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fetchReminders(matching predicate: NSPredicate, completion: @escaping ([EKReminder]?) -> Void) -> Any
```

```objc
- (id) fetchRemindersMatchingPredicate:(NSPredicate *) predicate completion:(void (^)(NSArray<EKReminder *> *reminders)) completion;
```

## Mentions

- [Retrieving events and reminders](../retrieving-events-and-reminders.md)

#### Return Value

A value that represents the asynchronous fetch request. To cancel a fetch request before it completes, pass this value to [`cancelFetchRequest(_:)`](./cancelfetchrequest%28_%29.md).

#### Discussion

Only committed reminders are included in the results. To include reminders saved using [`save(_:commit:)`](./save%28_,commit%29.md) with the `commit` parameter set to [`false`](../../Swift/false.md), call [`commit()`](./commit%28%29.md) first.

This method fetches reminders asynchronously.

## Parameters

- `predicate`: A search predicate created with [`predicateForReminders(in:)`](./predicateforreminders%28in%29.md).
- `completion`: A closure that receives the reminders that match `predicate`.

## See Also

### Searching calendars
- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](./enumerateevents%28matching,using%29.md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](./events%28matching%29.md)
  Finds all events that match a given predicate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/fetchreminders(matching:completion:))*