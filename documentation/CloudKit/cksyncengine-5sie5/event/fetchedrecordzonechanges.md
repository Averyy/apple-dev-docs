# CKSyncEngine.Event.FetchedRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about fetched record zone changes.

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
struct FetchedRecordZoneChanges
```

#### Overview

> **Note**:  Although CloudKit doesn’t guarantee the order of fetched record zone changes, the typical order for both deletions and modifications is oldest to newest.

## Topics

### Accessing changes
- [let deletions: [CKDatabase.RecordZoneChange.Deletion]](cksyncengine-5sie5/event/fetchedrecordzonechanges/deletions.md)
  The fetched record zone deletions.
- [let modifications: [CKDatabase.RecordZoneChange.Modification]](cksyncengine-5sie5/event/fetchedrecordzonechanges/modifications.md)
  The fetched record zone modifications.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](cksyncengine-5sie5/event/willfetchrecordzonechanges(_:).md)
  An event indicating an imminent fetch of changes in a record zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](cksyncengine-5sie5/event/willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md)
  An event indicating there are fetched record zone changes to process.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](cksyncengine-5sie5/event/didfetchrecordzonechanges(_:).md)
  An event that indicates the record zone fetch is done.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](cksyncengine-5sie5/event/didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetchedrecordzonechanges)*