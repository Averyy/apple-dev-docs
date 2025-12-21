# tryLock()

**Framework**: Core Data  
**Kind**: method

Attempts to acquire a lock.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
func tryLock() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Returns immediately—contrast [`lock()`](nspersistentstorecoordinator/lock().md) which blocks.

## See Also

- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](nspersistentstorecoordinator/addpersistentstore(oftype:configurationname:at:options:).md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/destroypersistentstore(at:oftype:options:).md)
  Deletes a specific type of persistent store at the provided location.
- [func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt: URL, to: URL, options: [AnyHashable : Any]?, ofType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/importstore(withidentifier:fromexternalrecordsdirectoryat:to:options:oftype:).md)
  Creates and populates a store with the external records found at a given URL.
- [func lock()](nspersistentstorecoordinator/lock.md)
  Attempts to acquire a lock.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](nspersistentstorecoordinator/migratepersistentstore(_:to:options:withtype:).md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](nspersistentstorecoordinator/replacepersistentstore(at:destinationoptions:withpersistentstorefrom:sourceoptions:oftype:).md)
  Replaces one persistent store with another.
- [func unlock()](nspersistentstorecoordinator/unlock.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/trylock())*