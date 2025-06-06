# importStore(withIdentifier:fromExternalRecordsDirectoryAt:to:options:ofType:)

**Framework**: Core Data  
**Kind**: method

Creates and populates a store with the external records found at a given URL.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func importStore(withIdentifier storeIdentifier: String?, fromExternalRecordsDirectoryAt externalRecordsURL: URL, to destinationURL: URL, options: [AnyHashable : Any]? = nil, ofType storeType: String) throws -> NSPersistentStore
```

#### Return Value

An object representing the newly-created store.

## Parameters

- `storeIdentifier`: If this value is   then the method imports the records for the first store found.
- `externalRecordsURL`: The location of the directory containing external records.
- `destinationURL`: There should be no existing store at this location, as the store will be created from scratch (appending to an existing store is not allowed).
- `options`: A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see  .
- `storeType`: A string constant (such as  ) that specifies the type of the new store—see  .

## See Also

- [func remove(NSPersistentStore) throws](nspersistentstorecoordinator/remove(_:).md)
  Removes the specified persistent store from the coordinator.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func lock()](nspersistentstorecoordinator/lock.md)
  Attempts to acquire a lock.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.
- [func tryLock() -> Bool](nspersistentstorecoordinator/trylock.md)
  Attempts to acquire a lock.
- [func unlock()](nspersistentstorecoordinator/unlock.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/importstore(withidentifier:fromexternalrecordsdirectoryat:to:options:oftype:))*