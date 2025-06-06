# TN3152: Migrating to the latest Calendar access levels

**Framework**: Technotes

Follow these guidelines to update your app to use the new Calendar access levels.

#### Overview

The EventKit framework brings new Calendar access levels in iOS 17, iPadOS 17, macOS 14, Mac Catalyst 17, watchOS 10, and later. The EventKitUI framework provides the ability to add events without requesting access to Calendar in iOS 17, iPadOS 17, Mac Catalyst 17, and later. See [`Accessing the Event Store`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/accessing_the_event_store) for details. This document describes how to update your app to use these new features. To learn how these changes may affect your existing apps, see [`TN3153: Adopting API changes for EventKit in iOS 17, macOS 14, and watchOS 10`](tn3153-adopting-api-changes-for-eventkit-in-ios-macos-and-watchos.md). Follow these guidelines to support the new features:

- If your app can present [`EKEventEditViewController`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller) to let people create events, don’t request access to events.
- If your app needs to create and save calendar data directly without the user making any later changes, request write-only access to calendar data.
- If accessing existing events is essential to the core experience of your app, request full access to calendar data.
- If your app accesses reminder data, request full access to reminders in your app.

 Xcode 15 includes SDKs for iOS 17, macOS 14, and watchOS 10 that provide the new write-only and full access features. For instance, if you are building an iOS app, link your app against the iOS 17 SDK or later. If you are building a watchOS app, link your app against the watchOS 10 SDK or later.

 Prior to iOS 17, your app needs to include the [`NSCalendarsUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarsusagedescription), [`NSRemindersUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsremindersusagedescription), and [`NSContactsUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscontactsusagedescription) keys in its `Info.plist` file before it can access the user’s calendar data or reminders. `NSCalendarsUsageDescription` and `NSRemindersUsageDescription` describe how your app intends to use the user’s calendar data or reminders, respectively. You provide a `NSContactsUsageDescription` key when your app uses EventKit UI to access Contacts data. If your app supports earlier versions of an OS, keep the key currently available in your app’s `Info.plist` file.

If your app requires running on iOS 17, iPadOS 17, macOS 14, Mac Catalyst 17, watchOS 10, or later, remove these keys from the plist file. Add [`NSCalendarsWriteOnlyAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarswriteonlyaccessusagedescription) or [`NSCalendarsFullAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nscalendarsfullaccessusagedescription) to the plist file, depending on the level of access to events your app needs. Include [`NSRemindersFullAccessUsageDescription`](https://developer.apple.comhttps://developer.apple.com/documentation/bundleresources/information_property_list/nsremindersfullaccessusagedescription) if your app needs access to reminders. See [`Protect user privacy with information property  list keys`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/accessing_the_event_store#2975207) for details.

 If your app checks its authorization status for events [`EKEventStore.authorizationStatus(for: .event)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507239-authorizationstatus), update it to handle the new [`writeOnly`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/writeonly) and [`fullCase`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/fullaccess) cases. Remove the deprecated [`authorized`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekauthorizationstatus/1451886-authorized) case from your app.

 The iOS, macOS, and watchOS SDKs bundled in Xcode 15 deprecate the [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) and [`requestAccess(to:completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/1507547-requestaccess) methods. If your app links against the iOS 17 SDK, macOS 14 SDK, or watchOS 10 SDK, calling these deprecated request methods doesn’t prompt the user for access and throws an error message. Remove these methods from your app. Use the new APIs to prompt the user for access in your app:

- To request access to reminders, call [`requestFullAccessToReminders(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162273-requestfullaccesstoreminders) or [`requestFullAccessToReminders(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162273-requestfullaccesstoreminders) in your app.
- To request write-only access to events, call [`requestWriteOnlyAccessToEvents(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162274-requestwriteonlyaccesstoevents) or [`requestWriteOnlyAccessToEvents(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162274-requestwriteonlyaccesstoevents) in your app.
- To request full access to events, call [`requestFullAccessToEvents(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162272-requestfullaccesstoevents) or [`requestFullAccessToEvents(completion:)`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/ekeventstore/4162272-requestfullaccesstoevents) in your app.

See [`Connect to the event store`](https://developer.apple.comhttps://developer.apple.com/documentation/eventkit/accessing_the_event_store#2975212) for details.

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3152-migrating-to-the-latest-calendar-access-levels)*