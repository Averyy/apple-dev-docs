# TN3164: Debugging the synchronization of NSPersistentCloudKitContainer

**Framework**: Technotes

Identify and resolve synchronization issues when working with `NSPersistentCloudKitContainer`.

#### Overview

When you use `NSPersistentCloudKitContainer` to manage a CloudKit-backed Core Data store, the store lives on the device to provide data to your app, the CloudKit database lives on the remote CloudKit server to hold the server truth, and `NSPersistentCloudKitContainer` synchronizes them by  the local changes from the store to the database, and  the remote changes from the database to the store. For more information about `NSPersistentCloudKitContainer`, see [`TN3163: Understanding the synchronization of NSPersistentCloudKitContainer`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer.md).

A synchronization failure can happen because of a code-level issue in your data presentation layer, a configuration issue related to CloudKit, or a limit on the system side. To debug a synchronization issue, look into the system logs in Xcode console or a sysdiagnose, then identify the relevant errors. This technote describes how to identify and resolve common errors seen in the logs when working with `NSPersistentCloudKitContainer`.

#### Understand When the Synchronization Happens

The system determines when to synchronize data. When you save data to your Core Data store, `NSPersistentCloudKitContainer` asks the system if it can export the changes; the export only proceeds after the system allows. Similarly, when getting notified of a change on a CloudKit private or shared database, it needs the system’s approval to execute an import.

A CloudKit public database doesn’t support database change notifications. When working with a CloudKit public database, `NSPersistentCloudKitContainer` needs to poll periodically for the database changes. To avoid draining the system resources, `NSPersistentCloudKitContainer` typically polls once every 30 minutes when working in the CloudKit development environment (to facilitate debugging), and up to once every 24 hours in the production environment. For more information, see WWDC20 session 10650: [`Sync a Core Data store with the CloudKit public database`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10650).

The goal of implementing such a mechanism is to balance the use of system resources and achieve the best overall user experience on the devices. There is no API for apps to configure the timing for the synchronization.

> **Note**: When your data synchronizes but not immediately, it is most likely that the system intentionally defers the synchronization. To discover what really happens inside an export or import, see [`Understand the export`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-export.md) and  [`Understand the import`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-import.md).

#### Present the Latest Data

When your app doesn’t show the changes the other peer exported to the CloudKit database, it can be that the data is synchronized but your app’s UI is not refreshed. To verify if that is your case, quit your app, relaunch it, and confirm that the data is now up-to-date.

> **Note**: `NSPersistentCloudKitContainer` may import data while an app is launching. If relaunching your app causes synchronization, it may be that the system intentionally deferred the imports in the previous launch session. See [`Understand the import`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-import.md) for more information.

`NSPersistentCloudKitContainer` synchronizes data when appropriate. To know the state of the synchronization, observe [`eventChangedNotification`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer/eventChangedNotification). To get notified that `NSPersistentCloudKitContainer` imported data to the store, observe [`NSPersistentStoreRemoteChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSPersistentStoreRemoteChange).

To keep your app’s UI up to date, consume the store’s persistent history when you get an `NSPersistentStoreRemoteChange` notification, merge the relevant changes to your [`viewContext`](https://developer.apple.com/documentation/CoreData/NSPersistentContainer/viewContext), and then refresh your app’s UI. Alternatively, [`reset()`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/reset()) your `viewContext` to clear the context cache, fetch the data, and then refresh your app’s UI.

For a sample that demonstrates how to observe the notifications and process the persistent history, see [`Sharing Core Data objects between iCloud users`](https://developer.apple.com/documentation/CoreData/sharing-core-data-objects-between-icloud-users).

When working with a CloudKit public database, `NSPersistentCloudKitContainer` doesn’t automatically synchronize object deletions because the database doesn’t support deletion tracking. To avoid presenting objects deleted by the other peer, consider the following strategy:

1. Add a new attribute to your Core Data entities to store the date when an object is removed.
2. When deleting an object, set its removal date to [`now`](https://developer.apple.com/documentation/Foundation/Date/now), rather than really removing the object from the store. This converts the `delete` to an `update`, which can be synchronized across devices.
3. In your app’s UI, only present the objects whose removal date is `nil`.
4. If necessary, remove the objects whose removal date is sometime after the last successful export. The  needs to be long enough for the objects to be synchronized, which can be several months for apps that users use on a regular basis.

For more information, see WWDC20 session 10650: [`Sync a Core Data store with the CloudKit public database`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10650).

#### Configure Icloud on Your Devices

To synchronize data across devices via `NSPersistentCloudKitContainer`, all the devices must have iCloud turn on for your app, and be logged in with an Apple ID. Perform the following steps to configure your devices:

- Go to Settings > Apple ID > iCloud > Apps Using iCloud, find your app, and select the checkbox.
- Log in the devices with an Apple ID. To synchronize a store associated with a CloudKit private database, log in the devices with a same Apple ID. For CloudKit sharing, log in the owner and participant devices with different Apple IDs.

When developing your app, if you see the synchronization works on some devices, but not on others, it may be that the CloudKit state cached on the device isn’t up to date. Perform the following steps to reset the cache:

1. Remove your app from the device.
2. Remove the Core Data store, if it still exists after step 1. On iOS and its variants, if the store is in an App Group container shared with other apps that need to stay, consider removing the store programmatically. On macOS, find the location of the store and remove it manually.
3. Log out iCloud on the device, log back in with the same Apple ID, and then reboot the device. This clears the cached state related to the Apple ID.

#### Configure Cloudkit in Your Project

To use CloudKit in your app, follow the process described in [`Setting Up Core Data with CloudKit`](https://developer.apple.com/documentation/CoreData/setting-up-core-data-with-cloudkit) to configure a CloudKit container. The process has Xcode automatically generate the appropriate entitlements for your app, and associate the container with your app ID, which allows your app to access the container.

When the association doesn’t exist, `NSPersistentCloudKitContainer` hits a permission failure at run time, and generates logs with an error like the following example:

```None
CoreData: error: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate recoverFromPartialError:forStore:inMonitor:]block_invoke(1943): 
<NSCloudKitMirroringDelegate: …>: Found unknown error as part of a partial failure: 
<CKError …: "Permission Failure" (10/2007); 
server message = "Invalid bundle ID for container"; … container ID = …>
```

> **Note**: For better readability, the logs in this technote are formatted to fit the page size, and some information in the logs is omitted.

To confirm that your CloudKit container and app ID are correctly associated:

1. Log in Apple’s [`Developer Portal`](https://developer.apple.comhttp://developer.apple.com/account) with your developer account, select the Certificates, Identifiers & Profiles page, and find the app ID of your app.
2. Click the app ID to navigate to the Capabilities page, confirm that iCloud is checked, then click Edit to navigate to the iCloud Container Assignment page.
3. Find your CloudKit container, and confirm that it is selected.
4. Refresh your provisioning profile. In Xcode, go to the Signing & Capabilities tab of your app target, un-select the `Automatically manage signing` checkbox, select it again, and then [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution#Assign-the-project-to-a-team) to have Xcode refresh the provisioning profile. If you use manual code signing, create the provisioning profile manually, and then download and install it to your Xcode.

If the portal shows that the association between your CloudKit container and app ID is correct, but the error still exists, it is most likely because the association isn’t synchronized to the CloudKit server. In that case, consider using a new CloudKit container to continue your development.

> **Note**: You can hide a CloudKit container using CloudKit Console, as shown in WWDC22 session 10115: [`What’s new in CloudKit Console`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10115) (the content starting at 1 minute), but can’t delete an existing container.

If your CloudKit container is already used in the production environment and switching to a new container leads to data loss, consider [`filing a feedback report`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/) with the following information to request manually associating your CloudKit container with your app ID:

- The app ID and the CloudKit container that trigger the permission failure.
- Screenshots that show the association between your CloudKit container and app ID in the developer portal.

#### Mirror Your Core Data Model to Cloudkit

`NSPersistentCloudKitContainer` requires that an app’s Core Data model is completely mirrored to CloudKit. When detecting a Core Data attribute or relationship not existing in the CloudKit schema, `NSPersistentCloudKitContainer` stops synchronization and generates logs like the following example:

```None
CoreData: CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:completionHandler:]_block_invoke(3364): 
<NSCloudKitMirroringDelegate: …> - Finished automatic export - AppDeactivationExport - 
with result: <NSCloudKitMirroringResult: …> storeIdentifier: … success: 0 madeChanges: 0 
error: Error Domain=NSCocoaErrorDomain Code=134406 
"Request '5FFC9F71-5E39-4FE8-8E48-C7A828D9B354' was aborted 
because the mirroring delegate never successfully initialized due to error: 
<CKError …: "Partial Failure" (2/1011); "Failed to modify some records"; … 
container ID = …; partial errors: {
41320DB5-A3CB-40C8-AD6D-1767C4B154D9:(com.apple.coredata.cloudkit.zone:__defaultOwner__) = 
<CKError …: "Invalid Arguments" (12/2006); 
server message = "Cannot create or modify field '<A record field>' in record '<A record type>' in production schema"; …> … 
44 "Batch Request Failed" CKError's omited ...}>" 
UserInfo={NSLocalizedFailureReason=Request '5FFC9F71-5E39-4FE8-8E48-C7A828D9B354' was aborted 
because the mirroring delegate never successfully initialized due to error: 
<CKError …: "Partial Failure" (2/1011); "Failed to modify some records"; … container ID = …; 
partial errors: { 41320DB5-A3CB-40C8-AD6D-1767C4B154D9:(com.apple.coredata.cloudkit.zone:__defaultOwner__) = 
<CKError …: "Invalid Arguments" (12/2006); 
server message = "Cannot create or modify field '<A record field>' in record '<A record type>' in production schema"; …
44 "Batch Request Failed" CKError's omited …}>}
```

To completely mirror your Core Data model to CloudKit, see [`Sharing Core Data objects between iCloud users`](https://developer.apple.com/documentation/CoreData/sharing-core-data-objects-between-icloud-users#4288212).

CloudKit doesn’t support all the features of a Core Data model. When designing your model, avoid using the unsupported features, such as unique constraints and ordered relationships. For more information, see [`Creating a Core Data Model for CloudKit`](https://developer.apple.com/documentation/CoreData/creating-a-core-data-model-for-cloudkit#3191035). For an example on how to avoid duplicates, see [`Sharing Core Data objects between iCloud users`](https://developer.apple.com/documentation/CoreData/sharing-core-data-objects-between-icloud-users#4288217).

> **Note**: If the debug build of your app synchronizes correctly but the App Store or TestFlight build doesn’t, it is most likely because you haven’t deployed your CloudKit schema to the production environment. For more information, see [`Deploying an iCloud Container’s Schema`](https://developer.apple.com/documentation/CloudKit/deploying-an-icloud-container-s-schema).

#### Avoid Hitting a Cloudkit Limit

CloudKit has some limits. For example:

- The number of record zones in a CloudKit container is limited to 1000.
- The number of record fields in a record type is limited to 256.
- The size of a record is limited 1MB. (Record fields of the `CKAsset` type are excluded to this limit.)
- The storage a user or an app can use is limited to its quota.

When your app hits a limit, `NSPersistentCloudKitContainer` generates logs with a `Limit Exceeded` error. Here is an example that happened because the record size was too large:

```None
CoreData+CloudKit: -[NSCloudKitMirroringDelegate _performSetupRequest:]_block_invoke_2(1123): 
Called about a failure to save a share: <CKRecordID: …; recordName=cloudkit.zoneshare, 
zoneID=com.apple.coredata.cloudkit.share.850B362A-983C-4C84-91C0-185ADA7811DB:__defaultOwner__> - 
<CKError 0x281d50c30: "Limit Exceeded" (27/2023); 
server message = "record too large"; 
op = 22900FB3D1959E5C; uuid = AEDE918E-F343-4245-A41B-7D7D3A41FD20; container ID = …>
```

To avoid the 256 fields per record type limit, review your CloudKit schema. If you find a record type that is close to or exceeds the limit, trace back to the associated Core Data entity, and split it into multiple entities. See [`Reading CloudKit Records for Core Data`](https://developer.apple.com/documentation/CoreData/reading-cloudkit-records-for-core-data) for how a Core Data model is mirrored to CloudKit.

For other limits, avoid them when designing your app’s architecture and workflow. If hitting a limit is inevitable, handle it appropriately. For example, whenever you create a new CloudKit share ([`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare)) using [`shareManagedObjects:toShare:completion:`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer/shareManagedObjects:toShare:completion:), the API creates a new shared record zone. Over time, your app may hit the 1000 record zone per container limit. To avoid that, consider reusing an existing share when appropriate, and removing empty shares using [`purgeObjectsAndRecordsInZoneWithID:inPersistentStore:completion:`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer/purgeObjectsAndRecordsInZoneWithID:inPersistentStore:completion:). In the case where your app inevitably hits the limit, provide an option the user to keep their data before removing a record zone.

#### Avoid Synchronizing a Store with Multiple Persistent Containers

When using `NSPersistentCloudKitContainer` to load a Core Data store that is already loaded by another `NSPersistentCloudKitContainer` instance, you might see an error like the following example:

```None
CoreData+CloudKit: -[NSCloudKitMirroringDelegate resetAfterError:andKeepContainer:](585): 
<NSCloudKitMirroringDelegate: …> - resetting internal state after error: 
Error Domain=NSCocoaErrorDomain Code=134410 
"CloudKit setup failed because there is another instance of this persistent store actively syncing with CloudKit in this process."
UserInfo={NSURL=file:///private/var/mobile/Containers/Shared/AppGroup/FF9DEFCC-5FA0-4CE6-98FC-BAAB2821911F/shared.sqlite, 
NSLocalizedFailureReason=CloudKit setup failed 
because there is another instance of this persistent store actively syncing with CloudKit in this process.,
NSUnderlyingException=Illegal attempt to register a second handler for activity identifier
com.apple.coredata.cloudkit.activity.setup.A21D2FE4-14B6-4A3C-9381-A56B58117E8F}
```

This can happen when your app and extension both use `NSPersistentCloudKitContainer` to manage a shared Core Data store (even though they are different processes). When working with an extension, you don’t control its lifecycle. It is perfectly possible that your extension is launched when your app is running, or vice versa, and both of them try to load the shared store.

To avoid the conflict, consider having the app in charge of the synchronization. An extension that has the capability to present UI can remind users to launch the app to synchronize with CloudKit, if that is an appropriate user experience.

The app and extension can avoid presenting stale data by observing `.NSPersistentStoreRemoteChange` and consuming the persistent history, as discussed in [`Present the latest data`](tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer#Present-the-latest-data.md).

The error can also happen when your app unintentionally has multiple `NSPersistentCloudKitContainer` instances that manage the same store. For example, when you set a variable that holds an `NSPersistentCloudKitContainer` instance to a new value, the instance won’t be released if a Core Data object tied to the container still exists. To avoid the situation, release all the objects before releasing the `NSPersistentCloudKitContainer` instance.

#### Avoid Rate Limit Throttles

`NSPersistentCloudKitContainer` exports every change on the Core Data store to CloudKit. A lot of changes in a short time frame are converted to a high export rate. If the rate hits a limit, the system on the device or the CloudKit server may decide to defer the synchronization to avoid draining the resources. To determine if your app hits rate limit throttles, see [`Understand system throttles`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-system-throttles.md) and [`TN3162: Understanding CloudKit throttles`](tn3162-understanding-cloudkit-throttles.md).

`NSPersistentCloudKitContainer` stops synchronization when hitting rate limit throttles, and automatically recovers when the throttles expire. The expiration time can be hours, and there is no API for your app to configure it. The strategy to handle rate limit throttles is to avoid them in the first place.

If your app hits the throttles, consider redesigning its architecture and workflow so it makes less changes in a longer time frame. For example, populating a large dataset in a short time frame to your Core Data store may trigger rate limit throttles, and you might be able to avoid that by separating the dataset in batches and populating them lazily, or by shipping the dataset as a local store, and then gradually moving the data to the CloudKit-back store if necessary. To manage multiple Core Data stores with a persistent container, see [`Linking Data Between Two Core Data Stores`](https://developer.apple.com/documentation/CoreData/linking-data-between-two-core-data-stores).

#### Diagnose with a Sysdiagnose

If your issue isn’t covered in the technote, consider figuring out what happens inside the synchronization process by tracing the exports and imports. For more information, see [`TN3163: Understanding the synchronization of NSPersistentCloudKitContainer`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer)*