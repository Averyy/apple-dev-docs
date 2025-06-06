# NSPersistentStoreUbiquitousContentURLKey

**Framework**: Core Data  
**Kind**: var

Option to specify the log path to use for ubiquitous content logs.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
let NSPersistentStoreUbiquitousContentURLKey: String
```

#### Discussion

In iOS 6 and OS X 10.8 and below, this option is required for ubiquitous content to function. In iOS 7 and macOS 10.9 and later, it is optional.

## See Also

- [let NSExternalRecordsDirectoryOption: String](nsexternalrecordsdirectoryoption.md)
  Option indicating the directory where Spotlight external record files should be written to.
- [let NSExternalRecordExtensionOption: String](nsexternalrecordextensionoption.md)
  Option indicating the file extension to use for Spotlight external record files.
- [let NSExternalRecordsFileFormatOption: String](nsexternalrecordsfileformatoption.md)
  Option to specify the file format of a Spotlight external records.
- [let NSPersistentStoreUbiquitousContentNameKey: String](nspersistentstoreubiquitouscontentnamekey.md)
  Option to specify that a persistent store has a given name in ubiquity.
- [let NSPersistentStoreUbiquitousPeerTokenOption: String](nspersistentstoreubiquitouspeertokenoption.md)
  The corresponding value is an optionally specified string which will be mixed in to Core Data’s identifier for each iCloud peer. The value must be an alphanumeric string without any special characters, whitespace or punctuation. The primary use for this option is to allow multiple applications on the same peer (device) to share a Core Data store integrated with iCloud. Each application will require its own store file.
- [let NSPersistentStoreRemoveUbiquitousMetadataOption: String](nspersistentstoreremoveubiquitousmetadataoption.md)
  The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should remove all associated ubiquity metadata from a persistent store. You typically use this option during migration or copying to disassociate a persistent store file from an iCloud account.
- [let NSPersistentStoreUbiquitousContainerIdentifierKey: String](nspersistentstoreubiquitouscontaineridentifierkey.md)
  The a string specifying the iCloud container identifier.
- [let NSPersistentStoreRebuildFromUbiquitousContentOption: String](nspersistentstorerebuildfromubiquitouscontentoption.md)
  The corresponding value is an `NSNumber` object representing a boolean that indicates whether the receiver should erase the local store file and rebuild it from the iCloud data in Mobile Documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontenturlkey)*