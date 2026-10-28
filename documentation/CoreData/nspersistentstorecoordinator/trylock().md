# tryLock()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Attempts to acquire a lock.

**Availability**:
- iOS 3.0+ - Deprecated in 8.0
- iPadOS 3.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.4+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use -performBlock: instead

## Declaration

```swift
func tryLock() -> Bool
```

```objc
- (BOOL) tryLock;
```

## Return Value

[`true`](../../Swift/true.md) if successful, otherwise [`false`](../../Swift/false.md).

## Discussion

Returns immediately—contrast [`lock()`](./lock%28%29.md) which blocks.

## See Also

### Deprecated instance methods
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](./destroypersistentstore%28at,oftype,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt: URL, to: URL, options: [AnyHashable : Any]?, ofType: String) throws -> NSPersistentStore](./importstore%28withidentifier,fromexternalrecordsdirectoryat,to,options,oftype%29.md)
  Creates and populates a store with the external records found at a given URL.
- [func lock()](./lock%28%29.md)
  Attempts to acquire a lock.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](./replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,oftype%29.md)
  Replaces one persistent store with another.
- [func unlock()](./unlock%28%29.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](./perform%28_%29-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](./performandwait%28_%29-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/trylock())*