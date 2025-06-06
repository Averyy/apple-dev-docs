# destroyPersistentStore(at:type:options:)

**Framework**: Core Data  
**Kind**: method

Deletes a specific type of persistent store at the provided location.

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
func destroyPersistentStore(at url: URL, type storeType: NSPersistentStore.StoreType, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `url`: The store’s location.
- `storeType`: The store type. For possible values, see  .
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see  .

## See Also

- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:).md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:type:options:))*