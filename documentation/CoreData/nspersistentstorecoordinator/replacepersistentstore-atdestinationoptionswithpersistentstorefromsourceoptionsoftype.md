# replacePersistentStore(at:destinationOptions:withPersistentStoreFrom:sourceOptions:ofType:)

**Framework**: Core Data  
**Kind**: method

Replaces one persistent store with another.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replacePersistentStore(at destinationURL: URL, destinationOptions: [AnyHashable : Any]? = nil, withPersistentStoreFrom sourceURL: URL, sourceOptions: [AnyHashable : Any]? = nil, ofType storeType: String) throws
```

## Parameters

- `destinationURL`: The location of the store to replace.
- `destinationOptions`: A dictionary containing key-value pairs that specify the behavior and characteristics of the store to replace. For more information, see  .
- `sourceURL`: The location of the store to use as the replacement.
- `sourceOptions`: A dictionary containing key-value pairs that specify the behavior and characteristics of the replacement store. For more information, see  .
- `storeType`: The store type of the replacement store. For possible values, see  .

## See Also

- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:type:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:).md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:))*