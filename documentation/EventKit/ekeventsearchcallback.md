# EKEventSearchCallback

**Framework**: EventKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for a closure that operates on events when enumerating them.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
typealias EKEventSearchCallback = (EKEvent, UnsafeMutablePointer<ObjCBool>) -> Void
```

```c
typedef void (^)(EKEvent *, _Bool *) EKEventSearchCallback;
```

## Parameters

- `event`: An event object to operate on.
- `stop`: A pointer to a Boolean value. Set this value to [`true`](../Swift/true.md) to stop enumerating events.

## See Also

### Searching calendars
- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](./ekeventstore/enumerateevents%28matching,using%29.md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](./ekeventstore/events%28matching%29.md)
  Finds all events that match a given predicate.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](./ekeventstore/fetchreminders%28matching,completion%29.md)
  Fetches reminders that match a given predicate.
- [func cancelFetchRequest(Any)](./ekeventstore/cancelfetchrequest%28_%29.md)
  Cancels the request to fetch reminders.
- [func predicateForEvents(withStart: Date, end: Date, calendars: [EKCalendar]?) -> NSPredicate](./ekeventstore/predicateforevents%28withstart,end,calendars%29.md)
  Creates a predicate to identify events that occur within a given date range.
- [func predicateForReminders(in: [EKCalendar]?) -> NSPredicate](./ekeventstore/predicateforreminders%28in%29.md)
  Creates a predicate to identify all reminders in a collection of calendars.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](./ekeventstore/predicateforcompletedreminders%28withcompletiondatestarting,ending,calendars%29.md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](./ekeventstore/predicateforincompletereminders%28withduedatestarting,ending,calendars%29.md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventsearchcallback)*