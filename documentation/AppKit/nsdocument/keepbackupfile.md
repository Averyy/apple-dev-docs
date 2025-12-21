# keepBackupFile

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document archives previously saved versions of the document.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var keepBackupFile: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which causes each new save operation to replace the document’s on-disk content. If you override this method and return [`true`](https://developer.apple.com/documentation/Swift/true), a save operation saves the document’s previous contents in a backup file before saving the current contents.

## See Also

- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](nsdocument/isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](nsdocument/filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var isDraft: Bool](nsdocument/isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](nsdocument/filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](nsdocument/isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](nsdocument/isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/keepbackupfile)*