# migratePersistentStore(_:to:options:withType:)

**Framework**: Core Data  
**Kind**: method

Changes the location and, if necessary, the store type of the specified persistent store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func migratePersistentStore(_ store: NSPersistentStore, to URL: URL, options: [AnyHashable : Any]? = nil, withType storeType: String) throws -> NSPersistentStore
```

#### Return Value

If the migration is successful, the new store, otherwise `nil`.

#### Discussion

This method is typically used for “Save As” operations. Performance may vary depending on the type of old and new store. For more details of the action of this method, see Persistent Store Features in [`Core Data Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

> ❗ **Important**:  After invocation of this method, the specified store is removed from the coordinator thus `store` is no longer a useful reference.

## Parameters

- `store`: A persistent store.
- `URL`: An URL object that specifies the location for the new store.
- `options`: A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see  .
- `storeType`: A string constant (such as  ) that specifies the type of the new store—see  .

## See Also

- [func remove(NSPersistentStore) throws](nspersistentstorecoordinator/remove(_:).md)
  Removes the specified persistent store from the coordinator.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:type:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:type:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, type: NSPersistentStore.StoreType) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:type:).md)
  Replaces one persistent store with another.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:))*