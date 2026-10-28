# CKSyncEngine.Event.FetchedRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about fetched record zone changes.

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
struct FetchedRecordZoneChanges
```

## Overview

> **Note**: Although CloudKit doesn’t guarantee the order of fetched record zone changes, the typical order for both deletions and modifications is oldest to newest.

## Topics

### Accessing changes
- [let deletions: [CKDatabase.RecordZoneChange.Deletion]](./fetchedrecordzonechanges/deletions.md)
  The fetched record zone deletions.
- [let modifications: [CKDatabase.RecordZoneChange.Modification]](./fetchedrecordzonechanges/modifications.md)
  The fetched record modifications.
### Debugging the event
- [var description: String](./fetchedrecordzonechanges/description.md)
  The textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./fetchedrecordzonechanges/customstringconvertible-implementations.md)

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
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](./didfetchrecordzonechanges%28_%29.md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](./didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetchedrecordzonechanges)*