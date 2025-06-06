# CKSyncEngineDelegate

**Framework**: CloudKit  
**Kind**: protocol

An interface for providing record data to a sync engine and customizing that engine’s behavior.

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
protocol CKSyncEngineDelegate : AnyObject, Sendable
```

#### Overview

> ❗ **Important**:  [`CKSyncEngine`](cksyncengine-5sie5.md) delivers events serially, which means the delegate doesn’t receive the next event until it finishes handling the current one. To maintain this ordering, don’t call sync engine methods from your delegate that may cause the engine to generate additional events. For example, don’t invoke [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) or [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) from within [`handleEvent(_:syncEngine:)`](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md).

 [`CKSyncEngine`](cksyncengine-5sie5.md) delivers events serially, which means the delegate doesn’t receive the next event until it finishes handling the current one. To maintain this ordering, don’t call sync engine methods from your delegate that may cause the engine to generate additional events. For example, don’t invoke [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) or [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) from within [`handleEvent(_:syncEngine:)`](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md).

## Topics

### Handling sync events
- [func handleEvent(CKSyncEngine.Event, syncEngine: CKSyncEngine) async](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md)
  Tells the delegate to handle the specified sync event.
- [CKSyncEngine.Event](cksyncengine-5sie5/event.md)
  Describes an event that occurs during a sync operation.
- [enum CKSyncEngineEventType](cksyncengineeventtype.md)
  Describes an event that occurs during a sync operation.
### Sending changes
- [func nextRecordZoneChangeBatch(CKSyncEngine.SendChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.RecordZoneChangeBatch?](cksyncenginedelegate-1q7g8/nextrecordzonechangebatch(_:syncengine:).md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngine.SendChangesContext](cksyncengine-5sie5/sendchangescontext.md)
  A type that describes a single attempt to send changes to the iCloud servers.
- [CKSyncEngine.RecordZoneChangeBatch](cksyncengine-5sie5/recordzonechangebatch.md)
  A type that contains the record changes for a single send operation.
### Instance Methods
- [func nextFetchChangesOptions(CKSyncEngine.FetchChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.FetchChangesOptions](cksyncenginedelegate-1q7g8/nextfetchchangesoptions(_:syncengine:).md)

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-1q7g8)*