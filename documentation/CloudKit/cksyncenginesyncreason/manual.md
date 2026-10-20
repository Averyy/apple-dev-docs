# CKSyncEngineSyncReason.manual

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

A manual sync operation.

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
case manual
```

```c
CKSyncEngineSyncReasonManual
```

#### Discussion

The sync engine uses this reason only when your app invokes the [`fetchChangesWithCompletionHandler:`](../cksyncengine-4b4w9/fetchchangeswithcompletionhandler_.md) and [`sendChangesWithCompletionHandler:`](../cksyncengine-4b4w9/sendchangeswithcompletionhandler_.md) methods and their variants.

## See Also

### Sync reasons
- [CKSyncEngineSyncReason.scheduled](./scheduled.md)
  The sync engine automatically scheduled this sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesyncreason/manual)*