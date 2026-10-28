# CKSyncEngine.Event.FetchedDatabaseChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about fetched database changes.

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
struct FetchedDatabaseChanges
```

## Overview

> **Note**: Although CloudKit doesn’t guarantee the order of fetched database changes, the typical order for both deletions and modifications is oldest to newest.

## Topics

### Accessing changes
- [let deletions: [CKDatabase.DatabaseChange.Deletion]](./fetcheddatabasechanges/deletions.md)
  The fetched record zone deletions.
- [enum CKSyncEngineZoneDeletionReason](../../cksyncenginezonedeletionreason.md)
  Describes the reason for a record zone deletion.
- [let modifications: [CKDatabase.DatabaseChange.Modification]](./fetcheddatabasechanges/modifications.md)
  The fetched record zone modifications.
### Debugging the event
- [var description: String](./fetcheddatabasechanges/description.md)
  The textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./fetcheddatabasechanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Remote database changes
- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](./willfetchchanges%28_%29.md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngine.Event.WillFetchChanges](./willfetchchanges.md)
  The sync engine is about to fetch changes from the server.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](./fetcheddatabasechanges%28_%29.md)
  The sync engine has fetched new database changes from the server.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](./didfetchchanges%28_%29.md)
  The sync engine finished fetching changes from the server.
- [CKSyncEngine.Event.DidFetchChanges](./didfetchchanges.md)
  A type that provides information about a finished database fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetcheddatabasechanges)*