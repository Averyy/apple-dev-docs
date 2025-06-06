# cancelFetchRequest(_:)

**Framework**: EventKit  
**Kind**: method

Cancels the request to fetch reminders.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancelFetchRequest(_ fetchIdentifier: Any)
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Discussion

After canceling a fetch request, EventKit doesn’t call the completion originally specified in [`fetchReminders(matching:completion:)`](ekeventstore/fetchreminders(matching:completion:).md).

## Parameters

- `fetchIdentifier`: The identifier of the request as returned by  .

## See Also

- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](ekeventstore/enumerateevents(matching:using:).md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](ekeventstore/events(matching:).md)
  Finds all events that match a given predicate.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](ekeventstore/fetchreminders(matching:completion:).md)
  Fetches reminders that match a given predicate.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/cancelfetchrequest(_:))*