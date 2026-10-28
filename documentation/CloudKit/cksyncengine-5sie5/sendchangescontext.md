# CKSyncEngine.SendChangesContext

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

The context of an attempt to send changes to the server.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct SendChangesContext
```

## Overview

A sync engine has two ways to send changes to iCloud — periodically, in cooperation with the system scheduler, and manually, whenever your app invokes the [`sendChanges(_:)`](./sendchanges%28_%29.md) method. This type provides information about a single attempt to send changes that includes both the reason for the attempt and any additional options in use by the attempt.

## Topics

### Accessing specific attributes
- [let reason: CKSyncEngine.SyncReason](./sendchangescontext/reason.md)
  The reason for the send operation.
- [CKSyncEngine.SyncReason](./syncreason.md)
  Describes the reason for a sync operation.
- [enum CKSyncEngineSyncReason](../cksyncenginesyncreason.md)
  Describes the reason for a sync operation.
- [let options: CKSyncEngine.SendChangesOptions](./sendchangescontext/options.md)
  The options being used for this attempt to send changes.
- [CKSyncEngine.SendChangesOptions](./sendchangesoptions.md)
  A set of options to use when sending changes to the server.
### Debugging the context
- [var description: String](./sendchangescontext/description.md)
  The textual description of the context that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./sendchangescontext/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending changes
- [func nextRecordZoneChangeBatch(CKSyncEngine.SendChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.RecordZoneChangeBatch?](../cksyncenginedelegate-1q7g8/nextrecordzonechangebatch%28_,syncengine%29.md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngine.RecordZoneChangeBatch](./recordzonechangebatch.md)
  A type that contains the record changes for a single send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangescontext)*