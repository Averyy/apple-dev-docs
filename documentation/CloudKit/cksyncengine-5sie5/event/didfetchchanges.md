# CKSyncEngine.Event.DidFetchChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about a finished database fetch.

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
struct DidFetchChanges
```

## Topics

### Debugging the event
- [var description: String](cksyncengine-5sie5/event/didfetchchanges/description.md)
  The textual description of the event that’s suitable for logging.
### Instance Properties
- [let context: CKSyncEngine.FetchChangesContext](cksyncengine-5sie5/event/didfetchchanges/context.md)
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/didfetchchanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](cksyncengine-5sie5/event/willfetchchanges(_:).md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngine.Event.WillFetchChanges](cksyncengine-5sie5/event/willfetchchanges.md)
  The sync engine is about to fetch changes from the server.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md)
  The sync engine has fetched new database changes from the server.
- [CKSyncEngine.Event.FetchedDatabaseChanges](cksyncengine-5sie5/event/fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](cksyncengine-5sie5/event/didfetchchanges(_:).md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didfetchchanges)*