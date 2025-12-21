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

When you call [`saveCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/saveCalendar(_:commit:)), [`removeCalendar(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/removeCalendar(_:commit:)), [`save(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:span:commit:)), [`remove(_:span:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:span:commit:)), [`save(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/save(_:commit:)), or [`remove(_:commit:)`](https://developer.apple.com/documentation/EventKit/EKEventStore/remove(_:commit:)) methods with the `commit` parameter set to `true`, [`EKEventStore`](https://developer.apple.com/documentation/EventKit/EKEventStore) attempts to immediately save and commit your changes to the event store. If the commit fails, `EKEventStore` automatically rolls back all changes that have been saved but aren’t yet committed to the event store.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3132-changes-eventkit-and-eventkitui-in-ios16)*