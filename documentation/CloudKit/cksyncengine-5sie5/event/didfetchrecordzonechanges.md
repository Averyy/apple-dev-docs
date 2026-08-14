# CKSyncEngine.Event.DidFetchRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about a finished record zone fetch.

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
struct DidFetchRecordZoneChanges
```

## Topics

### Identifying the record zone
- [let zoneID: CKRecordZone.ID](cksyncengine-5sie5/event/didfetchrecordzonechanges/zoneid.md)
  The associated record zone’s unique identifier.
### Handling errors
- [let error: CKError?](cksyncengine-5sie5/event/didfetchrecordzonechanges/error.md)
  An error that describes the cause of a failed fetch operation.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/didfetchrecordzonechanges/description.md)
  The textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/didfetchrecordzonechanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](cksyncengine-5sie5/event/willfetchrecordzonechanges(_:).md)
  The sync engine is about to fetch record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](cksyncengine-5sie5/event/willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md)
  The sync engine fetched new record zone changes from the server.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](cksyncengine-5sie5/event/fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](cksyncengine-5sie5/event/didfetchrecordzonechanges(_:).md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didfetchrecordzonechanges)*