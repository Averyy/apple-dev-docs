# CKSyncEngineSyncReason

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
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CKSyncEngineSyncReason
```

```c
enum CKSyncEngineSyncReason : NSInteger;
```

## Topics

### Sync reasons
- [CKSyncEngineSyncReason.scheduled](./cksyncenginesyncreason/scheduled.md)
  The sync engine automatically scheduled this sync.
- [CKSyncEngineSyncReason.manual](./cksyncenginesyncreason/manual.md)
  A manual sync operation.
### Initializers
- [init?(rawValue: Int)](./cksyncenginesyncreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing specific attributes
- [reason](./cksyncenginesendchangescontext/reason.md)
  The reason for the send operation.
- [options](./cksyncenginesendchangescontext/options.md)
  The additional options for the send operation.
- [CKSyncEngineSendChangesOptions](./cksyncenginesendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesyncreason)*