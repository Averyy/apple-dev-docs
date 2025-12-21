# fetchReminders(matching:completion:)

**Framework**: EventKit  
**Kind**: method

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

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

A value that represents the asynchronous fetch request. To cancel a fetch request before it completes, pass this value to [`cancelFetchRequest(_:)`](ekeventstore/cancelfetchrequest(_:).md).

#### Discussion

Only committed reminders are included in the results. To include reminders saved using [`save(_:commit:)`](ekeventstore/save(_:commit:).md) with the `commit` parameter set to [`false`](https://developer.apple.com/documentation/Swift/false), call [`commit()`](ekeventstore/commit().md) first.

This method fetches reminders asynchronously.

## Parameters

- `predicate`: A search predicate created with  .
- `completion`: A closure that receives the reminders that match  .

## See Also

- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](ekeventstore/enumerateevents(matching:using:).md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](ekeventstore/events(matching:).md)
  Finds all events that match a given predicate.
- [func cancelFetchRequest(Any)](ekeventstore/cancelfetchrequest(_:).md)
  Cancels the request to fetch reminders.
- [func predicateForEvents(withStart: Date, end: Date, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforevents(withstart:end:calendars:).md)
  Creates a predicate to identify events that occur within a given date range.
- [func predicateForReminders(in: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforreminders(in:).md)
  Creates a predicate to identify all reminders in a collection of calendars.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforcompletedreminders(withcompletiondatestarting:ending:calendars:).md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforincompletereminders(withduedatestarting:ending:calendars:).md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.
- [typealias EKEventSearchCallback](ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/fetchreminders(matching:completion:))*