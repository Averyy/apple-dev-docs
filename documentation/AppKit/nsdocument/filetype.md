# fileType

**Framework**: AppKit  
**Kind**: property

The name of the document type, as specified in the app’s information property-list file.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var fileType: String? { get set }
```

#### Discussion

The document type affects how the data is filtered when it is written to or read from a file. When a document is saved, the type is determined by the entries in the app’s information property list (specified in `Info.plist)`.

You cannot use this property to change the document’s format after it has already been opened or saved. This property records only the initial document format used when first opening or saving the file.

## See Also

- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](nsdocument/isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](nsdocument/filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var keepBackupFile: Bool](nsdocument/keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var isDraft: Bool](nsdocument/isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var isDocumentEdited: Bool](nsdocument/isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](nsdocument/isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filetype)*