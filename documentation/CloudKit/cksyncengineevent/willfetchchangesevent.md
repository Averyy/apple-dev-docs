# willFetchChangesEvent

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The event downcast to the subclass that represents an imminent database fetch.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, strong, readonly) CKSyncEngineWillFetchChangesEvent * willFetchChangesEvent;
```

## See Also

### Accessing fetch events
- [CKSyncEngineWillFetchChangesEvent](../cksyncenginewillfetchchangesevent.md)
  The sync engine is about to fetch changes from the server.
- [willFetchRecordZoneChangesEvent](./willfetchrecordzonechangesevent.md)
  The event downcast to the subclass that represents an imminent fetch of record zone changes.
- [CKSyncEngineWillFetchRecordZoneChangesEvent](../cksyncenginewillfetchrecordzonechangesevent.md)
  The sync engine finished fetching record zone changes from the server for a specific zone.
- [fetchedDatabaseChangesEvent](./fetcheddatabasechangesevent.md)
  The event downcast to the subclass that represents a set of fetched database changes to process.
- [CKSyncEngineFetchedDatabaseChangesEvent](../cksyncenginefetcheddatabasechangesevent.md)
  An object that provides information about fetched database changes.
- [fetchedRecordZoneChangesEvent](./fetchedrecordzonechangesevent.md)
  The event downcast to the subclass that represents a set of fetched record zone changes to process.
- [CKSyncEngineFetchedRecordZoneChangesEvent](../cksyncenginefetchedrecordzonechangesevent.md)
  An object that provides information about fetched record zone changes.
- [didFetchRecordZoneChangesEvent](./didfetchrecordzonechangesevent.md)
  The event downcast to the subclass that represents a completed record zone fetch.
- [CKSyncEngineDidFetchRecordZoneChangesEvent](../cksyncenginedidfetchrecordzonechangesevent.md)
  An object that provides information about a finished record zone fetch.
- [didFetchChangesEvent](./didfetchchangesevent.md)
  The event downcast to the subclass that represents a completed database fetch.
- [CKSyncEngineDidFetchChangesEvent](../cksyncenginedidfetchchangesevent.md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineevent/willfetchchangesevent)*