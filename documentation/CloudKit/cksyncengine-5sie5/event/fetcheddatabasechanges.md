# CKSyncEngine.Event.FetchedDatabaseChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about fetched database changes.

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
struct FetchedDatabaseChanges
```

#### Overview

> **Note**:  Although CloudKit doesn’t guarantee the order of fetched database changes, the typical order for both deletions and modifications is oldest to newest.

## Topics

### Accessing changes
- [let deletions: [CKDatabase.DatabaseChange.Deletion]](cksyncengine-5sie5/event/fetcheddatabasechanges/deletions.md)
  The fetched record deletions.
- [enum CKSyncEngineZoneDeletionReason](cksyncenginezonedeletionreason.md)
  Describes the reason for a record zone deletion.
- [let modifications: [CKDatabase.DatabaseChange.Modification]](cksyncengine-5sie5/event/fetcheddatabasechanges/modifications.md)
  The fetched record modifications.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](cksyncengine-5sie5/event/willfetchchanges(_:).md)
  An event indicating an imminent database fetch.
- [CKSyncEngine.Event.WillFetchChanges](cksyncengine-5sie5/event/willfetchchanges.md)
  A type that provides information about an imminent database fetch.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md)
  An event indicating there are fetched database changes to process.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](cksyncengine-5sie5/event/didfetchchanges(_:).md)
  An event that indicates the database fetch is done.
- [CKSyncEngine.Event.DidFetchChanges](cksyncengine-5sie5/event/didfetchchanges.md)
  A type that provides information about a finished database fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetcheddatabasechanges)*