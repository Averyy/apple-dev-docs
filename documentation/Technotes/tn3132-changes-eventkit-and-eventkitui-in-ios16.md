# TN3132: Changes to EventKit and EventKitUI in iOS 16

**Framework**: Technotes

Test your apps against EventKit and EventKitUI API changes in iOS 16.

#### Overview

The iOS 16 SDK introduces some changes to the EventKit and EventKitUI frameworks. This document highlights some of the major changes. To learn about related changes in macOS Ventura 13, see [`TN3130: Changes to EventKit in macOS Ventura 13`](tn3130-changes-to-eventkit-in-macos13-ventura.md).

For apps running on systems prior to iOS 16, built with Xcode 13 or earlier and linked against older versions of the iOS SDK, the legacy behavior remains in place when using these frameworks. When you run your app on iOS 16, and have built it with Xcode 14 and linked against the iOS 16 SDK, you may see behavior that you are unfamiliar with when using EventKit or EventKitUI. To identify these changes in behavior, thoroughly test your app on each major OS version it supports on real hardware. Confirm that your implementation of EventKit or EventKitUI behaves as you expect in each OS version and update your code where needed.
If you notice an unexpected behavior in EventKit, report it using [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/).

#### Ekcalendarchooser

Setting the [`selectedCalendars`](https://developer.apple.com/documentation/EventKitUI/EKCalendarChooser/selectedCalendars) property of a calendar chooser view controller no longer calls the [`calendarChooserSelectionDidChange(_:)`](https://developer.apple.com/documentation/EventKitUI/EKCalendarChooserDelegate/calendarChooserSelectionDidChange(_:)) delegate method. `calendarChooserSelectionDidChange(_:)` is only called when the user selects a calendar in the view controller.

#### Ekeventstore

##### Committing Changes

When you call [`saveCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/saveCalendar(_:commit:)), [`removeCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/removeCalendar(_:commit:)), [`save(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:span:commit:)), [`remove(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:span:commit:)), [`save(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:commit:)), or [`remove(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:commit:)) methods with the `commit` parameter set to `true`, [`EKEventStore`](https://developer.apple.com/documentation/EventKit/EKEventStore) attempts to immediatedly save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that have been saved but aren’t yet committed to the event store.

In the legacy behavior, objects remain saved but uncommitted in the event store when the commit failed.

##### Fetching Events

[`events(matching:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/events(matching:)) and [`enumerateEvents(matching:using:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/enumerateEvents(matching:using:)) now return events that have been saved but weren’t yet committed to the event store.

In the legacy behavior, `events(matching:)` and `enumerateEvents(matching:using:)` only return events that have been saved and committed to the event store.

##### Recurring Events

If you are saving a detached occurrence of a recurring event, and you specify [`EKSpan.futureEvents`](https://developer.apple.com/documentation/EventKit/EKSpan/futureEvents) for the `span` parameter of the [`save(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:span:commit:)) method, your changes apply to all future occurrences of the event.

In the legacy behavior, your changes only apply to this instance of the recurring event.

#### Revision History

-  First published.

## See Also

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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3132-changes-eventkit-and-eventkitui-in-ios16)*