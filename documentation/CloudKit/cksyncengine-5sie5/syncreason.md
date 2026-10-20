# CKSyncEngine.SyncReason

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Describes the reason for a sync operation.

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
enum SyncReason
```

## Topics

### Sync reasons
- [CKSyncEngine.SyncReason.scheduled](./syncreason/scheduled.md)
  The sync engine automatically scheduled this sync.
- [CKSyncEngine.SyncReason.manual](./syncreason/manual.md)
  A manual sync operation.
### Debugging the reason
- [var description: String](./syncreason/description.md)
  The textual description of the reason that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./syncreason/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing specific attributes
- [let reason: CKSyncEngine.SyncReason](./sendchangescontext/reason.md)
  The reason for the send operation.
- [enum CKSyncEngineSyncReason](../cksyncenginesyncreason.md)
  Describes the reason for a sync operation.
- [let options: CKSyncEngine.SendChangesOptions](./sendchangescontext/options.md)
  The options being used for this attempt to send changes.
- [CKSyncEngine.SendChangesOptions](./sendchangesoptions.md)
  A set of options to use when sending changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/syncreason)*