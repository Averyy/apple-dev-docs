# CKSyncEngine.Event.fetchedRecordZoneChanges(_:)

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The sync engine fetched new record zone changes from the server.

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
case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)
```

## See Also

### Remote record zone changes
- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](./willfetchrecordzonechanges%28_%29.md)
  The sync engine is about to fetch record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](./willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](./fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](./didfetchrecordzonechanges%28_%29.md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](./didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/fetchedrecordzonechanges(_:))*