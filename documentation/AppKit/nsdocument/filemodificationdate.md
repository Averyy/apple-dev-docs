# fileModificationDate

**Framework**: AppKit  
**Kind**: property

The last-known modification date of the document’s on-disk representation.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var fileModificationDate: Date? { get set }
```

#### Discussion

The `NSDocument` default file saving machinery uses this information to warn the user when the on-disk representation of an open document has been modified by something other than the current app.

## See Also

- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](nsdocument/isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var keepBackupFile: Bool](nsdocument/keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var isDraft: Bool](nsdocument/isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](nsdocument/filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](nsdocument/isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](nsdocument/isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filemodificationdate)*