# TN3153: Adopting API changes for EventKit in iOS 17, macOS 14, and watchOS 10

**Framework**: Technotes

Test your existing apps against EventKit API latest changes.

#### Overview

Xcode 15 includes SDKs for iOS 17, macOS 14, and watchOS 10 that introduce notable changes in EventKit such as new access levels: the ability to add events using EventKitUI without requesting access to Calendar, write-only access, and full access. Apps that don’t request access to calendar data use [`EKEventEditViewController`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller) to present UI for editing an event, which the person using your app can save. See [`Accessing the Event Store`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/accessing_the_event_store) for details. If the user grants your app write-only access, your app can create and write calendar events. However, your app can’t read or delete any events from the user’s calendars,  including the ones it creates. If the user grants your app full access, your app can read, write, create, and delete calendar events as in iOS 16 and earlier, for example. To learn how to update your app to use these new features, see [`TN3152: Migrating to the latest Calendar access levels`](tn3152-migrating-to-the-latest-calendar-access-levels.md).

If you built your app with an older version of Xcode 15 such as Xcode 14.3.1 and linked it against older versions of the iOS, macOS, or watchOS SDK, and run it on iOS 17, macOS 14, or watchOS 10, you may see behavior that you are unfamiliar with when using EventKit or EventKitUI. For instance, your app may not be able to fetch events even if the user previously granted full access to the app on an earlier OS version.

This document describes how some of these changes may affect your app. To identify these changes in behavior, thoroughly test your app for each major OS version it supports. Confirm that your usage of EventKit or EventKitUI behaves as you expect in each OS version and update your code where needed. If you notice an unexpected behavior in these frameworks, report it using [`Feedback Assistant`](https://developer.apple.comhttps://developer.apple.com/bug-reporting).

#### Calendar Usage Description Keys

The [`NSCalendarsUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarsusagedescription) and [`NSRemindersUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsremindersusagedescription) keys describe how your app  intends to use the user’s calendar data or reminders, respectively. If your app runs on iOS 17, macOS 14, watchOS 10, or later and doesn’t include the new [`NSCalendarsWriteOnlyAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarswriteonlyaccessusagedescription) or [`NSCalendarsFullAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarsfullaccessusagedescription) key, EventKit uses `NSCalendarsUsageDescription` as fallback. If your app doesn’t include the new [`NSRemindersFullAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsremindersfullaccessusagedescription) key, EventKit uses `NSRemindersUsageDescription` as fallback.

#### Requesting Permission From the User

If your app links against an SDK older than the iOS 17 SDK, macOS 14 SDK, or watchOS 10 SDK and hasn’t previously prompted the user for calendar access,

 Calling [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) or [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) with an entity type `event` prompts the user to grant write-only calendar access to your app. If the user allows write-only access to your app and your app used `requestAccess(to:completion:)`, the system calls the [`EKEventStoreRequestAccessCompletionHandler`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler) completion handler with its boolean parameter set to `true`.

```swift
let eventStore = EKEventStore()
eventStore.requestAccess(to: .event, completion: {(granted, error) in
    if granted {
      // Fetch latest events.
    }
})
```

If the app called `requestAccess(to:)`, the system asynchronously returns a boolean value set to `true`.

```swift
let eventStore = EKEventStore()
let response = try await eventStore.requestAccess(to: .event)
if response {
    // Fetch latest events.
}
```

If the user denies access, the completion handler receives a `false` parameter and `requestAccess(to:)` returns `false`.

 Calling these methods with an entity type `event` prompts the user to grant full calendar access to your app.

> **Note**: If the user previously granted write-only access to the iOS companion app, calling [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) or [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) for events in the watchOS app doesn’t prompt the user for access. The access level of the watchOS app matches its companion app, which is write-only.

#### Authorization Status

An app with write-only or full access to calendar events will see its authorization status as [`authorized`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/authorized). If the user previously granted calendar access (`authorized`) to your app, calling [`authorizationStatus(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus) with an entity type [`event`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekentitytype/event) returns `authorized`.

```swift
EKEventStore.authorizationStatus(for: .event) == .authorized
```

The iOS, macOS, and watchOS SDKs bundled in Xcode 15 provide different levels of access: [`writeOnly`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/writeonly)  and [`fullAccess`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/fullaccess). In an app linked against an SDK older than the iOS 17 SDK, macOS 14 SDK, or watchOS 10 SDK, `writeOnly` and `fullAccess` both map to `authorized`.

If the user previously granted calendar access to your app on an earlier OS, your app will have write-only access.

> **Note**: Implement the new APIs if you want to distinguish between the `writeOnly` and `fullAccess` access levels in your app.

#### Existing Apps with Write Only Calendar Access

If the user granted write-only access to your app,

- The [`sources`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507315-sources) property returns a single virtual source.
- The [`delegateSources`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507419-delegatesources) property returns an empty array.
- The [`defaultCalendarForNewEvents`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507062-defaultcalendarfornewevents) property returns a single virtual calendar. The [`calendars(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507128-calendars) method on [`EKEventStore`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore) and [`EKSource`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/eksource) returns the same virtual calendar.

An app with write-only access may later request full access. The first time your app calls the [`calendarItemWithIdentifier:`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritemwithidentifier),
[`calendarItemsWithExternalIdentifier:`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritemswithexternalidentif), [`enumerateEvents(matching:using:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateevents), [`events(matching:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events), or [`event(withIdentifier:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507490-event) instance methods, it implicitly prompts the user to upgrade the app to full access or keep it write-only access. If the user grants full access to the app, an [`EKEventStoreChanged`](https://developer.apple.comhttps://developer.apple.com/documentation/foundation/nsnotification/name/1507525-ekeventstorechanged) notification is posted, these methods return some results, and the app has a full access authorization status. When your app receives the event store notification, refetch all calendar data that your app needs to refresh its views. These data are now visible to your app.

If the user denies access, these methods don’t return any results, and any further calls don’t prompt the user for access again. Your app still has write-only calendar access.

> **Note**: If your app doesn’t call [`calendarItemWithIdentifier:`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507433-calendaritemwithidentifier), [`calendarItemsWithExternalIdentifier:`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507281-calendaritemswithexternalidentif), [`enumerateEvents(matching:using:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507518-enumerateevents), [`events(matching:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507183-events), or [`event(withIdentifier:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507490-event) to implicitly prompt the user for upgrade, the user would have to know to change the access level for the app in Settings > Privacy & Security > Calendars on their device.

#### Revision History

-  Made minor editorial changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3153-adopting-api-changes-for-eventkit-in-ios-macos-and-watchos)*