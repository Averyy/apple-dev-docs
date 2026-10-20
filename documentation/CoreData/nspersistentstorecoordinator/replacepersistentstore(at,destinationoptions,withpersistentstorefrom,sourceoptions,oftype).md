# replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:ofType:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Replaces one persistent store with another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: Use [`replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:type:)`](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,type%29.md) instead.

## Declaration

```swift
func replacePersistentStore(at destinationURL: URL, destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions: [AnyHashable : Any]? = nil, ofType storeType: String) throws
```

```objc
- (BOOL) replacePersistentStoreAtURL:(NSURL *) destinationURL destinationOptions:(NSDictionary *) destinationOptions withPersistentStoreFromURL:(NSURL *) sourceURL sourceOptions:(NSDictionary *) sourceOptions storeType:(NSString *) storeType error:(NSError **) error;
```

## Parameters

- `destinationURL`: The location of the store to replace.
- `destinationOptions`: A dictionary containing key-value pairs that specify the behavior and characteristics of the store to replace. For more information, see [Store options](../store-options.md).
- `sourceURL`: The location of the store to use as the replacement.
- `sourceOptions`: A dictionary containing key-value pairs that specify the behavior and characteristics of the replacement store. For more information, see [Store options](../store-options.md).
- `storeType`: The store type of the replacement store. For possible values, see [`NSPersistentStore.StoreType`](../nspersistentstore/storetype.md).

## See Also

### Modifying a store
- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,type,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,type%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,type%29.md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,oftype,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:))*