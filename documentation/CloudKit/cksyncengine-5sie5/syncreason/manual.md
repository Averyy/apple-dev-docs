# CKSyncEngine.SyncReason.manual

**Framework**: CloudKit  
**Kind**: case

A manual sync operation.

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
case manual
```

#### Discussion

The sync engine uses this reason only when your app invokes the [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) and [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) methods.

## See Also

- [CKSyncEngine.SyncReason.scheduled](cksyncengine-5sie5/syncreason/scheduled.md)
  A scheduled sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/syncreason/manual)*