# DataStoreSaveChangesRequest

**Framework**: SwiftData  
**Kind**: struct

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
struct DataStoreSaveChangesRequest<SnapshotType> where SnapshotType : DataStoreSnapshot
```

## Topics

### Instance Properties
- [let deleted: [SnapshotType]](datastoresavechangesrequest/deleted.md)
- [let editingState: EditingState](datastoresavechangesrequest/editingstate.md)
- [let inserted: [SnapshotType]](datastoresavechangesrequest/inserted.md)
- [let updated: [SnapshotType]](datastoresavechangesrequest/updated.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/datastoresavechangesrequest)*