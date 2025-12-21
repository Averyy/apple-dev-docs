# TN3130: Changes to EventKit in macOS Ventura 13

**Framework**: Technotes

Test your apps against EventKit API changes in macOS Ventura 13.

#### Overview

In macOS Ventura 13, the EventKit framework has seen significant changes. This document highlights some of the notable changes. To learn about related changes in iOS 16, see [`TN3132: Changes to EventKit and EventKitUI in iOS 16`](tn3132-changes-eventkit-and-eventkitui-in-ios16.md).

For apps running on systems prior to macOS Ventura 13, the legacy behavior remains in place when using EventKit. When you run your app on macOS Ventura 13, and have built it with Xcode 14 and linked against the macOS 13 SDK, you may see behavior that you are unfamiliar with when using EventKit. To identify these changes in behavior, thoroughly test your app for each major OS version it supports. Confirm that your implementation of EventKit behaves as you expect in each OS version and update your code where needed. If you notice an unexpected behavior in EventKit, report it using [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

#### Ekcalendar

The inherited initializer `init()` throws an exception when attempting to create a new calendar. Use [`init(for:eventStore:)`](https://developer.apple.com/documentation/EventKit/EKCalendar/init(for:eventStore:)) instead.

```swift
let calendar = EKCalendar(for: .event, eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKCalendar` object.

#### Ekcalendaritem

##### Fetching Recurrence Rules

The [`recurrenceRules`](https://developer.apple.com/documentation/EventKit/EKCalendarItem/recurrenceRules) property returns an empty array if the calendar item doesn’t have any recurrence rules.

In the legacy behavior, `recurrenceRules` returns `nil` if the calendar item doesn’t have any recurrence rules.

##### Updating Time Zones

Changing the time zone of an event no longer changes the absolute time at which it occurs.

#### Ekevent

##### Creating Events

The inherited initializer `init()` throws an exception when attempting to create a new event. Use [`init(eventStore:)`](https://developer.apple.com/documentation/EventKit/EKEvent/init(eventStore:)) to create new events.

In the legacy behavior, this inherited initializer returns an unusable `EKEvent` object.

##### Event Identifiers

The [`eventIdentifier`](https://developer.apple.com/documentation/EventKit/EKEvent/eventIdentifier) property now returns identifiers in a new format. The previous identifier format will continue to work.

##### End Date of All Day Events

The [`endDate`](https://developer.apple.com/documentation/EventKit/EKEvent/endDate) property of all-day events returns a time of `11:59:59 PM` on the last day of this event.

```json
Event title: Marathon  
Start date: June 18, 2022 at 12:00:00 AM PDT
End date: June 18, 2022 at 11:59:59 PM PDT
```

In the legacy behavior, this property returns a time of `12:00:00 AM` on the day after the event.

```json
Event title: Marathon  
Start date: June 18, 2022 at 12:00:00 AM PDT
End date: June 19, 2022 at 12:00:00 AM PDT
```

#### Ekeventstore

##### Accessing Sources

The [`sources`](https://developer.apple.com/documentation/EventKit/EKEventStore/sources) property now contains delegate sources.

```swift
// Fetch all sources associated with the event store.
let sources = eventStore.sources

sources.forEach { source in
    // Let's check whether source is a delegate event source.
    let name = (source.isDelegate) ? "Delegate Source" : "Source"
    print("\(name): \(source.title)")
}
// Prints "Source: iCloud"
// Prints "Delegate Source: Calculus Office Hours"
```

##### Fetching Events

[`events(matching:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/events(matching:)) and [`enumerateEvents(matching:using:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/enumerateEvents(matching:using:)) no longer necessarily return events sorted by start date.

##### Accessing Calendar Events

The [`calendarItem(withIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/calendarItem(withIdentifier:)), [`calendarItems(withExternalIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/calendarItems(withExternalIdentifier:)), and [`event(withIdentifier:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/event(withIdentifier:)) methods may return different occurrences of an event or reminder with a given identifier in some cases. For instance, when the first occurrence of a recurring event was modified and the specified identifier refers to this occurrence. In this case, use the given identifier to fetch the unmodified version of the event’s first occurrence.

##### Committing Changes

When you call [`saveCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/saveCalendar(_:commit:)), [`removeCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/removeCalendar(_:commit:)), [`save(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:span:commit:)), [`remove(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:span:commit:)), [`save(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:commit:)), or [`remove(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:commit:)) methods with the `commit` parameter set to `true`, [`EKEventStore`](https://developer.apple.com/documentation/EventKit/EKEventStore) attempts to immediately save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that been saved but aren’t yet committed to the event store.

In the legacy behavior, uncommitted objects remain saved in the event store.

#### Ekreminder

The inherited initializer `init()` throws an exception when attempting to create a new reminder. Use [`init(eventStore:)`](https://developer.apple.com/documentation/EventKit/EKReminder/init(eventStore:)) instead.

```swift
let reminder = EKReminder(eventStore: eventStore)
```

In the legacy behavior, this inherited initializer returns an unusable `EKReminder` object.

#### Eksource

The [`isDelegate`](https://developer.apple.com/documentation/EventKit/EKSource/isDelegate) property indicates whether the source is an event source delegated to the user.

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3130-changes-to-eventkit-in-macos13-ventura)*