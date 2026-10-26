# hasPendingUntrackedChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.

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
@property (assign) BOOL hasPendingUntrackedChanges;
```

#### Discussion

Use this property to inform the sync engine that there are pending changes other than those available in [`pendingRecordZoneChanges`](./pendingrecordzonechanges.md). After you set this property, the sync engine automatically schedules a send operation and, when that operation executes, asks your delegate to provide those changes by invoking the [`syncEngine:nextRecordZoneChangeBatchForContext:`](../cksyncenginedelegate-3c38p/syncengine_nextrecordzonechangebatchforcontext_.md) method.

Using this property is optional and is necessary only if you track pending changes manually, outside of the sync engine’s state.

## See Also

### Accessing pending changes
- [pendingDatabaseChanges](./pendingdatabasechanges.md)
  A list of database changes that the sync engine has yet to send to the iCloud servers.
- [pendingRecordZoneChanges](./pendingrecordzonechanges.md)
  A list of record zone changes that the sync engine has yet to send to the iCloud servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/haspendinguntrackedchanges)*