# convertExclude

**Framework**: Apple Archive  
**Kind**: property

An entry message indicating the conversion operation has skipped the entry as the path data is an archive header instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static let convertExclude: ArchiveHeader.EntryMessage
```

## See Also

- [static let decodeReading: ArchiveHeader.EntryMessage](archiveheader/entrymessage/decodereading.md)
  An entry message indicating the decoder operation is reading the entry at path.
- [static let encodeScanning: ArchiveHeader.EntryMessage](archiveheader/entrymessage/encodescanning.md)
  An entry message indicating the encoder operation is scanning the entry at path.
- [static let encodeWriting: ArchiveHeader.EntryMessage](archiveheader/entrymessage/encodewriting.md)
  An entry message indicating the encoder operation is writing the entry at path.
- [static let extractACL: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractacl.md)
  An entry message indicating the extraction operation has modified entry access control lists.
- [static let extractAttributes: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractattributes.md)
  An entry message indicating the extraction operation has modified entry attributes, and that the data is an entry attributes instance.
- [static let extractBegin: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractbegin.md)
  An entry message indicating the extraction operation has began, this is the first message for this entry.
- [static let extractEnd: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractend.md)
  An entry message indicating the extraction operation has ended, this is the last message for this entry.
- [static let extractFail: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractfail.md)
  An entry message indicating the extraction operation has failed, this is the last message for this entry.
- [static let extractXAT: ArchiveHeader.EntryMessage](archiveheader/entrymessage/extractxat.md)
  An entry message indicating the extraction operation has modified entry extended attributes, and that the data is an entry extended attributes blob.
- [static let processExclude: ArchiveHeader.EntryMessage](archiveheader/entrymessage/processexclude.md)
  An entry message indicating the process operation has skipped this entry and that the data is an archive header instance.
- [static let searchExclude: ArchiveHeader.EntryMessage](archiveheader/entrymessage/searchexclude.md)
  An entry message indicating the operation has excluded the entry, specified by path, in search.
- [static let searchFail: ArchiveHeader.EntryMessage](archiveheader/entrymessage/searchfail.md)
  An entry message indicating the operation has reported an error in search.
- [static let searchPruneDirectory: ArchiveHeader.EntryMessage](archiveheader/entrymessage/searchprunedirectory.md)
  An entry message indicating the operation has skipped the directory, specified by path, in search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrymessage/convertexclude)*