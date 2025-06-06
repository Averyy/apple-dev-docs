# isDraft

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document is a draft that the user has not yet saved.

**Availability**:
- macOS 10.8+

## Declaration

```swift
nonisolated
var isDraft: Bool { get set }
```

#### Discussion

The system presents a Save dialog when the user closes a draft document. Only documents with non-`nil` values for the [`fileURL`](nsdocument/fileurl.md) property should be considered drafts.

## See Also

- [var fileURL: URL?](nsdocument/fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](nsdocument/isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](nsdocument/filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var keepBackupFile: Bool](nsdocument/keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var fileType: String?](nsdocument/filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](nsdocument/isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](nsdocument/isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isdraft)*