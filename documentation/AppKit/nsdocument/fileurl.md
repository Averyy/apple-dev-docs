# fileURL

**Framework**: AppKit  
**Kind**: property

The location of the document’s on-disk representation.

**Availability**:
- macOS ?+

## Declaration

```swift
nonisolated
var fileURL: URL? { get set }
```

#### Return Value

The document’s location.

#### Discussion

The default implementation of this property returns the URL of the file that was opened. Changing the value of this property does not actually change the document’s name or location; it is only for recording the document’s location during its initial opening or saving.

## See Also

- [var isEntireFileLoaded: Bool](nsdocument/isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](nsdocument/filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/fileurl)*