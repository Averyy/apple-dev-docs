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

### Instance Properties
- [let context: CKSyncEngine.FetchChangesContext](cksyncengine-5sie5/event/didfetchchanges/context.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](cksyncengine-5sie5/event/willfetchchanges(_:).md)
  An event indicating an imminent database fetch.
- [CKSyncEngine.Event.WillFetchChanges](cksyncengine-5sie5/event/willfetchchanges.md)
  A type that provides information about an imminent database fetch.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md)
  An event indicating there are fetched database changes to process.
- [CKSyncEngine.Event.FetchedDatabaseChanges](cksyncengine-5sie5/event/fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](cksyncengine-5sie5/event/didfetchchanges(_:).md)
  An event that indicates the database fetch is done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didfetchchanges)*