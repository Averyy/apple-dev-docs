# remove(pendingRecordZoneChanges:)

**Framework**: CloudKit  
**Kind**: method

Removes the specified record zone changes from the state.

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
final func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])
```

## Parameters

- `pendingRecordZoneChanges`: An array of record zone changes.

## See Also

- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](cksyncengine-5sie5/pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md)
  Adds the specified record zone changes to the state.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/remove(pendingrecordzonechanges:))*