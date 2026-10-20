# Deprecated Symbols

**Framework**: Core Data  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Topics

### Deprecated constants
- [let NSXMLExternalRecordType: String](./nsxmlexternalrecordtype.md)
  Specifies an XML file format.
- [let NSBinaryExternalRecordType: String](./nsbinaryexternalrecordtype.md)
  Specifies a binary file format
### Deprecated enumerations
- [enum NSPersistentStoreUbiquitousTransitionType](./nspersistentstoreubiquitoustransitiontype.md)
  These constants are used as the value corresponding to the [`NSPersistentStoreUbiquitousTransitionTypeKey`](./nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [`NSPersistentStoreCoordinatorStoresWillChangeNotification`](./nspersistentstorecoordinatorstoreswillchangenotification.md) and [`NSPersistentStoreCoordinatorStoresDidChangeNotification`](./nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change.
### Deprecated type properties
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.md)
  Posted after records are imported from the ubiquitous content store.
### Deprecated type methods
- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](./nspersistentstorecoordinator/elementsderived%28fromexternalrecordat%29.md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](./nspersistentstorecoordinator/metadataforpersistentstore%28with%29.md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](./nspersistentstorecoordinator/metadataforpersistentstore%28oftype,at%29.md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](./nspersistentstorecoordinator/metadataforpersistentstore%28oftype,at,options%29.md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](./nspersistentstorecoordinator/registerstoreclass%28_,forstoretype%29.md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func removeUbiquitousContentAndPersistentStore(at: URL, options: [AnyHashable : Any]?) throws](./nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore%28at,options%29.md)
  Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](./nspersistentstorecoordinator/setmetadata%28_,forpersistentstoreoftype,at%29.md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](./nspersistentstorecoordinator/setmetadata%28_,forpersistentstoreoftype,at,options%29.md)
  Updates the metadata of a specific type of persistent store at the provided location.
### Deprecated instance methods
- [func addPersistentStore(ofType: String, configurationName: String?, at: URL?, options: [AnyHashable : Any]?) throws -> NSPersistentStore](./nspersistentstorecoordinator/addpersistentstore%28oftype,configurationname,at,options%29.md)
  Adds a specific type of persistent store at the provided location.
- [func destroyPersistentStore(at: URL, ofType: String, options: [AnyHashable : Any]?) throws](./nspersistentstorecoordinator/destroypersistentstore%28at,oftype,options%29.md)
  Deletes a specific type of persistent store at the provided location.
- [func importStore(withIdentifier: String?, fromExternalRecordsDirectoryAt: URL, to: URL, options: [AnyHashable : Any]?, ofType: String) throws -> NSPersistentStore](./nspersistentstorecoordinator/importstore%28withidentifier,fromexternalrecordsdirectoryat,to,options,oftype%29.md)
  Creates and populates a store with the external records found at a given URL.
- [func lock()](./nspersistentstorecoordinator/lock%28%29.md)
  Attempts to acquire a lock.
- [func migratePersistentStore(NSPersistentStore, to: URL, options: [AnyHashable : Any]?, withType: String) throws -> NSPersistentStore](./nspersistentstorecoordinator/migratepersistentstore%28_,to,options,withtype%29.md)
  Changes the location and, if necessary, the store type of the specified persistent store.
- [func replacePersistentStore(at: URL, destinationOptions: [AnyHashable : Any]?, withPersistentStoreFrom: URL, sourceOptions: [AnyHashable : Any]?, ofType: String) throws](./nspersistentstorecoordinator/replacepersistentstore%28at,destinationoptions,withpersistentstorefrom,sourceoptions,oftype%29.md)
  Replaces one persistent store with another.
- [func tryLock() -> Bool](./nspersistentstorecoordinator/trylock%28%29.md)
  Attempts to acquire a lock.
- [func unlock()](./nspersistentstorecoordinator/unlock%28%29.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](./nspersistentstorecoordinator/perform%28_%29-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](./nspersistentstorecoordinator/performandwait%28_%29-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator-deprecated-symbols)*