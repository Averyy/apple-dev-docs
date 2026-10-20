# importStore(withIdentifier:fromExternalRecordsDirectoryAt:to:options:ofType:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Creates and populates a store with the external records found at a given URL.

**Availability**:
- macOS 10.6+ - Deprecated in 10.13

> **Deprecated**: Spotlight integration is deprecated. Use CoreSpotlight integration instead.

## Declaration

```swift
func importStore(withIdentifier storeIdentifier: String?, fromExternalRecordsDirectoryAt externalRecordsURL: URL, to destinationURL: URL, options: [AnyHashable : Any]? = nil, ofType storeType: String) throws -> NSPersistentStore
```

```objc
- (NSPersistentStore *) importStoreWithIdentifier:(NSString *) storeIdentifier fromExternalRecordsDirectory:(NSURL *) externalRecordsURL toURL:(NSURL *) destinationURL options:(NSDictionary *) options withType:(NSString *) storeType error:(NSError **) error;
```

#### Return Value

An object representing the newly-created store.

## Parameters

- `storeIdentifier`: The identifier for a store.

  If this value is `nil` then the method imports the records for the first store found.
- `externalRecordsURL`: The location of the directory containing external records.
- `destinationURL`: An URL object that specifies the location for the new store.

  There should be no existing store at this location, as the store will be created from scratch (appending to an existing store is not allowed).
- `options`: A dictionary containing key-value pairs that specify whether the store should be read-only, and whether (for an XML store) the XML file should be validated against the DTD before it is read. For key definitions, see [Store options](../store-options.md).
- `storeType`: A string constant (such as `NSSQLiteStoreType`) that specifies the type of the new store—see [Persistent Store Types](../persistent-store-types.md).

## See Also

### Related Documentation
- [func remove(NSPersistentStore) throws](./remove%28_%29.md)
  Removes the specified persistent store from the coordinator.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
### Deprecated instance methods
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,oftype,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func lock()](./lock%28%29.md)
  Attempts to acquire a lock.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,oftype%29.md)
  Replaces one persistent store with another.
- [func tryLock() -> Bool](./trylock%28%29.md)
  Attempts to acquire a lock.
- [func unlock()](./unlock%28%29.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](./perform%28_%29-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](./performandwait%28_%29-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/importstore(withidentifier:fromexternalrecordsdirectoryat:to:options:oftype:))*