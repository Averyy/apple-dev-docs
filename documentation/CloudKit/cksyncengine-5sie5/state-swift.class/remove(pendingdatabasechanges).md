# remove(pendingDatabaseChanges:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified database changes from the state.

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
final func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])
```

## Discussion

Use this method when you no longer want the sync engine to send certain pending changes.

## Parameters

- `pendingDatabaseChanges`: An array of database changes.

## See Also

### Manipulating pending changes
- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](./add%28pendingdatabasechanges%29.md)
  Adds the specified database changes to the state.
- [CKSyncEngine.PendingDatabaseChange](../pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./add%28pendingrecordzonechanges%29.md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./remove%28pendingrecordzonechanges%29.md)
  Removes the specified record zone changes from the state.
- [CKSyncEngine.PendingRecordZoneChange](../pendingrecordzonechange.md)
  Describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:))*