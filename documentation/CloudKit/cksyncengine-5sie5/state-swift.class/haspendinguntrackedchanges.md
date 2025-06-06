# hasPendingUntrackedChanges

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.

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
final var hasPendingUntrackedChanges: Bool { get set }
```

#### Discussion

Use this property to inform the sync engine that there are pending changes other than those available in [`pendingRecordZoneChanges`](cksyncengine-5sie5/state-swift.class/pendingrecordzonechanges.md). After you set this property, the sync engine automatically schedules a send operation and, when that operation executes, asks your delegate to provide those changes by invoking the [`nextRecordZoneChangeBatch(_:syncEngine:)`](cksyncenginedelegate-1q7g8/nextrecordzonechangebatch(_:syncengine:).md) method.

Using this property is optional and is necessary only if you track pending changes manually, outside of the sync engine’s state.

## See Also

- [var pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange]](cksyncengine-5sie5/state-swift.class/pendingdatabasechanges.md)
  The database changes that the sync engine has yet to send to the iCloud servers.
- [var pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange]](cksyncengine-5sie5/state-swift.class/pendingrecordzonechanges.md)
  The record zone changes that the sync engine has yet to send to the iCloud servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/haspendinguntrackedchanges)*