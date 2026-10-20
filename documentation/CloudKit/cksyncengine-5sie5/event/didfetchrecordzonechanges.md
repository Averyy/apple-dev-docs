# CKSyncEngine.Event.DidFetchRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about a finished record zone fetch.

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
struct DidFetchRecordZoneChanges
```

## Topics

### Identifying the record zone
- [let zoneID: CKRecordZone.ID](./didfetchrecordzonechanges/zoneid.md)
  The associated record zone’s unique identifier.
### Handling errors
- [let error: CKError?](./didfetchrecordzonechanges/error.md)
  An error that describes the cause of a failed fetch operation.
### Debugging the event
- [var description: String](./didfetchrecordzonechanges/description.md)
  The textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./didfetchrecordzonechanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Remote record zone changes
- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](./willfetchrecordzonechanges%28_%29.md)
  The sync engine is about to fetch record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](./willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](./fetchedrecordzonechanges%28_%29.md)
  The sync engine fetched new record zone changes from the server.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](./fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](./didfetchrecordzonechanges%28_%29.md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didfetchrecordzonechanges)*