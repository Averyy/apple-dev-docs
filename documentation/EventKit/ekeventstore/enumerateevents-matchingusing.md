# enumerateEvents(matching:using:)

**Framework**: EventKit  
**Kind**: method

Finds all events that match a given predicate and calls a given callback for each event found.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateEvents(matching predicate: NSPredicate, using block: @escaping EKEventSearchCallback)
```

#### Discussion

Only committed events are included in the enumeration. To include events saved using [`save(_:span:commit:)`](ekeventstore/save(_:span:commit:).md) with the `commit` parameter set to [`false`](https://developer.apple.com/documentation/Swift/false), call [`commit()`](ekeventstore/commit().md) first.

This method is synchronous. For asynchronous behavior, run the method on another thread with [`dispatch_async`](https://developer.apple.com/documentation/Dispatch/dispatch_async) or [`Operation`](https://developer.apple.com/documentation/Foundation/Operation).

## Parameters

- `predicate`: A search predicate created with  .
- `block`: The closure to call for each event. The callback must match the signature defined by  .

## See Also

- [func events(matching: NSPredicate) -> [EKEvent]](ekeventstore/events(matching:).md)
  Finds all events that match a given predicate.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](ekeventstore/fetchreminders(matching:completion:).md)
  Fetches reminders that match a given predicate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/enumerateevents(matching:using:))*