# isDraft

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document is a draft that the user has not yet saved.

**Availability**:
- macOS 10.8+

## Declaration

```swift
nonisolated
var isDraft: Bool { get set }
```

```objc
@property (getter=isDraft) BOOL draft;
```

## Discussion

The system presents a Save dialog when the user closes a draft document. Only documents with non-`nil` values for the [`fileURL`](./fileurl.md) property should be considered drafts.

## See Also

### Getting Document Metadata
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](./isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var fileModificationDate: Date?](./filemodificationdate.md)
  The last-known modification date of the document’s on-disk representation.
- [var keepBackupFile: Bool](./keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var fileType: String?](./filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](./isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](./isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/isdraft)*