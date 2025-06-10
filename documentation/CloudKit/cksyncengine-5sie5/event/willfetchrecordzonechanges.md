# CKSyncEngine.Event.WillFetchRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about an imminent fetch of changes in a record zone.

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
struct WillFetchRecordZoneChanges
```

## Topics

### Identifying the record zone
- [let zoneID: CKRecordZone.ID](cksyncengine-5sie5/event/willfetchrecordzonechanges/zoneid.md)
  The associated record zone’s unique identifier.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](cksyncengine-5sie5/event/willfetchrecordzonechanges(_:).md)
  An event indicating an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md)
  An event indicating there are fetched record zone changes to process.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](cksyncengine-5sie5/event/fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](cksyncengine-5sie5/event/didfetchrecordzonechanges(_:).md)
  An event that indicates the record zone fetch is done.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](cksyncengine-5sie5/event/didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/willfetchrecordzonechanges)*