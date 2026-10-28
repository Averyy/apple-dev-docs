# pendingRecordZoneChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A list of record zone changes that the sync engine has yet to send to the iCloud servers.

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
@property (copy, readonly) NSArray<CKSyncEnginePendingRecordZoneChange *> * pendingRecordZoneChanges;
```

## Discussion

This array contains any pending record zone changes to send to the iCloud servers. After the sync engine sends those changes, your app’s sync delegate receives an event of type [`CKSyncEngineSentRecordZoneChangesEvent`](../cksyncenginesentrecordzonechangesevent.md).

The sync engine keeps this list up-to-date while sending changes to the server. For example, when it successfully saves a record, it removes that change from this list. If it fails to send a change due to some retryable error (e.g. a network failure), it keeps that change in this list.

Use the [`addPendingRecordZoneChanges:`](./addpendingrecordzonechanges_.md) and [`removePendingRecordZoneChanges:`](./removependingrecordzonechanges_.md) methods to modify the array’s contents.

## See Also

### Accessing pending changes
- [hasPendingUntrackedChanges](./haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [pendingDatabaseChanges](./pendingdatabasechanges.md)
  A list of database changes that the sync engine has yet to send to the iCloud servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/pendingrecordzonechanges)*