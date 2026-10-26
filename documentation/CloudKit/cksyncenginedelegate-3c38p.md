# CKSyncEngineDelegate

**Framework**: CloudKit  
**Kind**: protocol  
**Role**: Protocol

An interface for providing record data to a sync engine and customizing that engine’s behavior.

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
@protocol CKSyncEngineDelegate <NSObject>
```

#### Overview

> ❗ **Important**: [`CKSyncEngine`](./cksyncengine-4b4w9.md) delivers events serially, which means the delegate doesn’t receive the next event until it finishes handling the current one. To maintain this ordering, don’t call sync engine methods from your delegate that may cause the engine to generate additional events. For example, don’t invoke [`fetchChangesWithCompletionHandler:`](./cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md) or [`sendChangesWithCompletionHandler:`](./cksyncengine-4b4w9/sendchangeswithcompletionhandler_.md) from within [`syncEngine:handleEvent:`](./cksyncenginedelegate-3c38p/syncengine_handleevent_.md).

## Topics

### Handling sync events
- [- syncEngine:handleEvent:](./cksyncenginedelegate-3c38p/syncengine_handleevent_.md)
  Tells the delegate to handle the specified sync event.
- [CKSyncEngineEvent](./cksyncengineevent.md)
  An event that occurs during a sync operation.
### Sending changes
- [- syncEngine:nextRecordZoneChangeBatchForContext:](./cksyncenginedelegate-3c38p/syncengine_nextrecordzonechangebatchforcontext_.md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngineSendChangesContext](./cksyncenginesendchangescontext.md)
  The context of an attempt to send changes to the server.
- [CKSyncEngineRecordZoneChangeBatch](./cksyncenginerecordzonechangebatch.md)
  An object that contains the record changes for a single send operation.
### Instance Methods
- [- syncEngine:nextFetchChangesOptionsForContext:](./cksyncenginedelegate-3c38p/syncengine_nextfetchchangesoptionsforcontext_.md)
  Returns a custom set of options for CKSyncEngine to use while fetching changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-3c38p)*