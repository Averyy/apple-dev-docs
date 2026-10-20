# EKEventStore

**Framework**: EventKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface EKEventStore : NSObject
```

## Mentions

- [Retrieving events and reminders](./retrieving-events-and-reminders.md)
- [Accessing the event store](./accessing-the-event-store.md)
- [Creating events and reminders](./creating-events-and-reminders.md)

#### Overview

The `EKEventStore` class is an app’s point of contact for accessing calendar and reminder data.

After initializing the event store, you must request access to events or reminders before attempting to fetch or create data. To request access to reminders, call [`requestFullAccessToReminders(completion:)`](./ekeventstore/requestfullaccesstoreminders%28completion%29.md). To request access to events, call [`requestWriteOnlyAccessToEvents(completion:)`](./ekeventstore/requestwriteonlyaccesstoevents%28completion%29.md) or [`requestFullAccessToEvents(completion:)`](./ekeventstore/requestfullaccesstoevents%28completion%29.md).

> ❗ **Important**:  To request access to events and reminders, your app needs to include permission strings in its `Info.plist` file that explain to someone why the app needs access. For more information, see [Accessing the event store](./accessing-the-event-store.md).

A typical workflow for using an event store is:

1. Create a predicate, or a search query for events, with [`predicateForEvents(withStart:end:calendars:)`](./ekeventstore/predicateforevents%28withstart,end,calendars%29.md).
2. Fetch and process events that match the predicate with the [`events(matching:)`](./ekeventstore/events%28matching%29.md) and [`enumerateEvents(matching:using:)`](./ekeventstore/enumerateevents%28matching,using%29.md) methods.
3. Save and delete events from the event store with the [`save(_:span:commit:)`](./ekeventstore/save%28_,span,commit%29.md) and [`remove(_:span:commit:)`](./ekeventstore/remove%28_,span,commit%29.md) methods.

Use similar methods to access and manipulate reminders.

After receiving an object from an event store, don’t use that object with a different event store. This restriction applies to [`EKObject`](./ekobject.md) subclasses such as [`EKEvent`](./ekevent.md), [`EKReminder`](./ekreminder.md), [`EKCalendar`](./ekcalendar.md), and [`EKSource`](./eksource.md), as well as predicates that the event store creates. For example, don’t fetch an event from one event store, modify the event, and then pass it to [`save(_:span:)`](./ekeventstore/save%28_,span%29.md) in a different store.

## Topics

### Creating event stores
- [init()](./ekeventstore/init%28%29.md)
  Creates a new event store.
- [init(sources: [EKSource])](./ekeventstore/init%28sources%29.md)
  Creates an event store that contains data for the specified sources.
- [var eventStoreIdentifier: String](./ekeventstore/eventstoreidentifier.md)
  The unique identifier for the event store.
### Requesting access to events and reminders
- [func requestWriteOnlyAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestwriteonlyaccesstoevents%28completion%29.md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestfullaccesstoevents%28completion%29.md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestfullaccesstoreminders%28completion%29.md)
  Prompts people to grant or deny read and write access to reminders.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](./ekeventstore/authorizationstatus%28for%29.md)
  Determines the authorization status for the given entity type.
- [enum EKAuthorizationStatus](./ekauthorizationstatus.md)
  The current authorization status for a specific entity type.
- [typealias EKEventStoreRequestAccessCompletionHandler](./ekeventstorerequestaccesscompletionhandler.md)
  The signature for a closure that EventKit calls when requesting access to event and reminder data.
- [NSCalendarsFullAccessUsageDescription](../BundleResources/information-property-list/nscalendarsfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/information-property-list/nscalendarswriteonlyaccessusagedescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../BundleResources/information-property-list/nsremindersfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.
### Accessing account sources
- [var sources: [EKSource]](./ekeventstore/sources.md)
  An unordered array of objects that represent accounts that contain calendars.
- [var delegateSources: [EKSource]](./ekeventstore/delegatesources.md)
  The event sources delegated to the person using your app.
- [func source(withIdentifier: String) -> EKSource?](./ekeventstore/source%28withidentifier%29.md)
  Locates an event source with the specified identifier.
### Saving and restoring state
- [func commit() throws](./ekeventstore/commit%28%29.md)
  Commits all unsaved changes to the event store.
- [func reset()](./ekeventstore/reset%28%29.md)
  Reverts the event store to its saved state.
- [func refreshSourcesIfNecessary()](./ekeventstore/refreshsourcesifnecessary%28%29.md)
  Pulls new data from remote sources, if necessary.
### Accessing calendars
- [var defaultCalendarForNewEvents: EKCalendar?](./ekeventstore/defaultcalendarfornewevents.md)
  The calendar that events are added to by default, as specified by user settings.
- [func defaultCalendarForNewReminders() -> EKCalendar?](./ekeventstore/defaultcalendarfornewreminders%28%29.md)
  Identifies the default calendar for adding reminders to, as specified by user settings.
- [func calendars(for: EKEntityType) -> [EKCalendar]](./ekeventstore/calendars%28for%29.md)
  Identifies the calendars that support a given entity type, such as reminders or events.
- [func calendar(withIdentifier: String) -> EKCalendar?](./ekeventstore/calendar%28withidentifier%29.md)
  Locates a calendar with the specified identifier.
- [func saveCalendar(EKCalendar, commit: Bool) throws](./ekeventstore/savecalendar%28_,commit%29.md)
  Saves a calendar to the event store by either committing or batching the changes.
- [func removeCalendar(EKCalendar, commit: Bool) throws](./ekeventstore/removecalendar%28_,commit%29.md)
  Removes a calendar from the event store by either committing or batching the changes.
- [var calendars: [EKCalendar]](./ekeventstore/calendars.md)
  The calendars associated with the event store.
### Accessing calendar events
- [func event(withIdentifier: String) -> EKEvent?](./ekeventstore/event%28withidentifier%29.md)
  Locates the first occurrence of an event with a given identifier.
- [func calendarItem(withIdentifier: String) -> EKCalendarItem?](./ekeventstore/calendaritem%28withidentifier%29.md)
  Locates a reminder or the first occurrence of an event with the specified identifier.
- [func calendarItems(withExternalIdentifier: String) -> [EKCalendarItem]](./ekeventstore/calendaritems%28withexternalidentifier%29.md)
  Locates all reminders or the first occurrences of all events with the specified external identifier.
- [func remove(EKEvent, span: EKSpan) throws](./ekeventstore/remove%28_,span%29.md)
  Removes an event from the event store.
- [func remove(EKEvent, span: EKSpan, commit: Bool) throws](./ekeventstore/remove%28_,span,commit%29.md)
  Removes an event or recurring events from the event store by either committing or batching the changes.
- [func remove(EKReminder, commit: Bool) throws](./ekeventstore/remove%28_,commit%29.md)
  Removes a reminder from the event store by either committing or batching the changes.
- [func save(EKEvent, span: EKSpan) throws](./ekeventstore/save%28_,span%29.md)
  Saves changes to an event permanently.
- [func save(EKEvent, span: EKSpan, commit: Bool) throws](./ekeventstore/save%28_,span,commit%29.md)
  Saves an event or recurring events to the event store by either committing or batching the changes.
- [func save(EKReminder, commit: Bool) throws](./ekeventstore/save%28_,commit%29.md)
  Saves changes to a reminder by either committing or batching the changes.
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
- [typealias EKEventSearchCallback](./ekeventsearchcallback.md)
  The signature for a closure that operates on events when enumerating them.
### Deprecated methods
- [func requestAccess(to: EKEntityType, completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestaccess%28to,completion%29.md)
  Prompts the person using your app to grant or deny access to event or reminder data.
### Structures
- [EKEventStore.EventStoreChanged](./ekeventstore/eventstorechanged.md)
  A notification posted when changes are made to the Calendar or Reminders database.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Accessing the event store](./accessing-the-event-store.md)
  Request access to a person’s calendar data through the event store.
- [Accessing Calendar using EventKit and EventKitUI](./accessing-calendar-using-eventkit-and-eventkitui.md)
  Choose and implement the appropriate Calendar access level in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore)*