# CKSyncEngine.Event.DidFetchChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about a finished database fetch.

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
struct DidFetchChanges
```

## Topics

### Debugging the event
- [var description: String](./didfetchchanges/description.md)
  The textual description of the event that’s suitable for logging.
### Instance Properties
- [let context: CKSyncEngine.FetchChangesContext](./didfetchchanges/context.md)
### Default Implementations
- [CustomStringConvertible Implementations](./didfetchchanges/customstringconvertible-implementations.md)

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
- [CKSyncEngine.Event.FetchedDatabaseChanges](./fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](./didfetchchanges%28_%29.md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didfetchchanges)*