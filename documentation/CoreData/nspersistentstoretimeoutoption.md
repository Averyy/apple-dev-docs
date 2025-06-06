# NSPersistentStoreTimeoutOption

**Framework**: Core Data  
**Kind**: var

Options key that specifies the connection timeout for Core Data stores.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSPersistentStoreTimeoutOption: String
```

#### Discussion

The corresponding value is an `NSNumber` object that represents the duration in seconds that Core Data will wait while attempting to create a connection to a persistent store. If a connection is cannot be made within that timeframe, the operation is aborted and an error is returned.

## See Also

- [let NSReadOnlyPersistentStoreOption: String](nsreadonlypersistentstoreoption.md)
  A flag that indicates whether a store is treated as read-only or not.
- [let NSValidateXMLStoreOption: String](nsvalidatexmlstoreoption.md)
  A flag that indicates whether an XML file should be validated with the DTD while opening.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoretimeoutoption)*