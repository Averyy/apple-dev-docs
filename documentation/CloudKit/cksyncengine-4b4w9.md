# CKSyncEngine

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that manages the synchronization of local and remote record data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngine : NSObject
```

#### Overview

Use [`CKSyncEngine`](./cksyncengine-4b4w9.md) to handle your app’s CloudKit sync operations and benefit from the performance and reliability it provides. To use the class, create an instance early in your app’s launch process and specify a database to sync. Thereafter, and depending on good system conditions, the sync engine periodically pushes and pulls database and record zone changes on the app’s behalf. To participate in those sync operations and to provide the engine with the changes to send, create an object that conforms to [`CKSyncEngineDelegate`](./cksyncenginedelegate-3c38p.md) and assign an instance of it to the engine’s configuration. You can have multiple instances of [`CKSyncEngine`](./cksyncengine-4b4w9.md) in a single process, each targeting a different database. For example, you may have one syncing a person’s private database and another syncing their shared database.

Because periodic sync relies on good system conditions — adequate battery charge, an active network connection, a signed-in iCloud account, and so on — the engine’s sync schedule is indeterminate. If you need to sync immediately, like when your app requires it has the most recent changes before continuing, use the [`fetchChangesWithOptions:completionHandler:`](./cksyncengine-4b4w9/fetchchangeswithoptions_completionhandler_.md) and [`sendChangesWithOptions:completionHandler:`](./cksyncengine-4b4w9/sendchangeswithoptions_completionhandler_.md) methods.

The sync engine uses an opaque type to track its internal state, and it’s your responsibility to persist that state to disk and make it available across app launches so the engine can function properly. For more information, see [`syncEngine:handleEvent:`](./cksyncenginedelegate-3c38p/syncengine_handleevent_.md) and [`CKSyncEngineStateUpdateEvent`](./cksyncenginestateupdateevent.md).

[`CKSyncEngine`](./cksyncengine-4b4w9.md) requires the CloudKit and Remote notifications entitlements. For more information, see [Configuring iCloud services](../Xcode/configuring-icloud-services.md) and [Configuring background execution modes](../Xcode/configuring-background-execution-modes.md).

> ❗ **Important**: Don’t use [`CKSyncEngine`](./cksyncengine-4b4w9.md) to sync your app’s public database.

##### Send changes to iCloud

A sync engine requires you to tell it about any changes to send, which you do by invoking the [`addPendingDatabaseChanges:`](./cksyncenginestate/addpendingdatabasechanges_.md) and [`addPendingRecordZoneChanges:`](./cksyncenginestate/addpendingrecordzonechanges_.md) methods on the engine’s [`state`](./cksyncengine-4b4w9/state.md) property. If there are no scheduled sync operations when you invoke these methods, the engine automatically schedules one. Database changes don’t require any additional input, but the sync engine does expect you to provide the individual record zone changes — in batches — and return them from your delegate’s implementation of [`syncEngine:nextRecordZoneChangeBatchForContext:`](./cksyncenginedelegate-3c38p/syncengine_nextrecordzonechangebatchforcontext_.md). After the engine sends the changes, it notifies your delegate about their success (or failure) by dispatching events of type [`CKSyncEngineSentDatabaseChangesEvent`](./cksyncenginesentdatabasechangesevent.md) and [`CKSyncEngineSentRecordZoneChangesEvent`](./cksyncenginesentrecordzonechangesevent.md).

##### Batches

The sync engine sends record zone changes to the server in batches, where each batch corresponds to a single network request. After your app registers pending changes through [`addPendingRecordZoneChanges:`](./cksyncenginestate/addpendingrecordzonechanges_.md), the engine drives a send operation by repeatedly invoking [`syncEngine:nextRecordZoneChangeBatchForContext:`](./cksyncenginedelegate-3c38p/syncengine_nextrecordzonechangebatchforcontext_.md) to gather those changes into batches and sending each batch as one request. It keeps asking for batches until your delegate returns `nil` or the operation is cancelled, meaning a single send operation may span many batches.

Each batch is bounded by the server’s per-request limit of 250 records (saves plus deletes combined); a batch that exceeds the limit fails with [`CKError.Code.limitExceeded`](./ckerror/code/limitexceeded.md) and the sync engine treats it like any other send failure. To stay within the limit automatically, build your batches with [`initWithPendingChanges:recordProvider:`](./cksyncenginerecordzonechangebatch/initwithpendingchanges_recordprovider_.md), which walks your pending changes in order and stops once the batch is full. Any changes that don’t fit stay in [`pendingRecordZoneChanges`](./cksyncenginestate/pendingrecordzonechanges.md), so the engine picks them up on the next call.

After each batch finishes, the engine dispatches a [`CKSyncEngineSentRecordZoneChangesEvent`](./cksyncenginesentrecordzonechangesevent.md) (or [`CKSyncEngineSentDatabaseChangesEvent`](./cksyncenginesentdatabasechangesevent.md), for database changes) that describes only the records in that batch, so a single send operation produces one sent-changes event per batch rather than a single event for the whole operation.

When your delegate builds a batch, include only changes that fall within the scope specified by [`options`](./cksyncenginesendchangescontext/options.md) on the provided context. Returning changes outside that scope causes the send to fail with [`CKError.Code.invalidArguments`](./ckerror/code/invalidarguments.md).

##### Fetch changes from iCloud

By default, a sync engine attempts to discover an existing [`CKDatabaseSubscription`](./ckdatabasesubscription.md) for the associated database and uses that to receive silent notifications about remote record changes. If the engine doesn’t find a subscription, it automatically creates one to use. On receipt of a notification, the engine schedules a sync operation to fetch the related changes. When that operation runs, the engine dispatches an instance of [`CKSyncEngineWillFetchChangesEvent`](./cksyncenginewillfetchchangesevent.md) to your delegate. As it receives fetched changes, the engine dispatches [`CKSyncEngineFetchedDatabaseChangesEvent`](./cksyncenginefetcheddatabasechangesevent.md) and [`CKSyncEngineFetchedRecordZoneChangesEvent`](./cksyncenginefetchedrecordzonechangesevent.md), accordingly. After the operation finishes, the sync engine notifies your delegate by dispatching an instance of [`CKSyncEngineDidFetchChangesEvent`](./cksyncenginedidfetchchangesevent.md). You handle all dispatched events in your delegate’s implementation of [`syncEngine:handleEvent:`](./cksyncenginedelegate-3c38p/syncengine_handleevent_.md).

##### Sync Scheduling

###### Automatic sync

By default, the sync engine automatically schedules sync tasks on your behalf. If the user is signed in, the device has a network connection, and the system is generally in a good state, these scheduled syncs happen relatively quickly. However, if the device has no network, is low on power, or is otherwise under a heavy load, these automatic syncs might be delayed. Similarly, if the user isn’t signed in to an account, the sync engine won’t perform any sync tasks at all.

###### Manual sync

There may be some cases where you want to manually trigger a sync. For example, if you have a pull-to-refresh UI, you can call [`fetchChangesWithOptions:completionHandler:`](./cksyncengine-4b4w9/fetchchangeswithoptions_completionhandler_.md) to tell the sync engine to fetch immediately. Or, if you have a “backup now” UI, you can call [`sendChangesWithOptions:completionHandler:`](./cksyncengine-4b4w9/sendchangeswithoptions_completionhandler_.md) to send to the server immediately.

##### Error Handling

There are some transient errors that the sync engine handles automatically behind the scenes. The sync engine retries the operations for these transient errors automatically when it makes sense to do so. Specifically, the sync engine will handle the following errors on your behalf:

- [`CKError.Code.notAuthenticated`](./ckerror/code/notauthenticated.md)
- [`CKError.Code.accountTemporarilyUnavailable`](./ckerror/code/accounttemporarilyunavailable.md)
- [`CKError.Code.networkFailure`](./ckerror/code/networkfailure.md)
- [`CKError.Code.networkUnavailable`](./ckerror/code/networkunavailable.md)
- [`CKError.Code.requestRateLimited`](./ckerror/code/requestratelimited.md)
- [`CKError.Code.serviceUnavailable`](./ckerror/code/serviceunavailable.md)
- [`CKError.Code.zoneBusy`](./ckerror/code/zonebusy.md)

When the sync engine encounters one of these errors, it waits for the system to be in a good state, and tries again. For example, if the server sends back a [`CKError.Code.requestRateLimited`](./ckerror/code/requestratelimited.md) error, the sync engine respects this throttle and tries again after the error’s retry-after time.

`CKSyncEngine` does *not* handle errors that require application-specific logic. For example, if you try to save a record and get a [`CKError.Code.serverRecordChanged`](./ckerror/code/serverrecordchanged.md), you need to handle that error yourself. There are plenty of errors that the sync engine cannot handle on your behalf, see [`CKError`](./ckerror.md) for a list of all the possible errors.

##### Accounts

`CKSyncEngine` monitors for account status, and it only syncs if there’s an account signed in. Because of this, you can initialize your `CKSyncEngine` at any time, regardless of account status. If there is no account, or if the user disabled sync in settings, the sync engine stays dormant in the background. Once an account is available, the sync engine starts syncing automatically.

The sync engine listens for when the user signs in or out of their account. When it notices an account change, it sends an [`CKSyncEngineAccountChangeEvent`](./cksyncengineaccountchangeevent.md) to your delegate. It’s your responsibility to react appropriately to this change and update your local persistence.

> 💡 **Tip**: A sample code project for [`CKSyncEngine`](./cksyncengine-4b4w9.md) is available on GitHub here: [CloudKit Samples: CKSyncEngine](https://github.com/apple/sample-cloudkit-sync-engine).

## Topics

### Creating a sync engine
- [- initWithConfiguration:](./cksyncengine-4b4w9/initwithconfiguration_.md)
  Creates a sync engine with the specified configuration.
- [CKSyncEngineConfiguration](./cksyncengineconfiguration.md)
  A type that configures the attributes and behavior of a sync engine.
### Accessing the engine’s attributes
- [database](./cksyncengine-4b4w9/database.md)
  The associated database.
- [state](./cksyncengine-4b4w9/state.md)
  A collection of state properties used to efficiently manage sync engine operation.
- [CKSyncEngineState](./cksyncenginestate.md)
  An object that manages the sync engine’s state.
### Participating in scheduled sync operations
- [CKSyncEngineDelegate](./cksyncenginedelegate-3c38p.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.
### Invoking manual sync operations
- [- fetchChangesWithCompletionHandler:](./cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md)
  Fetches pending remote changes from the server.
- [- fetchChangesWithOptions:completionHandler:](./cksyncengine-4b4w9/fetchchangeswithoptions_completionhandler_.md)
  Fetches pending remote changes from the server using the specified options.
- [CKSyncEngineFetchChangesOptions](./cksyncenginefetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [- sendChangesWithCompletionHandler:](./cksyncengine-4b4w9/sendchangeswithcompletionhandler_.md)
  Sends pending local changes to the server.
- [- sendChangesWithOptions:completionHandler:](./cksyncengine-4b4w9/sendchangeswithoptions_completionhandler_.md)
  Sends pending local changes to the server using the specified options.
- [CKSyncEngineSendChangesOptions](./cksyncenginesendchangesoptions.md)
  A set of options to use with a send operation.
### Canceling operations
- [- cancelOperationsWithCompletionHandler:](./cksyncengine-4b4w9/canceloperationswithcompletionhandler_.md)
  Cancels any in-progress or pending sync operations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Records
- [Local Records](./local-records.md)
  Manipulate records on-device and save changes to the server.
- [Remote Records](./remote-records.md)
  Use subscriptions and change tokens to efficiently manage modifications to remote records.
- [Shared Records](./shared-records.md)
  Share one or more records with other iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9)*