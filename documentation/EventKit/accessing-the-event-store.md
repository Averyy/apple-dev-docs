# Accessing the event store

**Framework**: Eventkit

Request access to a person’s calendar data through the event store.

#### Overview

Your app must obtain permission from the person using the app before it can access the calendar database: your app must never directly modify the calendar database on its own. [`EKEventStore`](ekeventstore.md) is the app’s way of accessing calendar and reminder data.

Your app should only request the access it needs to complete its tasks. You can request write-only access to events, which lets your app create new events but doesn’t let it read any events or other calendar information, including events your app created. You can also request full access to either events or reminders, which lets your app create, view, edit, and delete data.

> **Note**:  Your app can’t request read-only access to either events or reminders. To read events or reminders from the event store, your app needs full access.

##### Connect to the Event Store

To receive event or reminder data, you must request access to an entity type after initializing the event store. To request access to reminders, use [`requestFullAccessToReminders(completion:)`](ekeventstore/requestfullaccesstoreminders(completion:).md). To request access to events, use [`requestWriteOnlyAccessToEvents(completion:)`](ekeventstore/requestwriteonlyaccesstoevents(completion:).md) or [`requestFullAccessToEvents(completion:)`](ekeventstore/requestfullaccesstoevents(completion:).md), depending on the level of access your app needs.

For example, to request full access to reminders, use the following:

Releasing an event store instance before other EventKit objects may result in an error.

##### Use Eventkit with Write Only Calendar Access

Your app can use the entire EventKit calendar API when it has write-only calendar access. If your app has write-only access, a request for a list of calendars returns a single virtual calendar, that doesn’t represent any real calendar in the event store. Requests for events on the virtual calendar return no results. When your app creates an event, EventKit saves it to a calendar that’s chosen by the person using your app.

[`EventKit UI`](https://developer.apple.com/documentation/EventKitUI) presents chooser and editor UI outside of your app’s process on iOS 17 and later. Your app can use [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI) without requesting write-only or full calendar access. The chooser and editor UI has full access to calendars on the device regardless of the access granted to your app. If your app needs to present UI for creating and editing calendar events, consider using [`EventKit UI`](https://developer.apple.com/documentation/EventKitUI) instead of requesting full access to calendar data. Create an event, then present an [`EKEventEditViewController`](https://developer.apple.com/documentation/EventKitUI/EKEventEditViewController) to allow people to edit and save the event. [`EKEventEditViewController`](https://developer.apple.com/documentation/EventKitUI/EKEventEditViewController) saves the event to the calendar the person requests in the editor UI.

##### Protect User Privacy with Information Property List Keys

An iOS app must include in its `Info.plist` file the usage description keys for the types of data it needs to access. On iOS 17 and later, to access a person’s calendar events or reminders, you need to include descriptions for:

- `NSCalendarsWriteOnlyAccessUsageDescription` or `NSCalendarsFullAccessUsageDescription`, depending on the level of access to events your app needs. Don’t request full access if your app’s features only need write-only access.
- `NSRemindersFullAccessUsageDescription`, if your app needs access to reminders.

> ❗ **Important**:  On iOS 17 or later, if your app doesn’t include usage description keys, or only includes the older [`NSCalendarsUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCalendarsUsageDescription) key for describing events access, iOS automatically denies any access request.

To access a person’s calendar events or reminders through EventKit or EventKit UI, your app needs to include descriptions for the following if your app links to iOS 10 or later, and runs on iOS 10 through iOS 16:

- [`NSCalendarsUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCalendarsUsageDescription), which is a fallback if your app runs on iOS 17 or later and doesn’t include descriptions for [`NSCalendarsWriteOnlyAccessUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCalendarsWriteOnlyAccessUsageDescription) or [`NSCalendarsFullAccessUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCalendarsFullAccessUsageDescription).
- [`NSRemindersUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRemindersUsageDescription), which is a fallback if your app runs on iOS 17 or later and doesn’t include a description for [`NSRemindersFullAccessUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSRemindersFullAccessUsageDescription).
- [`NSContactsUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSContactsUsageDescription), as EventKit UI may need to access Contacts data to choose the correct display name or avatar for a contact in a calendar.

> ⚠️ **Warning**:  If your app that’s linked on iOS 10 through iOS 16 doesn’t include these keys, your app crashes.

Because these keys provide access to the event store, they protect the person’s privacy by only allowing access to this information if they explicitly grant permission in the app.

To access Calendar data, all sandboxed macOS apps must include the `com.apple.security.personal-information.calendars` entitlement.

## See Also

- [class EKEventStore](ekeventstore.md)
  An object that accesses a person’s calendar events and reminders and supports the scheduling of new events.
- [Accessing Calendar using EventKit and EventKitUI](accessing-calendar-using-eventkit-and-eventkitui.md)
  Choose and implement the appropriate Calendar access level in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/EventKit/accessing-the-event-store)*