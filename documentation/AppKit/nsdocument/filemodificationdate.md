# fileModificationDate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The last-known modification date of the document’s on-disk representation.

**Availability**:
- macOS

## Declaration

```swift
nonisolated
var fileModificationDate: Date? { get set }
```

```objc
@property (copy, nullable) NSDate * fileModificationDate;
```

#### Discussion

The `NSDocument` default file saving machinery uses this information to warn the user when the on-disk representation of an open document has been modified by something other than the current app.

## See Also

### Getting Document Metadata
- [var fileURL: URL?](./fileurl.md)
  The location of the document’s on-disk representation.
- [var isEntireFileLoaded: Bool](./isentirefileloaded.md)
  A Boolean value that indicates whether the document’s file is completely loaded into memory.
- [var keepBackupFile: Bool](./keepbackupfile.md)
  A Boolean value that indicates whether the document archives previously saved versions of the document.
- [var isDraft: Bool](./isdraft.md)
  A Boolean value that indicates whether the document is a draft that the user has not yet saved.
- [var fileType: String?](./filetype.md)
  The name of the document type, as specified in the app’s information property-list file.
- [var isDocumentEdited: Bool](./isdocumentedited.md)
  A Boolean value that indicates whether the document has unsaved changes.
- [var isInViewingMode: Bool](./isinviewingmode.md)
  A Boolean value that indicates whether the document is in read-only mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/filemodificationdate)*