# EKEventStore

**Framework**: EventKit  
**Kind**: class

An object that accesses a person’s calendar events and reminders and supports the scheduling of new events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKEventStore
```

## Mentions

- [Retrieving events and reminders](retrieving-events-and-reminders.md)
- [Accessing the event store](accessing-the-event-store.md)
- [Creating events and reminders](creating-events-and-reminders.md)

#### Overview

The `EKEventStore` class is an app’s point of contact for accessing calendar and reminder data.

After initializing the event store, you must request access to events or reminders before attempting to fetch or create data. To request access to reminders, call [`requestFullAccessToReminders(completion:)`](ekeventstore/requestfullaccesstoreminders(completion:).md). To request access to events, call [`requestWriteOnlyAccessToEvents(completion:)`](ekeventstore/requestwriteonlyaccesstoevents(completion:).md) or [`requestFullAccessToEvents(completion:)`](ekeventstore/requestfullaccesstoevents(completion:).md).

> ❗ **Important**:  To request access to events and reminders, your app needs to include permission strings in its `Info.plist` file that explain to someone why the app needs access. For more information, see [`Accessing the event store`](accessing-the-event-store.md).

 To request access to events and reminders, your app needs to include permission strings in its `Info.plist` file that explain to someone why the app needs access. For more information, see [`Accessing the event store`](accessing-the-event-store.md).

A typical workflow for using an event store is:

1. Create a predicate, or a search query for events, with [`predicateForEvents(withStart:end:calendars:)`](ekeventstore/predicateforevents(withstart:end:calendars:).md).
2. Fetch and process events that match the predicate with the [`events(matching:)`](ekeventstore/events(matching:).md) and [`enumerateEvents(matching:using:)`](ekeventstore/enumerateevents(matching:using:).md) methods.
3. Save and delete events from the event store with the [`save(_:span:commit:)`](ekeventstore/save(_:span:commit:).md) and [`remove(_:span:commit:)`](ekeventstore/remove(_:span:commit:).md) methods.

Use similar methods to access and manipulate reminders.

After receiving an object from an event store, don’t use that object with a different event store. This restriction applies to [`EKObject`](ekobject.md) subclasses such as [`EKEvent`](ekevent.md), [`EKReminder`](ekreminder.md), [`EKCalendar`](ekcalendar.md), and [`EKSource`](eksource.md), as well as predicates that the event store creates. For example, don’t fetch an event from one event store, modify the event, and then pass it to [`save(_:span:)`](ekeventstore/save(_:span:).md) in a different store.

## Topics

### Creating event stores
- [init()](ekeventstore/init.md)
  Creates a new event store.
- [init(sources: [EKSource])](ekeventstore/init(sources:).md)
  Creates an event store that contains data for the specified sources.
- [var eventStoreIdentifier: String](ekeventstore/eventstoreidentifier.md)
  The unique identifier for the event store.
### Requesting access to events and reminders
- [func requestWriteOnlyAccessToEvents(completion: EKEventStoreRequestAccessCompletionHandler)](ekeventstore/requestwriteonlyaccesstoevents(completion:).md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: EKEventStoreRequestAccessCompletionHandler)](ekeventstore/requestfullaccesstoevents(completion:).md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: EKEventStoreRequestAccessCompletionHandler)](ekeventstore/requestfullaccesstoreminders(completion:).md)
  Prompts people to grant or deny read and write access to reminders.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](ekeventstore/authorizationstatus(for:).md)
  Determines the authorization status for the given entity type.
- [enum EKAuthorizationStatus](ekauthorizationstatus.md)
  The current authorization status for a specific entity type.
- [typealias EKEventStoreRequestAccessCompletionHandler](ekeventstorerequestaccesscompletionhandler.md)
  The signature for a closure that EventKit calls when requesting access to event and reminder data.
- [NSCalendarsFullAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsWriteOnlyAccessUsageDescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../BundleResources/Information-Property-List/NSRemindersFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.
### Accessing account sources
- [var sources: [EKSource]](ekeventstore/sources.md)
  An unordered array of objects that represent accounts that contain calendars.
- [var delegateSources: [EKSource]](ekeventstore/delegatesources.md)
  The event sources delegated to the person using your app.
- [func source(withIdentifier: String) -> EKSource?](ekeventstore/source(withidentifier:).md)
  Locates an event source with the specified identifier.
### Saving and restoring state
- [func commit() throws](ekeventstore/commit.md)
  Commits all unsaved changes to the event store.
- [func reset()](ekeventstore/reset.md)
  Reverts the event store to its saved state.
- [func refreshSourcesIfNecessary()](ekeventstore/refreshsourcesifnecessary.md)
  Pulls new data from remote sources, if necessary.
### Accessing calendars
- [var defaultCalendarForNewEvents: EKCalendar?](ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](ekeventstore/defaultcalendarfornewreminders.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](ekeventstore/calendars(for:).md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func calendar(withIdentifier: String) -> EKCalendar?](ekeventstore/calendar(withidentifier:).md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](ekeventstore/savecalendar(_:commit:).md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](ekeventstore/removecalendar(_:commit:).md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](ekeventstore/calendars.md)
  The calendars associated with the event store.
### Accessing calendar events
- [func event(withIdentifier: String) -> EKEvent?](ekeventstore/event(withidentifier:).md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](ekeventstore/calendaritem(withidentifier:).md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](ekeventstore/calendaritems(withexternalidentifier:).md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](ekeventstore/remove(_:span:).md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/remove(_:span:commit:).md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func remove(EKReminder, commit: Bool) throws](ekeventstore/remove(_:commit:).md)
  Removes a reminder from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan) throws](ekeventstore/save(_:span:).md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](ekeventstore/save(_:span:commit:).md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](ekeventstore/save(_:commit:).md)
  Saves changes to a reminder by either committing or batching the changes.
### Searching calendars
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
- [func predicateForReminders(in: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforreminders(in:).md)
  Creates a predicate to identify all reminders in a collection of calendars.
- [func predicateForCompletedReminders(withCompletionDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforcompletedreminders(withcompletiondatestarting:ending:calendars:).md)
  Creates a predicate to identify all completed reminders that occur within a given date range.
- [func predicateForIncompleteReminders(withDueDateStarting: Date?, ending: Date?, calendars: [EKCalendar]?) -> NSPredicate](ekeventstore/predicateforincompletereminders(withduedatestarting:ending:calendars:).md)
  Creates a predicate to identify all incomplete reminders that occur within a given date range.
- [typealias EKEventSearchCallback](ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.
### Deprecated methods
- [func requestAccess(to: EKEntityType, completion: EKEventStoreRequestAccessCompletionHandler)](ekeventstore/requestaccess(to:completion:).md)
  Prompts the person using your app to grant or deny access to event or reminder data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Accessing the event store](accessing-the-event-store.md)
  Request access to a person’s calendar data through the event store.
- [Accessing Calendar using EventKit and EventKitUI](accessing-calendar-using-eventkit-and-eventkitui.md)
  Choose and implement the appropriate Calendar access level in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore)*