# TN3163: Understanding the synchronization of NSPersistentCloudKitContainer

**Framework**: Technotes

Explore the details inside the synchronization of `NSPersistentCloudKitContainer` by capturing and analyzing a sysdiagnose.

#### Overview

[`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer) is designed to provide end-to-end synchronization for apps. In many cases, apps use this API to set up a Core Data stack, and the Core Data store automatically synchronizes across devices.

Under the hood, `NSPersistentCloudKitContainer` separates the synchronization process into many tasks, and encapsulates all the implementation details. When performing a task, it generates logs, which are persisted as a part of a sysdiagnose. To understand what really happens in the process, which is sometimes necessary when diagnosing a synchronization issue, you need to look into a sysdiagnose.

This technote unveils some details inside the synchronization by analyzing a sysdiagnose, and provides some representative logs that can be used to identify some important tasks and their state.

#### The Synchronization in a Nutshell

As a prerequisite, it’s important to understand how the synchronization works at a higher level.

`NSPersistentCloudKitContainer` associates a Core Data store with a CloudKit database. The store lives on the device to provide data to your app, the database lives on the remote CloudKit server to hold the server truth, and `NSPersistentCloudKitContainer` takes care the synchronization between them.

The synchronization process is transparent to your app. You still use Core Data APIs to access the store. When you perform a fetch, Core Data returns the data currently existing in the store, without querying CloudKit for potentially unsynchronized changes on the server side. When you perform a save, Core Data writes the data to the store and records the changes in the [`Persistent history`](https://developer.apple.com/documentation/CoreData/persistent-history). When appropriate, `NSPersistentCloudKitContainer`  the local changes from the store to the database, and  the remote changes from the database to the store.

Multiple system services get involved in the process. For example, `dasd` is a system process that coordinates the execution of app activities to balance the use of system resources and achieve the best overall user experience; `NSPersistentCloudKitContainer` works with the process to determine when it is appropriate to execute an import or export. `apsd` receives [`User Notifications`](https://developer.apple.com/documentation/UserNotifications) from APNs server and delivers them to the target apps; `NSPersistentCloudKitContainer` relies on it to detect changes on the associated CloudKit private or shared database. `NSPersistentCloudKitContainer` also relies on `cloudd`, the on-device CloudKit service, to do the data transportation between the device and the CloudKit server.

For more information about `NSPersistentCloudKitContainer`, see the following WWDC sessions:

- WWDC19 session 202: [`Using Core Data with CloudKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2019/202/)
- WWDC20 session 10650: [`Sync a Core Data store with the CloudKit public database`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10650/)
- WWDC21 session 10015: [`Build apps that share data through CloudKit and Core Data`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10015/)
- WWDC22 session 10119: [`Optimize your use of Core Data and CloudKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10119/)

To discover what happens inside an export or import and how the system services work together, see [`Understand the export`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-export.md) and  [`Understand the import`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-import.md).

#### Capture and Analyze a Sysdiagnose

Sysdiagnose analysis is the only means for peeking at the details inside the synchronization, and is typically for investigating a synchronization issue. To do that, capture a sysdiagnose, use your favorite tools to find the relevant logs, and then explore the messages. Focus on finding errors or suspicious activities that may be relevant to the issue you are investigating.

##### Capture a Sysdiagnose

Before capturing a sysdiagnose, find a set of devices and steps that can reproduce the issue. A sysdiagnose won’t contain the relevant logs if it isn’t captured from a device where the issue recently happened. If you can’t reproduce the issue, consider reaching out to the users who reported the issue to you for help.

Use [`CloudKit Console`](https://developer.apple.comhttp://icloud.developer.apple.com/dashboard/) to determine if the issue happens on the exporting or importing side:

1. Prepare two devices, A and B, that are well configured to access CloudKit and can reproduce the issue. To confirm that your devices and project are correctly configured, see [`Configure iCloud on your devices`](tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer#Configure-iCloud-on-your-devices.md) and [`Configure CloudKit in your project`](tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer#Configure-CloudKit-in-your-project.md).
2. Reproduce the synchronization issue by adding some data on device A and observing the data not being synchronized to device B after some time.
3. Try to find the associated CloudKit record with CloudKit Console. To learn how your Core Data model is mirrored to the CloudKit schema, see [`Sharing Core Data objects between iCloud users`](https://developer.apple.com/documentation/CoreData/sharing-core-data-objects-between-icloud-users). To query data in CloudKit Console, see WWDC22 session 10115: [`What’s new in CloudKit Console`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10115/).

If CloudKit Console can’t find the record, you determine that the data wasn’t exported, and so only need to focus on device A. Otherwise, the issue is either the system didn’t deliver the change to your app on device B, or your app didn’t present the data correctly. In this case, capture a sysdiagnose from each device in case your investigation needs the information from both sides.

To capture a sysdiagnose from a device:

1. Install [`the CloudKit profile`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/?name=CloudKit) on the device.
2. For an iOS device, install [`the APNs (Apple Push Notification service) for iOS profile`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/?name=APNs) (search by “APNs”), in case you need to examine push notifications.
3. Reproduce the issue, and note the timestamps immediately before you make a change and after you determine that the change isn’t synchronized correctly. These timestamps are very important because they help dramatically narrow down the system logs.
4. Follow [`the CloudKit profile`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/profiles-and-logs/?name=CloudKit) to capture the sysdiagnose from the device.

For more information, see WWDC22 session 10119: [`Optimize your use of Core Data and CloudKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10119/?time=1295).

##### Analyze a Sysdiagnose

The most relevant part in a sysdiagnose is the system logs, which are archived in the file named `system_logs.logarchive`. Use `Console.app` or `log` to find the relevant logs in the file and determine if the synchronization succeeds.

The logs are typically very overwhelming. Use the timestamps you noted when capturing the sysdiagnose to narrow the scope down to the time frame when the issue occurs, and use filters, such as `process`, `subsystem`, and `message`, to filter out the irrelevant logs.

If you use Console.app, specify a custom time frame with the `Showing` option below the log view, and use the search field in the toolbar to set up filters. Be sure that `Include Info Messages` and `Include Debug Messages` under the `Action` menu are checked. For more information about how to find log messages and activities in Console.app, see [`Console User Guide`](https://developer.apple.comhttps://support.apple.com/guide/console/find-log-messages-and-activities-cnslbf30b61a/1.1/mac/14.0).

If you use `log`, specify the time frame with the `--start` and `--end` options, and use `--predicate` to set up filters. As an example, the following command extracts the logs generated between `2023-12-07 12:22:47+0100` and `2023-12-07 12:33:53+0100` for the process named `YourCoolApp`, with the subsystem being `com.apple.coredata` and the messages containing “import.” For the detailed syntax of `log`, see its man page; for how to read man pages, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

```None
log show --start "2023-12-07 12:22:47+0100" --end "2023-12-07 12:33:53+0100" 
    —info —debug 
    —predicate 'process = "YourCoolApp" 
                and subsystem = "com.apple.coredata" 
                and message contains[cd] "import"' 
    ./system_logs.logarchive
```

Use these tools to explore what really happens inside the exports and imports. In the process, always use the timestamps and filters to find the relevant logs, and focus on finding the following:

- The errors related to Core Data or CloudKit. For more information about how to handle some common errors, see [`TN3164: Debugging the synchronization of NSPersistentCloudKitContainer`](tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer.md).
- The time frames when an activity should but doesn’t happen. If the activity is an export, confirm that `NSPersistentCloudKitContainer` detects the change on the store; for an import related to a CloudKit private or shared database, confirm that the system gets the CloudKit notification and delivers it to your app. See [`Understand the export`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-export.md) and  [`Understand the import`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-the-import.md) for more information.
- The activities that last unusually long. If any, check if they are intentionally deferred by the system. See [`Understand system throttles`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-system-throttles.md) for more information.

#### Understand the Export

An export has the following phases:

1. Observe if the Core Data store is changed.
2. Confirm that the export can proceed.
3. Execute the export.

This section shows the filters for tracing the phases, and provides the representative logs that can be used to identify the phases and their state.

##### Observe If the Core Data Store Is Changed

When observing the app saving a managed object context ([`NSManagedObjectContext`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext)) or a remote change notification ([`NSPersistentStoreRemoteChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/3180044-nspersistentstoreremotechange)) that indicates the store being changed remotely, `NSPersistentCloudKitContainer` logs the event and starts to schedule an export. Use the `process` (”<the app name>”), `subsystem` (“com.apple.coredata”), and `message` (“Observed”) filters to find the relevant logs, as shown in the following example:

```None
info  … 14:14:15.227567 …  YourCoolApp  debug: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate managedObjectContextSaved:](3097): 
<NSCloudKitMirroringDelegate: …>: Observed context save: 
<NSPersistentStoreCoordinator: …> - <NSManagedObjectContext: …>

info  … 14:14:15.230887 …  YourCoolApp debug: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate remoteStoreDidChange:](3140): 
<NSCloudKitMirroringDelegate: …>: Observed remote store notification: 
<NSPersistentStoreCoordinator: …> - A73C42D5-ADEE-4758-B2A1-F75DEBF93702 - …
```

> **Note**: For better readability, the logs in this technote are formatted to fit the page size, and some information in the logs is omitted.

For better readability, the logs in this technote are formatted to fit the page size, and some information in the logs is omitted.

> **Note**: If you save a managed object context but can’t find the relevant logs, confirm that the save was successful. Be sure to save the [`parent`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/parent), if you use a nested context.

If you save a managed object context but can’t find the relevant logs, confirm that the save was successful. Be sure to save the [`parent`](https://developer.apple.com/documentation/CoreData/NSManagedObjectContext/parent), if you use a nested context.

The logs contain the Core Data [`NSStoreUUIDKey`](https://developer.apple.com/documentation/CoreData/NSStoreUUIDKey), or `A73C42D5-ADEE-4758-B2A1-F75DEBF93702` in this example, which can be used with the `message` filter to filter out the logs irrelevant to the store.

##### Confirm That the Export Can Proceed

After observing that the store was changed, `NSPersistentCloudKitContainer` asks the system if now is appropriate to do an export. An export activity has an identifier that contains the store UUID.

Use the `process` (“dasd”) and `message` ( “activity.export.<the-store-UUID>”) filters to find the logs that tell if the export was allowed. Most likely, you will see something like the following example, where “Can Proceed” means what it says – The export can proceed:

```None
default  … 14:14:15.609957 …  dasd 
501:com.apple.coredata.cloudkit.activity.export.A73C42D5-ADEE-4758-B2A1-F75DEBF93702:0B1380:
[{name: Application Policy, policyWeight: 25.000, 
response: {Decision: Can Proceed, Score: 0.60}}
{name: Device Activity Policy, policyWeight: 2.000, 
response: {Decision: Can Proceed, Score: 0.41}
}] 
sumScores:60.704720, denominator:71.940000, 
FinalDecision: Can Proceed FinalScore: 0.843824}
```

Sometimes, you might see the system decides that an activity “Must Not Proceed,” as shown in the following example:

```None
default  … 14:14:16.316165 …  dasd 
501:com.apple.coredata.cloudkit.activity.export.A73C42D5-ADEE-4758-B2A1-F75DEBF93702:B1BC07:
[{name: Activity Group Policy, policyWeight: 0.500, 
response: {Decision: Must Not Proceed, Score: 0.00, 
Rationale: [{"com.apple.coredata.cloudkit.YourCoolApp.A73C42D5-ADEE-4758-B2A1-F75DEBF93702".currentAvailableLimit == 0}]}
}],FinalDecision: Must Not Proceed}
```

The above message conveys a piece of important information – the policy that the system applied when deciding to throttle the export, or `Activity Group Policy`. It means that the throttle was enforced because the number of the app’s scheduled concurrent activities hit the limit.

Here is another example that shows the system applied `ActivityRateLimitPolicy` to throttle the export because the app’s activities hit the rate limit:

```None
default  … 14:14:16.657700 …  dasd 
501:com.apple.coredata.cloudkit.activity.export.A73C42D5-ADEE-4758-B2A1-F75DEBF93702:B1BC07:
[{name: ActivityRateLimitPolicy, policyWeight: 1.000, 
response: {Decision: Must Not Proceed, Score: 0.00, 
Rationale: [{[ratelimited]: Required:1.00, Observed:0.00},]}}
], FinalDecision: Must Not Proceed}
```

When hitting a throttle, `NSPersistentCloudKitContainer` stops synchronization, until the throttle expires. The expiration time of a throttle depends on the policy. For more information, see [`Understand system throttles`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-system-throttles.md).

##### Execute the Export

Once the system decides that the export can proceed, `NSPersistentCloudKitContainer` starts to execute it. Use the `process` (”<the app name>”), `subsystem` (“com.apple.coredata”), and `message` (“export”) filters to find the logs that show the whole lifecycle. The following example shows an export was scheduled, enqueued, executed, and finished:

```None
default  … 14:14:16.621530 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:](3633):
<NSCloudKitMirroringDelegate: …> - Beginning automated export - ExportActivity:
<CKSchedulerActivity: …>

default  … 14:14:16.621597 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate executeMirroringRequest:error:](969): 
<NSCloudKitMirroringDelegate: …>: Asked to execute request: 
<NSCloudKitMirroringExportRequest: …> EAD940DB-330A-4DDF-9892-41286F9FE95A

default  … 14:14:16.621633 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke(1003): 
<NSCloudKitMirroringDelegate: …>: enqueuing request: 
<NSCloudKitMirroringExportRequest: …> EAD940DB-330A-4DDF-9892-41286F9FE95A

default  … 14:14:16.621675 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke_2(1012): 
Enqueued request: <NSCloudKitMirroringExportRequest: …> EAD940DB-330A-4DDF-9892-41286F9FE95A

default  … 14:14:16.621714 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate checkAndExecuteNextRequest]_block_invoke(3524): 
<NSCloudKitMirroringDelegate: …>: Executing: 
<NSCloudKitMirroringExportRequest: …> EAD940DB-330A-4DDF-9892-41286F9FE95A

default  … 14:14:16.623737 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[PFCloudKitExporter analyzeHistoryInStore:withManagedObjectContext:error:](531): 
<PFCloudKitExporter: …>: Exporting changes since (0): 
<NSPersistentHistoryToken - {
    "A73C42D5-ADEE-4758-B2A1-F75DEBF93702" = 3177;
}>

default  … 14:14:16.656255 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[PFCloudKitExporter exportIfNecessary]_block_invoke_2(345): 
<PFCloudKitExporter: …>: Found 0 objects needing export.

default  … 14:14:16.656769 …  YourCoolApp  warning: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _exportFinishedWithResult:exporter:](1477): 
Finished export: <PFCloudKitExporter: …>

default  … 14:14:16.656785 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _finishedRequest:withResult:](3542): 
Finished request: <NSCloudKitMirroringExportRequest: …> EAD940DB-330A-4DDF-9892-41286F9FE95A 
with result: <NSCloudKitMirroringResult: …> storeIdentifier: … 
success: 1 madeChanges: 0 error: (null)
```

You may also see that an export was cancelled because there was already a pending request, as shown in the following example. In case the pending export was finished successfully later and new exports were scheduled, ignore the error.

```None
default  …12:21:54.208523…  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _scheduleAutomatedExportWithLabel:activity:voucher:completionHandler:]_block_invoke(3647):
<NSCloudKitMirroringDelegate: …> - Finished automatic export - ExportActivity - with result: 
<NSCloudKitMirroringResult: …> storeIdentifier: … success: 0 madeChanges: 0 
error: Error Domain=NSCocoaErrorDomain Code=134417 
"Request '<NSCloudKitMirroringExportRequest: …> B543EDAB-6D08-4ED2-B422-27BB0C872624' 
was cancelled because there is already a pending request of type 'NSCloudKitMirroringExportRequest'." …
```

#### Understand the Import

An import has the following phases:

1. Schedule an import.
2. Confirm that the import can proceed.
3. Execute the import.

This section shows the filters for tracing the phases, and provides the representative logs that can be used to identify the phases and their state.

##### Schedule an Import

The associated CloudKit database can change (as a result of a peer’s export, for example). To merge the remote changes, `NSPersistentCloudKitContainer` schedules the following imports:

- A import for the initial synchronization, which happens in the app’s first launch session after being installed.
- Imports that happen at some points, like when the app is activated.
- An import when getting notified of a database change.

When working with a CloudKit private or shared database, `NSPersistentCloudKitContainer` schedules an import when getting a [`CKNotification`](https://developer.apple.com/documentation/CloudKit/CKNotification), which is triggered when the database changes. A CloudKit public database doesn’t support this kind of notification, and so `NSPersistentCloudKitContainer` needs to poll periodically for the database changes. To avoid draining the system resources, `NSPersistentCloudKitContainer` typically polls once every 30 minutes when working in the CloudKit development environment, and up to once every 24 hours in the production environment. For more information, see WWDC20 session 10650: [`Sync a Core Data store with the CloudKit public database`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10650/).

Use the `process` (”<the app name>”), `subsystem` (“com.apple.coredata”), and `message` (“checkAndSchedule”) filters to find the relevant logs. The following example shows that three imports were being scheduled:

```None
default  … 17:18:00.439094 …  YourCoolApp warning: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate checkAndScheduleImportIfNecessary:andStartAfterDate:]_block_invoke(3268): 
<NSCloudKitMirroringDelegate: …>: Scheduling automated import with activity 
(Database-LastFetchDate-2023-12-06 13:54:06 +0000): <CKSchedulerActivity: …>

default  … 17:18:01.121638 …  YourCoolApp warning: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate checkAndScheduleImportIfNecessary:andStartAfterDate:]_block_invoke(3268): 
<NSCloudKitMirroringDelegate: …>: Scheduling automated import with activity 
(Zone-LastFetchDate-com.apple.coredata.cloudkit.zone-2023-12-06 13:51:34 +0000): <CKSchedulerActivity: …>

default  … 17:26:17.667361 …  YourCoolApp warning: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate checkAndScheduleImportIfNecessary:andStartAfterDate:]_block_invoke(3268): 
<NSCloudKitMirroringDelegate: …>: Scheduling automated import with activity (Push): <CKSchedulerActivity: …>
```

The activity label (the text in the parentheses after “Scheduling automated import with activity”) in the logs conveys some important information. In this example, that is:

- The first import was to fetch the database changes, and the last fetch happened at `2023-12-06 13:54:06 +0000`.
- The second one was to fetch the CloudKit zone changes, and the last fetch happened at `2023-12-06 13:51:34 +0000`.
- The third one was an import triggered by a push notification.

Use this information to determine if an import is scheduled in a reasonable time frame.

When you find no import after the other peer changed the private or shared database, confirm that the system receives the CloudKit notification. To do that, use the `process` (“apsd”) and `message` ( “Received message”) filters to find the representative logs, as shown in the following example. Note that the notification topic contains the app’s bundle ID, or `com.example.YourCoolApp` here.

```None
default  … 15:37:22.786196 …  apsd 
<APSUserCourier … development 0>: Received message 
for enabled topic 'com.apple.icloud-container.com.example.YourCoolApp' 
onInterface: <APSCourierConnectionProtocolConnection: …; NonCellular> 
with payload '<redacted __NSDictionaryI count:2>' with priority 5 
for device token: YES isProxyMessage: NO
```

To confirm that the system forwarded the notification to your app, use the `process` (”<the app name>”) and `message` ( “Notification”) filters to find something like the following example:

```None
default  … 15:37:22.885571 …  YourCoolApp
<CKNotificationListener: …> received push with payload <PKPushPayload: …>

debug  … 15:37:22.886249 …  YourCoolApp
Received CKNotification: 
<CKDatabaseNotification: …; notificationType=4, 
notificationID=158bdf8b-4c6d-42d6-9628-9d3a9cf34dae, 
containerID=iCloud.com.example.YourCoolApp:Sandbox, 
subscriptionOwnerUserRecordID=…:(_defaultZone:defaultOwner), 
subscriptionID=com.apple.coredata.cloudkit.private.subscription, 
database=Private, 
zoneID=com.apple.coredata.cloudkit.zone:defaultOwner> for <CKNotificationListener: …>

debug  … 15:37:22.886609 …  YourCoolApp
Checking notification's user record ID <CKRecordID: …> against container user record ID for 
<CKSubscriptionInfo: …; database=<CKDatabase: …; databaseScope=Private, 
containerImplementation=<… containerIdentifier=iCloud.com.example.YourCoolApp, environment=Sandbox>>> 
subscriptionID=com.apple.coredata.cloudkit.private.subscription>

default  … 15:37:22.887476 …  YourCoolApp
Running handler for notification <CKDatabaseNotification: …>: {
    aps =     {
        "content-available" = 1;
    };
    ck =     {
        aux =         {
        };
        ce = 2;
        cid = "iCloud.com.example.YourCoolApp";
        ckuserid = …;
        met = {…};
        nid = "158bdf8b-4c6d-42d6-9628-9d3a9cf34dae";
    };
}

default  … 15:37:22.887758 …  YourCoolApp  CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _respondToPushNotification:forSubscription:]_block_invoke(896): 
<NSCloudKitMirroringDelegate: …> - Got notification for subscription: 
com.apple.coredata.cloudkit.private.subscription <CKDatabaseNotification: …>
```

> **Note**: If the system receives a CloudKit notification but doesn’t forward it to your app, confirm that the `Remote notification` background mode is on in your project, as described in [`Setting Up Core Data with CloudKit`](https://developer.apple.com/documentation/CoreData/setting-up-core-data-with-cloudkit).

If the system receives a CloudKit notification but doesn’t forward it to your app, confirm that the `Remote notification` background mode is on in your project, as described in [`Setting Up Core Data with CloudKit`](https://developer.apple.com/documentation/CoreData/setting-up-core-data-with-cloudkit).

##### Confirm That the Import Can Proceed

As it does for an export, `NSPersistentCloudKitContainer` coordinates with the system on when to do an import. Use the `process` (“dasd”) and `message` (“activity.import.<the-store-UUID>”) filters to find the relevant logs. The following example shows the system applied `Activity Group Policy` to throttle an import, and let it go almost immediately because the throttle quickly expired:

```None
default  … 14:14:15.613580 …  dasd 
501:com.apple.coredata.cloudkit.activity.import.A73C42D5-ADEE-4758-B2A1-F75DEBF93702:CF81BC:
[{name: Activity Group Policy, policyWeight: 0.500, 
response: {Decision: Must Not Proceed, Score: 0.00, 
Rationale: [{"com.apple.coredata.cloudkit.YourCoolApp.A73C42D5-ADEE-4758-B2A1-F75DEBF93702".currentAvailableLimit == 0}]}
}], FinalDecision: Must Not Proceed}
…
default  … 14:14:15.746773 …  dasd 
501:com.apple.coredata.cloudkit.activity.import.A73C42D5-ADEE-4758-B2A1-F75DEBF93702:CF81BC:
[{name: Application Policy, policyWeight: 25.000, 
response: {Decision: Can Proceed, Score: 0.60}}
{name: Device Activity Policy, policyWeight: 2.000, 
response: {Decision: Can Proceed, Score: 0.41}}
] sumScores:60.704720, denominator:71.940000, 
FinalDecision: Can Proceed FinalScore: 0.843824}
```

For more information, see [`Understand system throttles`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-system-throttles.md).

##### Execute the Import

`NSPersistentCloudKitContainer` starts to execute an import once the system determines the activity can proceed. Use the `process` (”<the app name>”), `subsystem` (“com.apple.coredata”), and `message` ( “import”) filters to find the relevant logs. The following example shows an import was scheduled, enqueued, executed, and finished. The scheduling messages include information about why an import was scheduled – In this example, `ImportActivity` indicates that the import was scheduled in response to the system approving the activity.

```None
default  … 14:14:15.841696 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _scheduleAutomatedImportWithLabel:activity:voucher:completionHandler:](3594): 
<NSCloudKitMirroringDelegate: …> - Beginning automated import - ImportActivity - 
in response to activity:<CKSchedulerActivity: …>

default  … 14:14:15.841767 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate executeMirroringRequest:error:](969): 
<NSCloudKitMirroringDelegate: …>: Asked to execute request: 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550

default  … 14:14:15.841814 … YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke(1003): 
<NSCloudKitMirroringDelegate: …>: enqueuing request: 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550

default  … 14:14:15.841866 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _enqueueRequest:]_block_invoke_2(1012): 
Enqueued request: <NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550

default  … 14:14:15.841911 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate checkAndExecuteNextRequest]_block_invoke(3524): 
<NSCloudKitMirroringDelegate: …>: Executing: 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550

default  … 14:14:16.287051 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[PFCloudKitImporter databaseFetchFinishWithContext:error:completion:]_block_invoke(304): 
<PFCloudKitImporter: …>: Import request finished: 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550
- <PFCloudKitImportDatabaseContext: …> {
Token: <CKServerChangeToken: 0x6000022c6ef0; data=AQAAAYxEadbv>
Changed: {(<CKRecordZoneID: …; zoneName=com.apple.coredata.cloudkit.zone, ownerName=defaultOwner>)}}

default  … 14:14:16.287167 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[PFCloudKitImporter processWorkItemsWithCompletion:](418): 
<PFCloudKitImporter: …>: Processing work items: (
"<PFCloudKitImporterZoneChangedWorkItem: 0x6000017d3d30 - 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550>
{\n(\n \"<CKRecordZoneID: 0x600002ed7450; zoneName=com.apple.coredata.cloudkit.zone, ownerName=defaultOwner>\"\n)\n}")

default  … 14:14:16.535114 …  YourCoolApp warning: CoreData+CloudKit: 
-[PFCloudKitImportRecordsWorkItem newMirroringResultByApplyingAccumulatedChanges]_block_invoke(241): 
Finished importing changes for request: 
<NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550

default  … 14:14:16.535195 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[PFCloudKitImporter processWorkItemsWithCompletion:](418): 
<PFCloudKitImporter: …>: Processing work items: ()

default  … 14:14:16.536834 …  YourCoolApp CloudKit: CoreData+CloudKit: 
-[NSCloudKitMirroringDelegate _finishedRequest:withResult:](3542): 
Finished request: <NSCloudKitMirroringImportRequest: …> 2D00459F-8C08-4E9A-BC44-FCE1CD29A550
with result: <NSCloudKitMirroringResult: …> storeIdentifier: … 
success: 1 madeChanges: 0 error: (null)
```

#### Understand System Throttles

The system resources on a device are finite and shared by all apps. High utilization from one app can negatively affect others. To balance the use of the resources and achieve the best overall user experience on the device, the system includes a process to coordinate the execution of app activities, and that is `dasd`.

`dasd` decides if an activity should be throttled based on a set of policies. To determine if your app hits throttles, see [`Confirm that the export can proceed`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Confirm-that-the-export-can-proceed.md) and [`Confirm that the import can proceed`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Confirm-that-the-import-can-proceed.md). Depending on the policy, a throttle can expire in a second or last for hours.

For example, a throttle applied with `Activity Group Policy` expires when the preceding activity is finished, which is typically quick; a throttle with `ActivityRateLimitPolicy` is triggered by the app frequently doing too many activities, and can last for hours; a throttle with `Low Power Mode Policy` is triggered because the device runs in the lower power mode, and may last until the battery level is back to a certain level, or the device is connected to a power adapter.

When identifying a throttle in your system logs, check the policy to figure out why `dasd` made the decision, and see if you can avoid running into the situation. For example, a throttle with `ActivityRateLimitPolicy` can happen when you try to populate a large dataset to a Core Data store in a short time frame, and you might be able to avoid that by separating the dataset in batches and populating them lazily.

Apps don’t need to do anything about some kinds of throttles. As an example, it is as-designed that `dasd` throttles some activities when the device is in low energy mode. There is no API for apps to change the behavior. If you believe that it doesn’t make sense to trigger a throttle in your use case, consider [`Provide actionable feedback`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Provide-actionable-feedback.md).

When hitting a throttle, `NSPersistentCloudKitContainer` stops exporting or importing data, until the throttle expires. There is no API for apps to configure the expiration time.

CloudKit can throttle the requests from `NSPersistentCloudKitContainer` as well. For more information, see [`TN3162: Understanding CloudKit throttles`](tn3162-understanding-cloudkit-throttles.md).

#### Provide Actionable Feedback

When you see a system behavior that doesn’t make sense in your use case, consider [`filing a feedback report`](https://developer.apple.comhttp://developer.apple.com/bug-reporting/). It is important to make your report  by providing the following information:

1. A clear description of the symptoms, and the detailed steps to reproduce them.
2. The name and bundle ID of your app, and the iCloud container ID.
3. The sysdiagnose(s) and the timestamps, as described in [`Capture a sysdiagnose`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Capture-a-sysdiagnose.md).
4. The part of the system logs that shows the behavior, or why the behavior makes no sense to you.
5. The Core Data store on the device(s).

To retrieve a Core Data store in your app’s container from an iOS device, see [`View, download, and replace app containers on a device`](https://developer.apple.comhttps://help.apple.com/xcode/mac/11.4/#/dev816c242e1). If your store is in another location, such as an App Group container, use [`replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)`](https://developer.apple.com/documentation/CoreData/NSPersistentStoreCoordinator/replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)) to copy it to a location where you have access. A Core Data store contains a main database file, multiple accompanying files (`-wal` and `-shm` files), and potentially some hidden files. When zipping a store, zip the whole parent folder so all the files are included.

For more information about filing a great feedback report, see WWDC22 session 10119: [`Optimize your use of Core Data and CloudKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10119/?time=1295).

> **Note**: When providing feedback for other CloudKit APIs, such as the [`CloudKit`](https://developer.apple.com/documentation/CloudKit) framework and [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore), make your report actionable as well by providing the same information, except the Core Data store that isn’t needed.

When providing feedback for other CloudKit APIs, such as the [`CloudKit`](https://developer.apple.com/documentation/CloudKit) framework and [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore), make your report actionable as well by providing the same information, except the Core Data store that isn’t needed.

#### Revision History

-  Adjusted some of the video links.
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

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer)*