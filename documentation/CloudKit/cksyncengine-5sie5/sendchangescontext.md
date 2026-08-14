# CKSyncEngine.SendChangesContext

**Framework**: CloudKit  
**Kind**: struct

The context of an attempt to send changes to the server.

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
struct SendChangesContext
```

#### Overview

A sync engine has two ways to send changes to iCloud — periodically, in cooperation with the system scheduler, and manually, whenever your app invokes the [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) method. This type provides information about a single attempt to send changes that includes both the reason for the attempt and any additional options in use by the attempt.

## Topics

### Accessing specific attributes
- [let reason: CKSyncEngine.SyncReason](cksyncengine-5sie5/sendchangescontext/reason.md)
  The reason for the send operation.
- [CKSyncEngine.SyncReason](cksyncengine-5sie5/syncreason.md)
  Describes the reason for a sync operation.
- [enum CKSyncEngineSyncReason](cksyncenginesyncreason.md)
  Describes the reason for a sync operation.
- [let options: CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangescontext/options.md)
  The options being used for this attempt to send changes.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use when sending changes to the server.
### Debugging the context
- [var description: String](cksyncengine-5sie5/sendchangescontext/description.md)
  The textual description of the context that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/sendchangescontext/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func nextRecordZoneChangeBatch(CKSyncEngine.SendChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.RecordZoneChangeBatch?](cksyncenginedelegate-1q7g8/nextrecordzonechangebatch(_:syncengine:).md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngine.RecordZoneChangeBatch](cksyncengine-5sie5/recordzonechangebatch.md)
  A type that contains the record changes for a single send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangescontext)*