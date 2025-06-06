# NSExternalRecordExtensionOption

**Framework**: Core Data  
**Kind**: var

Option indicating the file extension to use for Spotlight external record files.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let NSExternalRecordExtensionOption: String
```

## See Also

- [let NSExternalRecordsDirectoryOption: String](nsexternalrecordsdirectoryoption.md)
  Option indicating the directory where Spotlight external record files should be written to.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsexternalrecordextensionoption)*