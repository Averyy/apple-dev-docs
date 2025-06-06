# migratePersistentStore(_:to:options:type:)

**Framework**: Core Data  
**Kind**: method

Changes the location and, if necessary, the store type of the specified persistent store.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func migratePersistentStore(_ store: NSPersistentStore, to storeURL: URL, options: [AnyHashable : Any]? = nil, type storeType: NSPersistentStore.StoreType) throws -> NSPersistentStore
```

#### Discussion

Performance may vary depending on the store types of the old and new stores. Invoking this method removes the specified store from the coordinator.

## Parameters

- `store`: The peristent store to migrate.
- `storeURL`: The location of the new persistent store.
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see  .
- `storeType`: The new store type. For possible values, see  .

## See Also

- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:type:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:).md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:))*