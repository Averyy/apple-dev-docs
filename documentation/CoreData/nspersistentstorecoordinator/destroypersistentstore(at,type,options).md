# destroyPersistentStore(at:type:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Deletes a specific type of persistent store at the provided location.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func destroyPersistentStore(at url: URL, type storeType: NSPersistentStore.StoreType, options: [AnyHashable : Any]? = nil) throws
```

## Parameters

- `url`: The store’s location.
- `storeType`: The store type. For possible values, see [`NSPersistentStore.StoreType`](../nspersistentstore/storetype.md).
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Modifying a store
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,type%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,type%29.md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,oftype,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,oftype%29.md)
  Replaces one persistent store with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:type:options:))*