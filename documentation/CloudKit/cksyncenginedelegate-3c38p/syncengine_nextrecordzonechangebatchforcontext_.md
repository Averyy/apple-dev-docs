# syncEngine:nextRecordZoneChangeBatchForContext:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the next set of record changes to send to the server.

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
- (CKSyncEngineRecordZoneChangeBatch *) syncEngine:(CKSyncEngine *) syncEngine nextRecordZoneChangeBatchForContext:(CKSyncEngineSendChangesContext *) context;
```

#### Return Value

If there are pending record changes, a batch of those changes for the sync engine to process; otherwise, `nil` to indicate there are no changes to send.

#### Discussion

In your implementation, ask the sync engine’s state for any pending record zone changes and then return a change batch containing an instance of [`CKRecord`](../ckrecord.md) for each record identifier the state provides. For both scheduled and manual send operations, the sync engine calls this method repeatedly until your app has no more changes and returns `nil`.

## Parameters

- `syncEngine`: The sync engine requesting changes.
- `context`: The reason for the sync engine’s request, and any additional options that request is using.

## See Also

### Sending changes
- [CKSyncEngineSendChangesContext](../cksyncenginesendchangescontext.md)
  The context of an attempt to send changes to the server.
- [CKSyncEngineRecordZoneChangeBatch](../cksyncenginerecordzonechangebatch.md)
  An object that contains the record changes for a single send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-3c38p/syncengine:nextrecordzonechangebatchforcontext:)*