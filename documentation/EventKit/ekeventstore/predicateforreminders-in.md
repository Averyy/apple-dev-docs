# predicateForReminders(in:)

**Framework**: EventKit  
**Kind**: method

Creates a predicate to identify all reminders in a collection of calendars.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func predicateForReminders(in calendars: [EKCalendar]?) -> NSPredicate
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

A predicate to use when calling [`fetchReminders(matching:completion:)`](ekeventstore/fetchreminders(matching:completion:).md).

## Parameters

- `calendars`: An array of calendars to search.

## See Also

- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](ekeventstore/enumerateevents(matching:using:).md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](ekeventstore/events(matching:).md)
  Finds all events that match a given predicate.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](ekeventstore/fetchreminders(matching:completion:).md)
  Fetches reminders that match a given predicate.
- [func cancelFetchRequest(Any)](ekeventstore/cancelfetchrequest(_:).md)
  Cancels the request to fetch reminders.
- [func predicateForEvents(withStart: Date, end: Date, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforevents(withstart:end:calendars:).md)
  Creates a predicate to identify events that occur within a given date range.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforcompletedreminders(withcompletiondatestarting:ending:calendars:).md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforincompletereminders(withduedatestarting:ending:calendars:).md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.
- [typealias EKEventSearchCallback](ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/predicateforreminders(in:))*