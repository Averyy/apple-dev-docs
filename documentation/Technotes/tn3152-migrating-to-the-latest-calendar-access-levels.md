# TN3152: Migrating to the latest Calendar access levels

**Framework**: Technotes  
**Role**: Technote

Follow these guidelines to update your app to use the new Calendar access levels.

#### Overview

The EventKit framework brings new Calendar access levels in iOS 17, iPadOS 17, macOS 14, Mac Catalyst 17, watchOS 10, and later. The EventKitUI framework provides the ability to add events without requesting access to Calendar in iOS 17, iPadOS 17, Mac Catalyst 17, and later. See [Accessing the Event Store](../EventKit/accessing_the_event_store.md) for details. This document describes how to update your app to use these new features. To learn how these changes may affect your existing apps, see [TN3153: Adopting API changes for EventKit in iOS 17, macOS 14, and watchOS 10](./tn3153-adopting-api-changes-for-eventkit-in-ios-macos-and-watchos.md). Follow these guidelines to support the new features:

**Choose the access level needed to complete your tasks.**

- If your app can present [EKEventEditViewController](../EventKitUI/ekeventeditviewcontroller.md) to let people create events, don’t request access to events.
- If your app needs to create and save calendar data directly without the user making any later changes, request write-only access to calendar data.
- If accessing existing events is essential to the core experience of your app, request full access to calendar data.
- If your app accesses reminder data, request full access to reminders in your app.

**Build your app with Xcode 15 and link against the SDK matching your app’s platform.** Xcode 15 includes SDKs for iOS 17, macOS 14, and watchOS 10 that provide the new write-only and full access features. For instance, if you are building an iOS app, link your app against the iOS 17 SDK or later. If you are building a watchOS app, link your app against the watchOS 10 SDK or later.

**Replace the calendar usage description keys.** Prior to iOS 17, your app needs to include the [NSCalendarsUsageDescription](../BundleResources/information_property_list/nscalendarsusagedescription.md), [NSRemindersUsageDescription](../BundleResources/information_property_list/nsremindersusagedescription.md), and [NSContactsUsageDescription](../BundleResources/information_property_list/nscontactsusagedescription.md) keys in its `Info.plist` file before it can access the user’s calendar data or reminders. `NSCalendarsUsageDescription` and `NSRemindersUsageDescription` describe how your app intends to use the user’s calendar data or reminders, respectively. You provide a `NSContactsUsageDescription` key when your app uses EventKit UI to access Contacts data. If your app supports earlier versions of an OS, keep the key currently available in your app’s `Info.plist` file.

If your app requires running on iOS 17, iPadOS 17, macOS 14, Mac Catalyst 17, watchOS 10, or later, remove these keys from the plist file. Add [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/information_property_list/nscalendarswriteonlyaccessusagedescription.md) or [NSCalendarsFullAccessUsageDescription](../BundleResources/information_property_list/nscalendarsfullaccessusagedescription.md) to the plist file, depending on the level of access to events your app needs. Include [NSRemindersFullAccessUsageDescription](../BundleResources/information_property_list/nsremindersfullaccessusagedescription.md) if your app needs access to reminders. See [Protect user privacy with information property  list keys](../EventKit/accessing_the_event_store.md#2975207) for details.

**Update the authorization status to handle the writeOnly and fullAccess cases.** If your app checks its authorization status for events [EKEventStore.authorizationStatus(for: .event)](../EventKit/ekeventstore/api-1507239-authorizationstatus.md), update it to handle the new [writeOnly](../EventKit/ekauthorizationstatus/writeonly.md) and [fullCase](../EventKit/ekauthorizationstatus/fullaccess.md) cases. Remove the deprecated [authorized](../EventKit/ekauthorizationstatus/api-1451886-authorized.md) case from your app.

**Replace the deprecated request methods.** The iOS, macOS, and watchOS SDKs bundled in Xcode 15 deprecate the [requestAccess(to:completion:)](../EventKit/ekeventstore/api-1507547-requestaccess.md) and [`requestAccess(to:)`](../EventKit/ekeventstore/api-1507547-requestaccess.md) methods. If your app links against the iOS 17 SDK, macOS 14 SDK, or watchOS 10 SDK, calling these deprecated request methods doesn’t prompt the user for access and throws an error message. Remove these methods from your app. Use the new APIs to prompt the user for access in your app:

- To request access to reminders, call [requestFullAccessToReminders(completion:)](../EventKit/ekeventstore/api-4162273-requestfullaccesstoreminders.md) or [`requestFullAccessToReminders()`](../EventKit/ekeventstore/api-4162273-requestfullaccesstoreminders.md) in your app.
- To request write-only access to events, call [requestWriteOnlyAccessToEvents(completion:)](../EventKit/ekeventstore/api-4162274-requestwriteonlyaccesstoevents.md) or [`requestWriteOnlyAccessToEvents()`](../EventKit/ekeventstore/api-4162274-requestwriteonlyaccesstoevents.md) in your app.
- To request full access to events, call [requestFullAccessToEvents(completion:)](../EventKit/ekeventstore/api-4162272-requestfullaccesstoevents.md) or [`requestFullAccessToEvents()`](../EventKit/ekeventstore/api-4162272-requestfullaccesstoevents.md) in your app.

See [Connect to the event store](../EventKit/accessing_the_event_store.md#2975212) for details.

#### Revision History

- **2023-06-06** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3152-migrating-to-the-latest-calendar-access-levels)*