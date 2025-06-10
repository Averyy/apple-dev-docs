# Deprecated Symbols

**Framework**: Core Data

Review unsupported symbols and their replacements.

## Topics

### Deprecated constants
- [let NSXMLExternalRecordType: String](nsxmlexternalrecordtype.md)
  Specifies an XML file format.
- [let NSBinaryExternalRecordType: String](nsbinaryexternalrecordtype.md)
  Specifies a binary file format
### Deprecated enumerations
- [enum NSPersistentStoreUbiquitousTransitionType](nspersistentstoreubiquitoustransitiontype.md)
  These constants are used as the value corresponding to the [`NSPersistentStoreUbiquitousTransitionTypeKey`](nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [`NSPersistentStoreCoordinatorStoresWillChangeNotification`](nspersistentstorecoordinatorstoreswillchangenotification.md) and [`NSPersistentStoreCoordinatorStoresDidChangeNotification`](nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change.
### Deprecated type properties
- [static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/NSPersistentStoreDidImportUbiquitousContentChanges.md)
  Posted after records are imported from the ubiquitous content store.
### Deprecated type methods
- [class func elementsDerived(fromExternalRecordAt: URL) -> [AnyHashable : Any]](nspersistentstorecoordinator/elementsderived(fromexternalrecordat:).md)
  Returns a dictionary containing the parsed elements derived from the Spotlight external record file that is specified by the given URL.
- [class func metadataForPersistentStore(with: URL) throws -> [AnyHashable : Any]](nspersistentstorecoordinator/metadataforpersistentstore(with:).md)
  Returns a dictionary that contains the metadata stored in the persistent store at the specified location.
- [class func metadataForPersistentStore(ofType: String?, at: URL) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:).md)
  Returns a dictionary containing the metadata stored in the persistent store at a given URL.
- [class func metadataForPersistentStore(ofType: String, at: URL, options: [AnyHashable : Any]?) throws -> [String : Any]](nspersistentstorecoordinator/metadataforpersistentstore(oftype:at:options:).md)
  Returns the metadata of a specific type of persistent store at the provided location.
- [class func registerStoreClass(AnyClass?, forStoreType: String)](nspersistentstorecoordinator/registerstoreclass(_:forstoretype:).md)
  Registers a persistent store subclass using the specified store type identifier.
- [class func removeUbiquitousContentAndPersistentStore(at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/removeubiquitouscontentandpersistentstore(at:options:).md)
  Deletes all ubiquitous content for all peers for the persistent store at a given URL and also delete the local store file.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String?, at: URL) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:).md)
  Sets the metadata for a given store.
- [class func setMetadata([String : Any]?, forPersistentStoreOfType: String, at: URL, options: [AnyHashable : Any]?) throws](nspersistentstorecoordinator/setmetadata(_:forpersistentstoreoftype:at:options:).md)
  Updates the metadata of a specific type of persistent store at the provided location.
### Deprecated instance methods
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
- [func tryLock() -> Bool](nspersistentstorecoordinator/trylock.md)
  Attempts to acquire a lock.
- [func unlock()](nspersistentstorecoordinator/unlock.md)
  Relinquishes a previously acquired lock.
- [func perform(() -> Void)](nspersistentstorecoordinator/perform(_:)-7jqb.md)
  Executes the provided closure asynchronously on the coordinator’s queue.
- [func performAndWait(() -> Void)](nspersistentstorecoordinator/performandwait(_:)-d3kq.md)
  Executes the provided closure on the coordinator’s queue and waits for it to finish.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator-deprecated-symbols)*