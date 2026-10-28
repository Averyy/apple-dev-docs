# CKSyncEngine.SyncReason.manual

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
- visionOS
- watchOS 10.0+

## Declaration

```swift
case manual
```

## Discussion

The sync engine uses this reason only when your app invokes the [`fetchChanges(_:)`](../fetchchanges%28_%29.md) and [`sendChanges(_:)`](../sendchanges%28_%29.md) methods.

## See Also

### Sync reasons
- [CKSyncEngine.SyncReason.scheduled](./scheduled.md)
  The sync engine automatically scheduled this sync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/syncreason/manual)*