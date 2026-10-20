# extractBegin

**Framework**: Apple Archive  
**Kind**: property  
**Role**: Type Property

An entry message indicating the extraction operation has began, this is the first message for this entry.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
static let extractBegin: ArchiveHeader.EntryMessage
```

## See Also

### Entry Messages
- [static let convertExclude: ArchiveHeader.EntryMessage](./convertexclude.md)
  An entry message indicating the conversion operation has skipped the entry as the path data is an archive header instance.
- [static let decodeReading: ArchiveHeader.EntryMessage](./decodereading.md)
  An entry message indicating the decoder operation is reading the entry at path.
- [static let encodeScanning: ArchiveHeader.EntryMessage](./encodescanning.md)
  An entry message indicating the encoder operation is scanning the entry at path.
- [static let encodeWriting: ArchiveHeader.EntryMessage](./encodewriting.md)
  An entry message indicating the encoder operation is writing the entry at path.
- [static let extractACL: ArchiveHeader.EntryMessage](./extractacl.md)
  An entry message indicating the extraction operation has modified entry access control lists.
- [static let extractAttributes: ArchiveHeader.EntryMessage](./extractattributes.md)
  An entry message indicating the extraction operation has modified entry attributes, and that the data is an entry attributes instance.
- [static let extractEnd: ArchiveHeader.EntryMessage](./extractend.md)
  An entry message indicating the extraction operation has ended, this is the last message for this entry.
- [static let extractFail: ArchiveHeader.EntryMessage](./extractfail.md)
  An entry message indicating the extraction operation has failed, this is the last message for this entry.
- [static let extractXAT: ArchiveHeader.EntryMessage](./extractxat.md)
  An entry message indicating the extraction operation has modified entry extended attributes, and that the data is an entry extended attributes blob.
- [static let processExclude: ArchiveHeader.EntryMessage](./processexclude.md)
  An entry message indicating the process operation has skipped this entry and that the data is an archive header instance.
- [static let searchExclude: ArchiveHeader.EntryMessage](./searchexclude.md)
  An entry message indicating the operation has excluded the entry, specified by path, in search.
- [static let searchFail: ArchiveHeader.EntryMessage](./searchfail.md)
  An entry message indicating the operation has reported an error in search.
- [static let searchPruneDirectory: ArchiveHeader.EntryMessage](./searchprunedirectory.md)
  An entry message indicating the operation has skipped the directory, specified by path, in search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrymessage/extractbegin)*