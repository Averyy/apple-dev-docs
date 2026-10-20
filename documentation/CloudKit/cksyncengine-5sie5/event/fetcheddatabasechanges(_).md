# CKSyncEngine.Event.fetchedDatabaseChanges(_:)

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The sync engine has fetched new database changes from the server.

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
case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)
```

## See Also

### Remote database changes
- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](./willfetchchanges%28_%29.md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngine.Event.WillFetchChanges](./willfetchchanges.md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngine.Event.FetchedDatabaseChanges](./fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](./didfetchchanges%28_%29.md)
  The sync engine finished fetching changes from the server.
- [CKSyncEngine.Event.DidFetchChanges](./didfetchchanges.md)
  A type that provides information about a finished database fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetcheddatabasechanges(_:))*