# destroyPersistentStore(at:ofType:options:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Deletes a specific type of persistent store at the provided location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`destroyPersistentStore(at:type:options:)`](./destroypersistentstore%28at,type,options%29.md) instead.

## Declaration

```swift
func destroyPersistentStore(at url: URL, ofType storeType: String, options: [AnyHashable : Any]? = nil) throws
```

```objc
- (BOOL) destroyPersistentStoreAtURL:(NSURL *) url withType:(NSString *) storeType options:(NSDictionary *) options error:(NSError **) error;
```

## Parameters

- `url`: The store’s location.
- `storeType`: The store type. For possible values, see [`NSPersistentStore.StoreType`](../nspersistentstore/storetype.md).
- `options`: A dictionary containing key-value pairs that specify store behavior and characteristics. For more information, see [Store options](../store-options.md).

## See Also

### Modifying a store
- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,type,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,type%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,type%29.md)
  Replaces one persistent store with another.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,oftype%29.md)
  Replaces one persistent store with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:))*