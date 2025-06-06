# Store options

**Framework**: Core Data

The options keys that configure the behavior and characteristics of a persistent store.

## Topics

### Constants
- [let NSReadOnlyPersistentStoreOption: String](nsreadonlypersistentstoreoption.md)
  A flag that indicates whether a store is treated as read-only or not.
- [let NSValidateXMLStoreOption: String](nsvalidatexmlstoreoption.md)
  A flag that indicates whether an XML file should be validated with the DTD while opening.
- [let NSPersistentStoreTimeoutOption: String](nspersistentstoretimeoutoption.md)
  Options key that specifies the connection timeout for Core Data stores.
- [let NSSQLitePragmasOption: String](nssqlitepragmasoption.md)
  Options key for a dictionary of SQLite pragma settings with pragma values indexed by pragma names as keys.
- [let NSSQLiteAnalyzeOption: String](nssqliteanalyzeoption.md)
  Option key to run an analysis of the store data to optimize indices based on statistical information when the store is added to the coordinator.
- [let NSSQLiteManualVacuumOption: String](nssqlitemanualvacuumoption.md)
  Option key to rebuild the store file, forcing a database wide defragmentation when the store is added to the coordinator.
- [let NSPersistentStoreFileProtectionKey: String](nspersistentstorefileprotectionkey.md)
  Key to represent the protection class for the persistent store.
- [let NSPersistentStoreForceDestroyOption: String](nspersistentstoreforcedestroyoption.md)
  A flag that indicates the coordinator destroys the store file even if the operation might be unsafe, overriding locks, if necessary.
### Deprecated
- [let NSExternalRecordsDirectoryOption: String](nsexternalrecordsdirectoryoption.md)
  Option indicating the directory where Spotlight external record files should be written to.
- [let NSExternalRecordExtensionOption: String](nsexternalrecordextensionoption.md)
  Option indicating the file extension to use for Spotlight external record files.
- [let NSExternalRecordsFileFormatOption: String](nsexternalrecordsfileformatoption.md)
  Option to specify the file format of a Spotlight external records.
- [let NSPersistentStoreUbiquitousContentNameKey: String](nspersistentstoreubiquitouscontentnamekey.md)
  Option to specify that a persistent store has a given name in ubiquity.
- [let NSPersistentStoreUbiquitousContentURLKey: String](nspersistentstoreubiquitouscontenturlkey.md)
  Option to specify the log path to use for ubiquitous content logs.
- [let NSPersistentStoreUbiquitousPeerTokenOption: String](nspersistentstoreubiquitouspeertokenoption.md)
  The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file.
- [let NSPersistentStoreRemoveUbiquitousMetadataOption: String](nspersistentstoreremoveubiquitousmetadataoption.md)
  The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account.
- [let NSPersistentStoreUbiquitousContainerIdentifierKey: String](nspersistentstoreubiquitouscontaineridentifierkey.md)
  The a string specifying the iCloud container identifier.
- [let NSPersistentStoreRebuildFromUbiquitousContentOption: String](nspersistentstorerebuildfromubiquitouscontentoption.md)
  The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents.

## See Also

- [init(managedObjectModel: NSManagedObjectModel)](nspersistentstorecoordinator/init(managedobjectmodel:).md)
  Creates a persistent store coordinator with the specified managed object model.
- [Migration options](migration-options.md)
  The options keys that configure the migration behavior of a persistent store.
- [Store versions](store-versions.md)
  The metadata keys you use when comparing store versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/store-options)*