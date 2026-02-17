# CKSyncEngine

**Framework**: CloudKit  
**Kind**: class

An object that manages the synchronization of local and remote record data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final class CKSyncEngine
```

## Mentions

- [Deciding whether CloudKit is right for your app](deciding-whether-cloudkit-is-right-for-your-app.md)

#### Overview

Use [`CKSyncEngine`](cksyncengine-5sie5.md) to handle your app’s CloudKit sync operations and benefit from the performance and reliability it provides. To use the class, create an instance early in your app’s launch process and specify a database to sync. Thereafter, and depending on good system conditions, the sync engine periodically pushes and pulls database and record zone changes on the app’s behalf. To participate in those sync operations and to provide the engine with the changes to send, create a type that conforms to [`CKSyncEngineDelegate`](cksyncenginedelegate-1q7g8.md) and assign an instance of it to the engine’s configuration. You can have multiple instances of [`CKSyncEngine`](cksyncengine-5sie5.md) in a single process, each targeting a different database. For example, you may have one syncing a person’s private database and another syncing their shared database.

Because periodic sync relies on good system conditions — adequate battery charge, an active network connection, a signed-in iCloud account, and so on — the engine’s sync schedule is indeterminate. If you need to sync immediately, like when your app requires it has the most recent changes before continuing, use the [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) and [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) methods.

The sync engine uses an opaque type to track its internal state, and it’s your responsibility to persist that state to disk and make it available across app launches so the engine can function properly. For more information, see [`handleEvent(_:syncEngine:)`](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md) and [`CKSyncEngine.Event.StateUpdate`](cksyncengine-5sie5/event/stateupdate.md).

[`CKSyncEngine`](cksyncengine-5sie5.md) requires the CloudKit and Remote notifications entitlements. For more information, see [`Configuring iCloud services`](https://developer.apple.com/documentation/Xcode/configuring-icloud-services) and [`Configuring background execution modes`](https://developer.apple.com/documentation/Xcode/configuring-background-execution-modes).

> ❗ **Important**: Don’t use [`CKSyncEngine`](cksyncengine-5sie5.md) to sync your app’s public database.

##### Send Changes to Icloud

A sync engine requires you to tell it about any changes to send, which you do by invoking the [`add(pendingDatabaseChanges:)`](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md) and [`add(pendingRecordZoneChanges:)`](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md) methods on the engine’s [`state`](cksyncengine-5sie5/state-swift.property.md) property. If there are no scheduled sync operations when you invoke these methods, the engine automatically schedules one. Database changes don’t require any additional input, but the sync engine does expect you to provide the individual record zone changes — in batches — and return them from your delegate’s implementation of [`nextRecordZoneChangeBatch(_:syncEngine:)`](cksyncenginedelegate-1q7g8/nextrecordzonechangebatch(_:syncengine:).md). After the engine sends the changes, it notifies your delegate about their success (or failure) by dispatching [`CKSyncEngine.Event.sentDatabaseChanges(_:)`](cksyncengine-5sie5/event/sentdatabasechanges(_:).md) and [`CKSyncEngine.Event.sentRecordZoneChanges(_:)`](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md) events.

##### Fetch Changes From Icloud

By default, a sync engine attempts to discover an existing [`CKDatabaseSubscription`](ckdatabasesubscription.md) for the associated database and uses that to receive silent notifications about remote record changes. If the engine doesn’t find a subscription, it automatically creates one to use. On receipt of a notification, the engine schedules a sync operation to fetch the related changes. When that operation runs, the engine dispatches a [`CKSyncEngine.Event.willFetchChanges(_:)`](cksyncengine-5sie5/event/willfetchchanges(_:).md) event to your delegate. As it receives fetched changes, the engine dispatches [`CKSyncEngine.Event.fetchedDatabaseChanges(_:)`](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md) and [`CKSyncEngine.Event.fetchedRecordZoneChanges(_:)`](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md), accordingly. After the operation finishes, the sync engine notifies your delegate by dispatching a [`CKSyncEngine.Event.didFetchChanges(_:)`](cksyncengine-5sie5/event/didfetchchanges(_:).md) event. You handle all dispatched events in your delegate’s implementation of [`handleEvent(_:syncEngine:)`](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md).

##### Sync Scheduling

###### Automatic Sync

By default, the sync engine automatically schedules sync tasks on your behalf. If the user is signed in, the device has a network connection, and the system is generally in a good state, these scheduled syncs happen relatively quickly. However, if the device has no network, is low on power, or is otherwise under a heavy load, these automatic syncs might be delayed. Similarly, if the user isn’t signed in to an account, the sync engine won’t perform any sync tasks at all.

###### Manual Sync

There may be some cases where you want to manually trigger a sync. For example, if you have a pull-to-refresh UI, you can call [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) to tell the sync engine to fetch immediately. Or, if you have a “backup now” UI, you can call [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) to send to the server immediately.

##### Error Handling

There are some transient errors that the sync engine handles automatically behind the scenes. The sync engine retries the operations for these transient errors automatically when it makes sense to do so. Specifically, the sync engine will handle the following errors on your behalf:

- [`CKError.Code.notAuthenticated`](ckerror/code/notauthenticated.md)
- [`CKError.Code.accountTemporarilyUnavailable`](ckerror/code/accounttemporarilyunavailable.md)
- [`CKError.Code.networkFailure`](ckerror/code/networkfailure.md)
- [`CKError.Code.networkUnavailable`](ckerror/code/networkunavailable.md)
- [`CKError.Code.requestRateLimited`](ckerror/code/requestratelimited.md)
- [`CKError.Code.serviceUnavailable`](ckerror/code/serviceunavailable.md)
- [`CKError.Code.zoneBusy`](ckerror/code/zonebusy.md)

When the sync engine encounters one of these errors, it waits for the system to be in a good state, and tries again. For example, if the server sends back a [`CKError.Code.requestRateLimited`](ckerror/code/requestratelimited.md) error, the sync engine respects this throttle and tries again after the error’s retry-after time.

`CKSyncEngine` does  handle errors that require application-specific logic. For example, if you try to save a record and get a [`CKError.Code.serverRecordChanged`](ckerror/code/serverrecordchanged.md), you need to handle that error yourself. There are plenty of errors that the sync engine cannot handle on your behalf, see [`CKError`](ckerror.md) for a list of all the possible errors.

##### Accounts

`CKSyncEngine` monitors for account status, and it only syncs if there’s an account signed in. Because of this, you can initialize your `CKSyncEngine` at any time, regardless of account status. If there is no account, or if the user disabled sync in settings, the sync engine stays dormant in the background. Once an account is available, the sync engine starts syncing automatically.

The sync engine listens for when the user signs in or out of their account. When it notices an account change, it sends an [`CKSyncEngine.Event.accountChange(_:)`](cksyncengine-5sie5/event/accountchange(_:).md) to your delegate. It’s your responsibility to react appropriately to this change and update your local persistence.

> 💡 **Tip**: A sample code project for [`CKSyncEngine`](cksyncengine-5sie5.md) is available on GitHub here: [`CloudKit Samples: CKSyncEngine`](https://developer.apple.comhttps://github.com/apple/sample-cloudkit-sync-engine).

## Topics

### Creating a sync engine
- [init(CKSyncEngine.Configuration)](cksyncengine-5sie5/init(_:).md)
  Creates a sync engine with the specified configuration.
- [CKSyncEngine.Configuration](cksyncengine-5sie5/configuration.md)
  A type that configures the attributes and behavior of a sync engine.
### Accessing the engine’s attributes
- [var database: CKDatabase](cksyncengine-5sie5/database.md)
  The associated database.
- [var state: CKSyncEngine.State](cksyncengine-5sie5/state-swift.property.md)
  A collection of state properties used to efficiently manage sync engine operation.
- [CKSyncEngine.State](cksyncengine-5sie5/state-swift.class.md)
  An object that manages the sync engine’s state.
### Participating in scheduled sync operations
- [protocol CKSyncEngineDelegate](cksyncenginedelegate-1q7g8.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.
### Invoking manual sync operations
- [func fetchChanges(CKSyncEngine.FetchChangesOptions) async throws](cksyncengine-5sie5/fetchchanges(_:).md)
  Fetches pending remote changes from the server.
- [CKSyncEngine.FetchChangesOptions](cksyncengine-5sie5/fetchchangesoptions.md)
  A set of options to use when fetching changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](cksyncengine-5sie5/sendchanges(_:).md)
  Sends pending local changes to the server.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use when sending changes to the server.
### Canceling operations
- [func cancelOperations() async](cksyncengine-5sie5/canceloperations.md)
  Cancels any in-progress or pending sync operations.
### Debugging the sync engine
- [var description: String](cksyncengine-5sie5/description.md)
  The textual description of the engine that’s suitable for logging.
### Structures
- [CKSyncEngine.FetchChangesContext](cksyncengine-5sie5/fetchchangescontext.md)
  The context of an attempt to fetch changes from the server.
- [CKSyncEngine.RecordZoneChangeBatch](cksyncengine-5sie5/recordzonechangebatch.md)
  A type that contains the record changes for a single send operation.
- [CKSyncEngine.SendChangesContext](cksyncengine-5sie5/sendchangescontext.md)
  The context of an attempt to send changes to the server.
### Enumerations
- [CKSyncEngine.Event](cksyncengine-5sie5/event.md)
  Describes an event that occurs during a sync operation.
- [CKSyncEngine.PendingDatabaseChange](cksyncengine-5sie5/pendingdatabasechange.md)
  Describes an unsent database modification.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.
- [CKSyncEngine.SyncReason](cksyncengine-5sie5/syncreason.md)
  Describes the reason for a sync operation.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Local Records](local-records.md)
  Manipulate records on-device and save changes to the server.
- [Remote Records](remote-records.md)
  Use subscriptions and change tokens to efficiently manage modifications to remote records.
- [Shared Records](shared-records.md)
  Share one or more records with other iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5)*