# predicateForEvents(withStart:end:calendars:)

**Framework**: EventKit  
**Kind**: method

Creates a predicate to identify events that occur within a given date range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func predicateForEvents(withStart startDate: Date, end endDate: Date, calendars: [EKCalendar]?) -> NSPredicate
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)

#### Return Value

A predicate to use when calling [`enumerateEvents(matching:using:)`](ekeventstore/enumerateevents(matching:using:).md) or [`events(matching:)`](ekeventstore/events(matching:).md).

#### Discussion

Use this method to create a predicate for use with [`events(matching:)`](ekeventstore/events(matching:).md) or [`enumerateEvents(matching:using:)`](ekeventstore/enumerateevents(matching:using:).md). The events returned using this predicate are in the default time zone. For performance reasons, this method matches only those events within a four-year time span. If the date range between `startDate` and `endDate` is greater than four years, it’s shortened to the first four years.

## Parameters

- `startDate`: The start date of the range of events fetched.
- `endDate`: The end date of the range of events fetched.
- `calendars`: An array of calendars to search, or   to search all calendars.

## See Also

- [func enumerateEvents(matching: NSPredicate, using: EKEventSearchCallback)](ekeventstore/enumerateevents(matching:using:).md)
  Finds all events that match a given predicate and calls a given callback for each event found.
- [func events(matching: NSPredicate) -> [EKEvent]](ekeventstore/events(matching:).md)
  Finds all events that match a given predicate.
- [func fetchReminders(matching: NSPredicate, completion: ([EKReminder]?) -> Void) -> Any](ekeventstore/fetchreminders(matching:completion:).md)
  Fetches reminders that match a given predicate.
- [func cancelFetchRequest(Any)](ekeventstore/cancelfetchrequest(_:).md)
  Cancels the request to fetch reminders.
- [func predicateForReminders(in: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforreminders(in:).md)
  Creates a predicate to identify all reminders in a collection of calendars.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforcompletedreminders(withcompletiondatestarting:ending:calendars:).md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforincompletereminders(withduedatestarting:ending:calendars:).md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.
- [typealias EKEventSearchCallback](ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/predicateforevents(withstart:end:calendars:))*